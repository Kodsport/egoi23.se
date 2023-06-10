---
title: Organizing Team
layout: default
background: bkg/sjonsjon.jpg
backgroundAlign: bottom
extraCSS: organizers.css
---

{% for list in site.data.organizers %}
<h1>{{ list.title }}</h1>
<div class="organizers-list">
{% for item in list.people %}
<div class="organizer-box">
	<img src="{{ '/assets/images/organizers/' | append: item.imgname | relative_url }}" alt="{{ item.name }}">
	<div class="organizer-name">{{ item.name }}</div>
	<div class="fl">{{ item.title }}</div>
</div>
{% endfor %}
</div>
{% endfor %}
