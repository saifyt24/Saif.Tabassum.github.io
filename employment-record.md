---
layout: default
title: Employment Record
description: Details of my professional experience, short-term jobs, and volunteer work.
permalink: /employment-record/
---

<section class="page-heading">
  <p class="eyebrow">Career history</p>
  <h1>Employment Record</h1>
  <p class="lead">
    A record of my professional experience, temporary positions,
    responsibilities, achievements, and volunteer contributions.
  </p>
</section>

{% assign jobs = site.employment | sort: "start_date" | reverse %}
{% assign long_term_jobs = jobs | where: "record_category", "Long-term Employment" %}
{% assign short_term_jobs = jobs | where: "record_category", "Short-term Employment" %}
{% assign volunteer_jobs = jobs | where: "record_category", "Volunteering" %}

{% assign long_term_count = long_term_jobs | size %}
{% assign short_term_count = short_term_jobs | size %}
{% assign volunteer_count = volunteer_jobs | size %}
{% assign total_jobs = jobs | size %}

{% if long_term_count > 0 %}
<section class="section">
  <h2>Long-term Employment</h2>
  <p class="muted">Ongoing and longer-term professional positions.</p>

  <div class="card-grid">
    {% for job in long_term_jobs %}
      {% include employment-record-card.html job=job %}
    {% endfor %}
  </div>
</section>
{% endif %}

{% if short_term_count > 0 %}
<section class="section">
  <h2>Short-term Employment</h2>
  <p class="muted">Temporary, contract, seasonal, and brief positions.</p>

  <div class="card-grid">
    {% for job in short_term_jobs %}
      {% include employment-record-card.html job=job %}
    {% endfor %}
  </div>
</section>
{% endif %}

{% if volunteer_count > 0 %}
<section class="section">
  <h2>Volunteering</h2>
  <p class="muted">Volunteer roles and community contributions.</p>

  <div class="card-grid">
    {% for job in volunteer_jobs %}
      {% include employment-record-card.html job=job %}
    {% endfor %}
  </div>
</section>
{% endif %}

{% if total_jobs == 0 %}
<section class="section">
  <p class="muted">
    Employment history and volunteer experience will appear here as entries are added.
  </p>
</section>
{% endif %}

{% assign uncategorized_jobs = jobs | where_exp: "job", "job.record_category == nil or job.record_category == ''" %}
{% assign uncategorized_count = uncategorized_jobs | size %}

{% if uncategorized_count > 0 %}
<section class="section">
  <h2>Other Records</h2>
  <p class="muted">
    These entries need a category assigned in Pages CMS.
  </p>

  <div class="card-grid">
    {% for job in uncategorized_jobs %}
      {% include employment-record-card.html job=job %}
    {% endfor %}
  </div>
</section>
{% endif %}
