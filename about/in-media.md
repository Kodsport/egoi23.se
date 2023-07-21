---
title: EGOI in Media
layout: default
background: bkg/ma.jpg
backgroundAlign: bottom
---

EGOI 2023 has been featured in various Swedish media. Here are links to some articles (all in Swedish):

<ul>
{% for item in site.data.media %}
	<li>
		<a href="{{ item.url }}" target="_blank">
			<b>{{ item.source }}:</b> {{ item.title }}
		</a>
	</li>
{% endfor %}
</ul>
