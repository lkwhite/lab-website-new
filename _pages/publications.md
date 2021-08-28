---
layout: page
permalink: /publications/
title: publications
description: > 
    publications by categories in reversed chronological order
    with pre-prints at the top.
years: [preprint, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2010, 2009, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999]
nav: true
---

<div class="publications">

{% for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>

