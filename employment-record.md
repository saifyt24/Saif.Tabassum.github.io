---
layout: default
title: Employment Record
description: Details of my professional experience and employment history.
permalink: /employment-record/
---

<section class="page-heading">
  <p class="eyebrow">Career history</p>
  <h1>Employment Record</h1>
  <p class="lead">
    Details of my professional experience, responsibilities,
    and employment history.
  </p>
</section>

<section class="section">
  <div class="card-grid">
    {% assign jobs = site.employment | sort: "start_date" | reverse %}
    {% assign visible_jobs = 0 %}

    {% for job in jobs %}
      {% assign visible_jobs = visible_jobs | plus: 1 %}
      <article class="card">
        <div class="card-content">
          <p class="eyebrow">
            {% if job.start_date %}
              {{ job.start_date | date: "%b %Y" }}
            {% endif %}
            –
            {% if job.current %}
              Present
            {% elsif job.end_date %}
              {{ job.end_date | date: "%b %Y" }}
            {% else %}
              End date not provided
            {% endif %}
          </p>

          <h2>{{ job.job_title | escape }}</h2>
          <p><strong>{{ job.company | escape }}</strong></p>

          {% if job.location %}
            <p class="muted">{{ job.location | escape }}</p>
          {% endif %}

          {% if job.employment_type %}
            <p class="muted">{{ job.employment_type | escape }}</p>
          {% endif %}

          {% if job.description %}
            <p class="card-description">
              {{ job.description | escape }}
            </p>
          {% endif %}

          {% if job.responsibilities %}
            <h3>Responsibilities and achievements</h3>
            <ul>
              {% for item in job.responsibilities %}
                <li>{{ item | escape }}</li>
              {% endfor %}
            </ul>
          {% endif %}

          {% if job.reason_for_leaving %}
            <div class="employment-reason">
              <h3>Reason for Leaving</h3>
              <p>{{ job.reason_for_leaving | escape }}</p>
            </div>
          {% endif %}

          {% if job.company_website %}
            <p>
              <a href="{{ job.company_website | escape }}"
                 target="_blank"
                 rel="noopener noreferrer">
                Company website ↗
              </a>
            </p>
          {% endif %}

          {% if job.body %}
            <div class="content">
              {{ job.body }}
            </div>
          {% endif %}
        </div>
      </article>
    {% endfor %}

    {% if visible_jobs == 0 %}
      <p class="muted">
        Employment history will appear here as entries are added.
      </p>
    {% endif %}
  </div>
</section>
