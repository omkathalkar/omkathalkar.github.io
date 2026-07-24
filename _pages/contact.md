---
layout: page
title: contact
permalink: /contact/
nav: true
nav_order: 9
---

<style>
.contact-wrap {
  max-width: 900px;
  margin: 3rem auto 0;
}

.contact-tag {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--global-theme-color);
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}
.contact-tag::before {
  content: '//';
  opacity: 0.5;
}

.contact-headline {
  font-size: clamp(2rem, 5vw, 3.4rem);
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.02em;
  color: var(--global-text-color);
  margin-bottom: 2rem;
}

.contact-divider {
  height: 1px;
  background: var(--global-divider-color);
  margin: 2rem 0 2.5rem;
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: start;
}

/* ── Left: email + address ── */
.contact-emails {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.contact-email-link {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  font-size: clamp(0.88rem, 1.8vw, 1.1rem);
  font-weight: 600;
  color: var(--global-theme-color);
  text-decoration: none;
  border-bottom: 1.5px solid var(--global-theme-color);
  padding-bottom: 2px;
  transition: opacity 0.15s;
  word-break: break-all;
  width: fit-content;
}
.contact-email-link:hover {
  opacity: 0.75;
  text-decoration: none;
  color: var(--global-theme-color);
}
.contact-email-link svg {
  flex-shrink: 0;
}

.contact-address {
  margin-top: 1.75rem;
  font-size: 0.85rem;
  line-height: 1.8;
  color: var(--global-text-color-light);
  font-family: monospace;
  letter-spacing: 0.02em;
}

/* ── Right: link list ── */
.contact-links {
  list-style: none;
  padding: 0;
  margin: 0;
}
.contact-links li {
  border-top: 1px solid var(--global-divider-color);
}
.contact-links li:last-child {
  border-bottom: 1px solid var(--global-divider-color);
}
.contact-links a {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.1rem 0;
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--global-text-color);
  text-decoration: none;
  transition: color 0.15s, padding-left 0.15s;
}
.contact-links a:hover {
  color: var(--global-theme-color);
  padding-left: 0.4rem;
  text-decoration: none;
}
.contact-links .link-arrow {
  font-size: 0.85rem;
  opacity: 0.5;
  transition: opacity 0.15s, transform 0.15s;
}
.contact-links a:hover .link-arrow {
  opacity: 1;
  transform: translate(2px, -2px);
}

@media (max-width: 640px) {
  .contact-grid {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
}
</style>

<div class="contact-wrap">

  <div class="contact-tag">let's talk</div>

  <h1 class="contact-headline">The best way to<br>reach me is email.</h1>

  <div class="contact-divider"></div>

  <div class="contact-grid">

    <div>
      <div class="contact-emails">
        <a href="mailto:om_kathalkar@mail.ntua.gr" class="contact-email-link">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
          </svg>
          om_kathalkar [at] mail.ntua.gr
        </a>
        <a href="mailto:omkathalkar.connect@gmail.com" class="contact-email-link">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
          </svg>
          omkathalkar.connect [at] gmail.com
        </a>
      </div>

      <div class="contact-address">
        School of Electrical and Computer Engineering<br>
        National Technical University of Athens<br>
        Polytechnic Campus, Zografou<br>
        157 73, Athens, Greece
      </div>
    </div>

    <ul class="contact-links">
      <li>
        <a href="{{ '/assets/pdf/Om_Kathalkar_CV.pdf' | relative_url }}" target="_blank">
          Curriculum Vitae (PDF)
          <span class="link-arrow">↓</span>
        </a>
      </li>
      <li>
        <a href="https://github.com/omkathalkar" target="_blank">
          GitHub — @omkathalkar
          <span class="link-arrow">↗</span>
        </a>
      </li>
      <li>
        <a href="https://www.linkedin.com/in/om-kathalkar/" target="_blank">
          LinkedIn
          <span class="link-arrow">↗</span>
        </a>
      </li>
      <li>
        <a href="https://scholar.google.com/citations?user=a_lzSPoAAAAJ&hl=en" target="_blank">
          Google Scholar
          <span class="link-arrow">↗</span>
        </a>
      </li>
    </ul>

  </div>

</div>
