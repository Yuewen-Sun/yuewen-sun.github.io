---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}


<span class='anchor' id='about-me'></span>

{% include_relative includes/1-intro.md %}

{% include_relative includes/2-news.md %}

{% include_relative includes/3-pub.md %}

{% include_relative includes/4-experience.md %}

{% include_relative includes/5-service.md %}

{% include_relative includes/6-talks.md %}

{% include_relative includes/7-honors.md %}










