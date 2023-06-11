---
title: Schedule
layout: default
background: bkg/ma.jpg
extraCSS: schedule.css
extraJS: schedule.js

minTime: 7
maxTime: 22
timeRemPerHour: 6
---

<div id="sch-tabs">
{% for day in site.data.schedule %}
<div class="sch-tab"><span class="sch-tab-month">July</span> {{ day.date }}</div>
{% endfor %}
</div>

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
				{% unless event.compact %}
				{% assign minutes = event.time[0] | modulo: 1 | times: 60 | round %}
				<div class="sch-event-top">
					<span class="sch-event-time">
						{{ event.time[0] | floor }}:{% if minutes < 10 %}0{% endif %}{{ minutes }}
					</span>
					{% if event.location %}
					<span class="sch-event-location">
						{{ event.location }}
					</span>
					{% endif %}
				</div>
				{% endunless %}
				<div class="sch-event-vspace"></div>
				<div class="sch-event-desc">{{ event.name }}</div>
				{% if event.showEndTime %}
				<span class="sch-event-time">
					{% assign minutes = event.time[1] | modulo: 1 | times: 60 | round %}
					{{ event.time[1] | floor }}:{% if minutes < 10 %}0{% endif %}{{ minutes }}
				</span>
				{% endif %}
			</div>
		{% endfor %}
		</div>
		<div class="sch-day-bottom"></div>
	</div>
	{% endfor %}
</div>
