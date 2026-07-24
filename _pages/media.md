---
layout: page
title: media
permalink: /media/
description: Places where my work has been highlighted.
nav: true
nav_order: 8
---

<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 mt-1">

  {% for item in site.data.featured_media %}
  <div class="col">
    <a href="{{ item.url }}" target="_blank" class="text-decoration-none">
      <div class="card h-100 border-0 shadow-sm">
        <div class="card-body">
          <h6 class="card-title">{{ item.title }}</h6>
          <p class="card-text text-muted small mb-0">
            {% if item.source %}{{ item.source }}{% endif %}
            {% if item.date %} · {{ item.date }}{% endif %}
          </p>
        </div>
      </div>
    </a>
  </div>
  {% endfor %}

</div>
