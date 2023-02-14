---
title: Contact
layout: default
background: bkg/ma.jpg
---

The organizing committee consists of a team of nine.<br>
You can contact us by email at [egoi2023@kodsport.se](mailto:egoi2023@kodsport.se) or at any of the email addresses below:

<table>
{% for item in site.data.organizers %}
<tr>
<td><strong>{{ item.name }}</strong><span class="fl"> - {{ item.title }}</span></td>
<td><a href="mailto:{{ item.email }}">{{ item.email }}</a></td>
</tr>
{% endfor %}
</table>
