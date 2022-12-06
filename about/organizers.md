---
title: Organizing Team
layout: default
background: bkg/sjonsjon.jpg
backgroundAlign: bottom
extraCSS: organizers.css
---

<div class="organizers-list">
{% for item in site.data.organizers %}
<div class="organizer-box">
	<img src="{{ '/assets/images/organizers/' | append: item.imgname | relative_url }}" alt="{{ item.name }}">
	<div class="organizer-name">{{ item.name }}</div>
	<div class="fl">{{ item.title }}</div>
</div>
{% endfor %}
</div>

# Jury
<div class="hr"></div>
<div class="organizers-list">
{% for item in site.data.jury %}
<div class="organizer-box">
	<img src="{{ '/assets/images/organizers/' | append: item.imgname | relative_url }}" alt="{{ item.name }}">
	<div class="organizer-name">{{ item.name }}</div>
	<div class="fl">{{ item.title }}</div>
</div>
{% endfor %}
</div>

<!--
# Volunteers
<div class="hr"></div>
-->
