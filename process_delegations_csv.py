#!/bin/python3

import sys
import csv
import os
from unidecode import unidecode
from wand.image import Image

if len(sys.argv) < 3:
	print("usage: process_delegations.py [path/to/people.csv] [path/to/pictures/]")
	exit(0)

ROLES_TO_INCLUDE = ["Contestant", "Leader", "Deputy Leader"]

skipped_roles = set()

delegations = {}

with open(sys.argv[1], newline='') as fp:
	csv_reader = csv.reader(fp)
	for row in csv_reader:
		if len(row) < 4:
			continue
		country, role, passport_name, display_name = row[:4]
		if not display_name:
			continue
		if role in ROLES_TO_INCLUDE:
			if country not in delegations:
				delegations[country] = []
			delegations[country].append((role, display_name, passport_name))
		else:
			skipped_roles.add(role)
print("skipped roles:", skipped_roles)

delegations = list(delegations.items())
delegations.sort()

def remove_repeated_underscore(s: str):
	result = []
	for c in s:
		if result and result[-1] == "_" and c == "_":
			continue
		result.append(c)
	return "".join(result)

consent_forms = set()
profile_picture_paths = {}
pictures_dir_path = sys.argv[2]
for file_name in os.listdir(pictures_dir_path):
	file_name_lower = file_name.lower()
	
	file_name_lower = file_name_lower.replace("photo", "picture")
	file_name_lower = file_name_lower.replace("pricture", "picture")
	file_name_lower = file_name_lower.replace("profie", "profile")
	file_name_lower = file_name_lower.replace("pofile", "profile")
	file_name_lower = file_name_lower.replace("plofile", "profile")
	
	file_name_lower = remove_repeated_underscore(file_name_lower.replace(" ", "_"))
	
	if "picture" in file_name_lower:
		name = file_name_lower[:file_name_lower.index("picture")]
		name = name.removesuffix("profile_")
		name = name.removesuffix("_")
		name = unidecode(name)
		profile_picture_paths[name] = file_name
	elif "consent_form" in file_name_lower:
		name = file_name_lower[:file_name_lower.index("consent_form")]
		name = name.removesuffix("_")
		name = unidecode(name)
		consent_forms.add(name)
	else:
		print("unrecognized file name format: " + file_name)

def unidecode2(s: str):
	return s.replace("ö", "oe").replace("ø", "oe").replace("å", "aa")

def find_profile_picture(name):
	name = unidecode(remove_repeated_underscore(name.lower().replace(" ", "_").replace(",", "")))
	if name in profile_picture_paths and name in consent_forms:
		return profile_picture_paths[name]
	
	name_parts = name.split("_")
	name_without_underscore = name.replace("_", "")
	matches = []
	for picture_name, file_name in profile_picture_paths.items():
		if picture_name not in consent_forms:
			continue
		if picture_name.replace("_", "") == name_without_underscore:
			matches.append(file_name)
			continue
		picture_name_parts = picture_name.split("_")
		if name_parts[0] in [picture_name_parts[0], picture_name_parts[-1]] and all(map(lambda p: p in name_parts, picture_name_parts)):
			matches.append(file_name)
	if len(matches) == 1:
		return matches[0]
	elif len(matches) > 1:
		print(f"multiple matches for {name}:", matches)
	return None

missing_profile_pictures = 0

delegations_yaml_lines = []
images_to_copy = []

for country_name, people in delegations:
	print(country_name)
	delegations_yaml_lines.append(f"- name: {country_name}")
	delegations_yaml_lines.append("  people:")
	people.sort(key=lambda p: (ROLES_TO_INCLUDE.index(p[0]), p[1]))
	for idx, (role, display_name, passport_name) in enumerate(people):
		profile_picture_path = find_profile_picture(display_name) or find_profile_picture(passport_name) or find_profile_picture(unidecode2(display_name))
		if profile_picture_path is None:
			missing_profile_pictures += 1
		print(f"  {role:<15}  {display_name:>35}  {profile_picture_path}")
		
		delegations_yaml_lines.append(f"  - name: {display_name}")
		if role == "Leader":
			delegations_yaml_lines.append(f"    role: tl")
			img_suffix = "_tl"
		elif role == "Deputy Leader":
			delegations_yaml_lines.append(f"    role: dtl")
			img_suffix = "_dtl"
		else:
			img_suffix = "_c" + str(idx + 1)
		if profile_picture_path:
			img_name = unidecode(country_name).lower().replace(' ', '_') + img_suffix + ".jpg"
			delegations_yaml_lines.append("    img: " + img_name)
			images_to_copy.append((pictures_dir_path + "/" + profile_picture_path, img_name))

print("missing pictures:", missing_profile_pictures)

with open("_data/delegations.yml", "w") as delegations_yml_fp:
	delegations_yml_fp.write("\n".join(delegations_yaml_lines))

IMAGE_HEIGHT = 300

DELEGATIONS_IMG_PATH = "assets/images/delegations/"

if os.path.exists(DELEGATIONS_IMG_PATH):
	for filename in os.listdir(DELEGATIONS_IMG_PATH):
		os.unlink(DELEGATIONS_IMG_PATH + filename)
else:
	os.mkdir(DELEGATIONS_IMG_PATH)

for img_src, img_dst in images_to_copy:
	with Image(filename=img_src) as img:
		width = round(IMAGE_HEIGHT * img.width / img.height)
		img.resize(width, IMAGE_HEIGHT)
		img.save(filename="assets/images/delegations/" + img_dst)
