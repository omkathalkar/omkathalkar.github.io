---
layout: page
title: media
permalink: /media/
description: Places where my work has been highlighted.
nav: true
nav_order: 8
---

<style>
.media-card {
  display: block;
  text-decoration: none;
  border-radius: 12px;
  border: 1px solid rgba(128,128,128,0.2);
  padding: 1.25rem 1.5rem;
  height: 100%;
  transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
  background: var(--global-card-bg-color, #fff);
}
.media-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.12);
  border-color: var(--global-theme-color, #0076df);
  text-decoration: none;
}
.media-card .media-title {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--global-text-color);
  margin-bottom: 0.5rem;
  line-height: 1.4;
}
.media-card .media-meta {
  font-size: 0.8rem;
  color: var(--global-text-color-light, #6c757d);
  display: flex;
  align-items: center;
  gap: 0.3rem;
}
.media-card .media-icon {
  font-size: 0.7rem;
  opacity: 0.5;
  float: right;
  margin-top: 2px;
}
.media-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1.25rem;
  margin-top: 1.5rem;
}
</style>

<div class="media-grid">
  {% for item in site.data.featured_media %}
  <a href="{{ item.url }}" target="_blank" class="media-card">
    <span class="media-icon">↗</span>
    <div class="media-title">{{ item.title }}</div>
    <div class="media-meta">
      {% if item.source %}<span>{{ item.source }}</span>{% endif %}
      {% if item.date %}<span>·</span><span>{{ item.date }}</span>{% endif %}
    </div>
  </a>
  {% endfor %}
</div>
