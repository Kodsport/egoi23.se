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

pictures_dir_path = sys.argv[2]

delegations = {}

with open(sys.argv[1], newline='') as fp:
	csv_reader = csv.reader(fp)
	rows = list(csv_reader)
	first_row = rows.pop(0)
	consent_form_col_idx = first_row.index("consent form filename")
	picture_col_idx = first_row.index("profile picture filename")
	for row in rows:
		if len(row) < 4:
			continue
		country, role, passport_name, display_name = row[:4]
		if not display_name:
			continue
		if role not in ROLES_TO_INCLUDE:
			skipped_roles.add(role)
			continue
		
		consent_form_link = row[consent_form_col_idx].lower()
		if consent_form_link:
			if "consent" not in consent_form_link:
				print(f"warning! filename does not look like a consent form: {consent_form_link}")
				consent_form_link = ""
			elif not os.path.exists(pictures_dir_path + "/" + consent_form_link):
				print(f"warning! consent form file does not exist: " + pictures_dir_path + "/" + consent_form_link)
				consent_form_link = ""
		else:
			print(f"no consent form for {display_name}")
		if country not in delegations:
			delegations[country] = []
		delegations[country].append((role, display_name, passport_name, row[picture_col_idx].lower(), bool(consent_form_link)))

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

delegations_yaml_lines = []
images_to_copy = []

for country_name, people in delegations:
	#print(country_name)
	delegations_yaml_lines.append(f"- name: {country_name}")
	delegations_yaml_lines.append("  people:")
	people.sort(key=lambda p: (ROLES_TO_INCLUDE.index(p[0]), p[1]))
	for idx, (role, display_name, passport_name, profile_picture_path, has_consent_form) in enumerate(people):
		#print(f"  {role:<15}  {display_name:>35}  {profile_picture_path}")
		
		delegations_yaml_lines.append(f"  - name: {display_name}")
		if role == "Leader":
			delegations_yaml_lines.append(f"    role: tl")
			img_suffix = "_tl"
		elif role == "Deputy Leader":
			delegations_yaml_lines.append(f"    role: dtl")
			img_suffix = "_dtl"
		else:
			img_suffix = "_c" + str(idx + 1)
		if profile_picture_path and has_consent_form:
			full_path = pictures_dir_path + "/" + profile_picture_path
			if os.path.exists(full_path):
				img_name = unidecode(country_name).lower().replace(' ', '_') + img_suffix + ".jpg"
				delegations_yaml_lines.append("    img: " + img_name)
				images_to_copy.append((pictures_dir_path + "/" + profile_picture_path, img_name))
			else:
				print("profile picture not found: " + full_path)

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
