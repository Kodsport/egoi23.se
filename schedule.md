---
title: Schedule
layout: default
background: bkg/ma.jpg
extraCSS: schedule.css

minTime: 7
maxTime: 24
timeRemPerHour: 2
---

This is the preliminary schedule and is still subject to change.

<div id="sch-dividers-wrapper">
<div id="sch-dividers">
	{% for i in (page.minTime..page.maxTime) %}
	<div class="sch-divider" style="height: {{ page.timeRemPerHour }}rem;">
		<div class="sch-divider-num">{{i}}</div>
	</div>
	{% endfor %}
</div>
</div>
<div id="sch-wrapper">
	{% for day in site.data.schedule %}
	<div class="sch-day {% if day.compressed %} sch-day-compressed {% endif %}">
		<div class="sch-day-header">
			<h4><span class="fl">{{ day.day }}.</span> July {{ day.date }}</h4>
			{% unless day.compressed %}
			<div class="sch-day-subheader">
				<div>Contestants</div>
				<div>Leaders</div>
			</div>
			{% endunless %}
		</div>
			
		<div class="sch-events-wrapper" style="height: {{ page.maxTime | minus: page.minTime | times: page.timeRemPerHour }}rem;">
		{% for event in day.events %}
			<div class="sch-event" data-for="{{ event.for | default: 'lc' }}" data-color="{{ event.color | default: '' }}" style="
				margin-top: {{ event.time[0] | minus: page.minTime | times: page.timeRemPerHour | plus: 0.1 }}rem;
				height: {{ event.time[1] | minus: event.time[0] | times: page.timeRemPerHour | minus: 0.2 }}rem;
			">
			{{ event.name }}
			</div>
		{% endfor %}
		</div>
	</div>
	{% endfor %}
</div>
