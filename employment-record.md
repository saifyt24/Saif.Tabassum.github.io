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
  {% assign category_jobs = jobs | where: "record_category", category %}
  {% assign category_count = category_jobs | size %}

  {% if category_count > 0 %}
    <section class="section">
      <h2>{{ category }}</h2>

      {% if category == "Long-term Employment" %}
        <p class="muted">Ongoing and longer-term professional positions.</p>
      {% elsif category == "Short-term Employment" %}
        <p class="muted">Temporary, contract, seasonal, and brief positions.</p>
      {% else %}
        <p class="muted">Volunteer roles and community contributions.</p>
      {% endif %}

      <div class="card-grid">
        {% for job in category_jobs %}
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
                    Organization website ↗
                  </a>
                </p>
              {% endif %}

              {% if job.supporting_document %}
                <p>
                  <a href="{{ job.supporting_document | relative_url }}"
                     target="_blank"
                     rel="noopener noreferrer">
                    View supporting document (PDF) ↗
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
      </div>
    </section>
  {% endif %}
{% endfor %}

{% assign uncategorized_jobs = "" | split: "," %}

{% for job in jobs %}
  {% unless job.record_category == "Long-term Employment" or job.record_category == "Short-term Employment" or job.record_category == "Volunteering" %}
    {% assign uncategorized_jobs = uncategorized_jobs | push: job %}
  {% endunless %}
{% endfor %}

{% assign uncategorized_count = uncategorized_jobs | size %}

{% if uncategorized_count > 0 %}
  <section class="section">
    <h2>Other Records</h2>
    <p class="muted">
      These entries need a category assigned in Pages CMS.
    </p>

    <div class="card-grid">
      {% for job in uncategorized_jobs %}
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
                  Organization website ↗
                </a>
              </p>
            {% endif %}

            {% if job.supporting_document %}
              <p>
                <a href="{{ job.supporting_document | relative_url }}"
                   target="_blank"
                   rel="noopener noreferrer">
                  View supporting document (PDF) ↗
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
    </div>
  </section>
{% endif %}

{% assign total_jobs = jobs | size %}

{% if total_jobs == 0 %}
  <section class="section">
    <p class="muted">
      Employment history and volunteer experience will appear here as entries are added.
    </p>
  </section>
{% endif %}
