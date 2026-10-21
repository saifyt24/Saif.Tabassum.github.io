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

{% assign categories = "Long-term Employment|Short-term Employment|Volunteering" | split: "|" %}

{% for category in categories %}
  <section class="section">
    <h2>{{ category }}</h2>

    <div class="card-grid">
      {% for job in jobs %}
        {% if job.record_category == category %}
          <article class="card">
            <div class="card-content">
              <p class="eyebrow">
                {{ job.start_date | date: "%b %Y" }} –
                {% if job.current %}
                  Present
                {% elsif job.end_date %}
                  {{ job.end_date | date: "%b %Y" }}
                {% else %}
                  End date not provided
                {% endif %}
              </p>

              <h3>{{ job.job_title | escape }}</h3>
              <p><strong>{{ job.company | escape }}</strong></p>

              {% if job.location %}
                <p class="muted">{{ job.location | escape }}</p>
              {% endif %}

              {% if job.employment_type %}
                <p class="muted">{{ job.employment_type | escape }}</p>
              {% endif %}

              {% if job.description %}
                <p>{{ job.description | escape }}</p>
              {% endif %}

              {% if job.responsibilities %}
                <h4>Responsibilities and achievements</h4>
                <ul>
                  {% for item in job.responsibilities %}
                    <li>{{ item | escape }}</li>
                  {% endfor %}
                </ul>
              {% endif %}

              {% if job.reason_for_leaving %}
                <p><strong>Reason for leaving:</strong>
                  {{ job.reason_for_leaving | escape }}
                </p>
              {% endif %}

              {% if job.company_website %}
                <p>
                  <a href="{{ job.company_website | escape }}" target="_blank" rel="noopener noreferrer">
                    Organization website ↗
                  </a>
                </p>
              {% endif %}

              {% if job.supporting_document %}
                <p>
                  <a href="{{ job.supporting_document | relative_url }}" target="_blank" rel="noopener noreferrer">
                    View supporting document (PDF) ↗
                  </a>
                </p>
              {% endif %}
            </div>
          </article>
        {% endif %}
      {% endfor %}
    </div>
  </section>
{% endfor %}
