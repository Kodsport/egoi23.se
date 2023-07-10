---
title: Delegations
layout: default
background: bkg/sjonsjon.jpg
extraCSS: delegations.css
---

{% for delegation in site.data.delegations %}
<div class="delegation-outer">
<h3>{{ delegation.name }}</h3>
<div class="delegation-people">
	{% for p in delegation.people %}
	<div class="delegation-person" data-role="{{ p.role | default: 'c' }}">
		{% if p.img %}
		<img class="profile-picture" src="/assets/images/delegations/{{ p.img }}">
		{% else %}
		<img class="profile-picture" src="/assets/images/organizers/empty.svg">
		{% endif %}
		<div class="p-name">{{ p.name }}</div>
		<div class="p-role">
			{% if p.role == "tl" %}
			Leader
			{% elsif p.role == "dtl" %}
			Deputy Leader
			{% else %}
			Contestant
			{% endif %}
		</div>
	</div>
	{% endfor %}
</div>
</div>
<div class="hr"></div>
{% endfor %}
