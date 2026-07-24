---
layout: page
title: cv
permalink: /resume/
nav: true
nav_order: 5
---

<style>
/* ── Layout ── */
.cv-wrap { max-width: 860px; margin: 0 auto; padding: 0 1rem 4rem; }

/* ── Download button ── */
.cv-download {
  display: inline-flex; align-items: center; gap: 0.45rem;
  padding: 0.55rem 1.3rem; border-radius: 8px; font-size: 0.875rem; font-weight: 600;
  background: var(--global-theme-color); color: #fff; text-decoration: none;
  transition: opacity 0.15s ease;
}
.cv-download:hover { opacity: 0.85; color: #fff; text-decoration: none; }

/* ── Section headings ── */
.cv-section { margin-top: 2.8rem; }
.cv-section-title {
  font-size: 0.7rem; font-weight: 700; letter-spacing: 0.12em;
  text-transform: uppercase; color: var(--global-theme-color);
  border-bottom: 2px solid var(--global-theme-color);
  padding-bottom: 0.3rem; margin-bottom: 1.4rem;
}

/* ── Timeline ── */
.cv-timeline { position: relative; padding-left: 1.5rem; }
.cv-timeline::before {
  content: ""; position: absolute; left: 0; top: 6px; bottom: 0;
  width: 2px; background: rgba(128,128,128,0.18); border-radius: 2px;
}
.cv-entry { position: relative; margin-bottom: 2rem; }
.cv-entry::before {
  content: ""; position: absolute; left: -1.84rem; top: 6px;
  width: 10px; height: 10px; border-radius: 50%;
  background: var(--global-theme-color); border: 2px solid var(--global-bg-color, #fff);
  box-shadow: 0 0 0 2px var(--global-theme-color);
}
.cv-entry-header { display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.3rem; }
.cv-entry-title { font-size: 1rem; font-weight: 700; color: var(--global-text-color); margin: 0; }
.cv-entry-date {
  font-size: 0.78rem; font-weight: 600; color: var(--global-theme-color);
  background: rgba(var(--global-theme-color-rgb, 0,118,223), 0.08);
  padding: 0.15rem 0.55rem; border-radius: 20px; white-space: nowrap;
}
.cv-entry-org { font-size: 0.88rem; color: var(--global-text-color-light, #6c757d); margin: 0.2rem 0 0.5rem; }
.cv-entry-tag {
  display: inline-block; font-size: 0.72rem; font-weight: 600;
  padding: 0.1rem 0.5rem; border-radius: 4px; margin-right: 0.3rem; margin-bottom: 0.3rem;
  background: rgba(128,128,128,0.12); color: var(--global-text-color-light, #6c757d);
}
.cv-entry ul { margin: 0.4rem 0 0 0; padding-left: 1.1rem; }
.cv-entry ul li { font-size: 0.88rem; color: var(--global-text-color); margin-bottom: 0.25rem; }

/* ── Education cards ── */
.edu-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 1rem; }
.edu-card {
  border: 1px solid rgba(128,128,128,0.18); border-radius: 12px;
  padding: 1.1rem 1.25rem; background: var(--global-card-bg-color, #fff);
}
.edu-degree { font-size: 0.92rem; font-weight: 700; color: var(--global-text-color); margin-bottom: 0.2rem; }
.edu-inst { font-size: 0.82rem; color: var(--global-text-color-light, #6c757d); margin-bottom: 0.4rem; }
.edu-year { font-size: 0.75rem; font-weight: 600; color: var(--global-theme-color); }
.edu-note { font-size: 0.78rem; color: var(--global-text-color-light, #6c757d); margin-top: 0.4rem; }

/* ── Skills ── */
.skill-group { margin-bottom: 0.9rem; }
.skill-label { font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--global-text-color-light, #6c757d); margin-bottom: 0.4rem; }
.skill-badge {
  display: inline-block; font-size: 0.8rem; padding: 0.25rem 0.7rem;
  border-radius: 20px; margin: 0.2rem 0.25rem 0.2rem 0;
  border: 1px solid rgba(128,128,128,0.22);
  background: var(--global-card-bg-color, #fff); color: var(--global-text-color);
}

/* ── Publications ── */
.pub-entry { margin-bottom: 1.1rem; padding-bottom: 1.1rem; border-bottom: 1px solid rgba(128,128,128,0.12); }
.pub-entry:last-child { border-bottom: none; }
.pub-badge {
  display: inline-block; font-size: 0.68rem; font-weight: 700; padding: 0.1rem 0.5rem;
  border-radius: 4px; margin-right: 0.4rem; vertical-align: middle;
  background: var(--global-theme-color); color: #fff;
}
.pub-title { font-size: 0.88rem; font-weight: 600; color: var(--global-text-color); }
.pub-meta { font-size: 0.8rem; color: var(--global-text-color-light, #6c757d); margin-top: 0.15rem; }
.pub-venue { font-style: italic; }

/* ── Awards ── */
.award-entry { display: flex; gap: 1rem; align-items: flex-start; margin-bottom: 0.9rem; }
.award-num {
  min-width: 28px; height: 28px; border-radius: 50%; font-size: 0.75rem; font-weight: 700;
  background: var(--global-theme-color); color: #fff;
  display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 1px;
}
.award-text { font-size: 0.88rem; color: var(--global-text-color); }
.award-text strong { color: var(--global-text-color); }

/* ── Projects ── */
.proj-entry { margin-bottom: 1.2rem; }
.proj-header { display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.3rem; }
.proj-name { font-size: 0.92rem; font-weight: 700; color: var(--global-text-color); }
.proj-year { font-size: 0.78rem; color: var(--global-text-color-light, #6c757d); }
.proj-fund { font-size: 0.78rem; color: var(--global-theme-color); margin-bottom: 0.3rem; }
.proj-desc { font-size: 0.85rem; color: var(--global-text-color); }
</style>

<div class="cv-wrap">

<!-- Header -->
<div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem; margin-bottom:0.5rem;">
  <div>
    <h2 style="margin:0; font-size:1.6rem; font-weight:800;">Om Rajendra Kathalkar</h2>
    <p style="margin:0.3rem 0 0; font-size:0.88rem; color:var(--global-text-color-light, #6c757d);">
      Doctoral Researcher · National Technical University of Athens, Greece
    </p>
  </div>
  <a href="{{ '/assets/pdf/Om_Kathalkar_CV.pdf' | relative_url }}" target="_blank" class="cv-download">
    ↓ Download CV
  </a>
</div>

<!-- ── EDUCATION ── -->
<div class="cv-section">
  <div class="cv-section-title">Education</div>
  <div class="edu-grid">

    <div class="edu-card">
      <div class="edu-degree">PhD in Computer Science</div>
      <div class="edu-inst">National Technical University of Athens (NTUA), Greece</div>
      <div class="edu-year">2025 – Present</div>
      <div class="edu-note">Horizon Europe TURING Project · Advisor: Dr. Konstantinos Tserpes</div>
    </div>

    <div class="edu-card">
      <div class="edu-degree">MS by Research — ECE</div>
      <div class="edu-inst">IIIT Hyderabad, India</div>
      <div class="edu-year">2021 – 2025</div>
      <div class="edu-note">iHub-Data Fellow · Advisor: Dr. Sachin Chaudhari · Defended Nov 2025</div>
    </div>

    <div class="edu-card">
      <div class="edu-degree">BE — Electronics &amp; Telecom</div>
      <div class="edu-inst">St. Vincent Pallotti College (SVPCET), Nagpur</div>
      <div class="edu-year">2019 – 2023</div>
      <div class="edu-note">CGPA 8.83/10 · Student of the Year 2023</div>
    </div>

  </div>
</div>

<!-- ── RESEARCH EXPERIENCE ── -->
<div class="cv-section">
  <div class="cv-section-title">Research Experience</div>
  <div class="cv-timeline">

    <div class="cv-entry">
      <div class="cv-entry-header">
        <div class="cv-entry-title">Research Associate</div>
        <div class="cv-entry-date">Jan 2026 – Present</div>
      </div>
      <div class="cv-entry-org">Institute of Communication and Computer Systems (ICCS), NTUA, Greece</div>
      <span class="cv-entry-tag">Horizon Europe · TURING</span>
      <ul>
        <li>Research on <strong>efficient and autonomous execution of AI models</strong>, focusing on edge inference and scalable AI systems.</li>
        <li>Contributing to AI-driven optimization pipelines for real-world deployment under the TURING project.</li>
        <li>Collaborating with interdisciplinary teams across academia and industry.</li>
      </ul>
    </div>

    <div class="cv-entry">
      <div class="cv-entry-header">
        <div class="cv-entry-title">Applied AI Researcher</div>
        <div class="cv-entry-date">Dec 2024 – Dec 2025</div>
      </div>
      <div class="cv-entry-org">Ericsson Research, Bangalore</div>
      <span class="cv-entry-tag">Horizon Europe · PANDORA</span>
      <ul>
        <li>Developed <strong>network-aware path planning</strong> algorithms for Autonomous Mobile Robots (AMRs).</li>
        <li>Combined real-time decision-making and semantic understanding for reliable industrial navigation.</li>
        <li>Published at IEEE ANTS 2025 and Springer Nature Autonomous Robots (under review).</li>
      </ul>
    </div>

    <div class="cv-entry">
      <div class="cv-entry-header">
        <div class="cv-entry-title">Research Scholar</div>
        <div class="cv-entry-date">Aug 2021 – Oct 2025</div>
      </div>
      <div class="cv-entry-org">Signal Processing and Communications Research Centre (SPCRC), IIIT Hyderabad</div>
      <span class="cv-entry-tag">iHub-Data Fellowship</span>
      <ul>
        <li>Built <strong>TRAQID</strong> — 26,678+ traffic images with co-located AQI and weather data; Spotlight paper at ICVGIP 2024.</li>
        <li>Proposed <strong>AQIFormer</strong>, a transformer-based multi-view model achieving 90% AQI accuracy and 81.67% cross-city transfer.</li>
        <li>Developed sensor-free AQI estimation framework reducing dependency on costly sensor networks.</li>
      </ul>
    </div>

  </div>
</div>

<!-- ── TEACHING EXPERIENCE ── -->
<div class="cv-section">
  <div class="cv-section-title">Teaching Experience</div>
  <div class="cv-timeline">

    <div class="cv-entry">
      <div class="cv-entry-header">
        <div class="cv-entry-title">Gen AI-ML Instructor</div>
        <div class="cv-entry-date">Apr 2024 – Present</div>
      </div>
      <div class="cv-entry-org">TalentSprint (Part of Accenture)</div>
      <ul>
        <li>Guiding ML, DL, and NLP to industry professionals via programs from IIIT-H, IISc Bangalore, and University of Michigan.</li>
        <li>Mentored <strong>250+ professionals</strong> with 15+ years of industry experience on Agentic AI and Generative AI.</li>
      </ul>
    </div>

    <div class="cv-entry">
      <div class="cv-entry-header">
        <div class="cv-entry-title">AI Instructor</div>
        <div class="cv-entry-date">Apr 2025 – Jan 2026</div>
      </div>
      <div class="cv-entry-org">iHub-Data, IIIT Hyderabad</div>
      <ul>
        <li>Delivered 24-week AI/ML training covering classification, regression, clustering, PCA, neural networks.</li>
        <li>Facilitated hands-on tutorials for <strong>50+ engineering students</strong>.</li>
      </ul>
    </div>

    <div class="cv-entry">
      <div class="cv-entry-header">
        <div class="cv-entry-title">Workshop Instructor</div>
        <div class="cv-entry-date">2022 – 2024</div>
      </div>
      <div class="cv-entry-org">IIIT Hyderabad &amp; KEIT</div>
      <ul>
        <li>Embedded Systems Workshop — Monsoon 2024</li>
        <li>ML for IoT Workshop — Monsoon 2023</li>
        <li>Machine Learning, KEIT — Spring 2022</li>
      </ul>
    </div>

  </div>
</div>

<!-- ── PUBLICATIONS ── -->
<div class="cv-section">
  <div class="cv-section-title">Publications</div>

  <div class="pub-entry">
    <span class="pub-badge">Journal</span>
    <span class="pub-title">Network-aware path planning for AMRs: A generalizable framework with spatial-aware adaptation</span>
    <div class="pub-meta">Om Kathalkar, H. H. Hassan, A. Kattepur, G. Bouloukakis · <span class="pub-venue">Autonomous Robots, Springer Nature</span> · under review</div>
  </div>

  <div class="pub-entry">
    <span class="pub-badge">C4</span>
    <span class="pub-title">Network-Aware Path Planning for Autonomous Mobile Robots in Industrial Environments</span>
    <div class="pub-meta">Om Kathalkar, H. H. Hassan, A. Kattepur, G. Bouloukakis · <span class="pub-venue">IEEE ANTS 2025, Delhi</span> · Acceptance rate: 32.8%</div>
  </div>

  <div class="pub-entry">
    <span class="pub-badge">C3</span>
    <span class="pub-title">AQIFormer: A Transformer-Based Multi-View Architecture for Cross-City Air Quality Classification</span>
    <div class="pub-meta">Om Kathalkar, N. Nilesh, S. Chaudhari, A. Namboodiri · <span class="pub-venue">ICVGIP 2025, Mandi</span></div>
  </div>

  <div class="pub-entry">
    <span class="pub-badge">C2 ★</span>
    <span class="pub-title">TRAQID – Traffic-Related Air Quality Image Dataset</span>
    <div class="pub-meta">Om Kathalkar, N. Nilesh, S. Chaudhari, A. Namboodiri · <span class="pub-venue">ICVGIP 2024, Bangalore</span> · <strong>Spotlight Presentation</strong></div>
  </div>

  <div class="pub-entry">
    <span class="pub-badge">C1</span>
    <span class="pub-title">Protocol for Hunting PM2.5 Emission Hot Spots in Cities</span>
    <div class="pub-meta">S. Sara, A. Rebeiro-Hargrave, Om Kathalkar, S. Chaudhari · <span class="pub-venue">EnvSys 2023, Helsinki</span></div>
  </div>

  <div class="pub-entry">
    <span class="pub-badge">P3</span>
    <span class="pub-title">System for Determining AQI in Urban Environments · Indian Patent 202541073518</span>
    <div class="pub-meta">Om Kathalkar, A. Shah, S. Chaudhari, A. Namboodiri · Filed May 2025</div>
  </div>

  <div class="pub-entry">
    <span class="pub-badge">P2</span>
    <span class="pub-title">System and Method for Determining Air Quality by Processing Environmental and Traffic-Related Visual Data · 202441043706</span>
    <div class="pub-meta">Om Kathalkar, N. Nilesh, S. Chaudhari, A. Namboodiri · Indian Patent Published, May 2024</div>
  </div>

  <div class="pub-entry">
    <span class="pub-badge">P1</span>
    <span class="pub-title">System and Method for Implementing an Experiment Remotely Using a Computer Vision Model · US20240078641A1</span>
    <div class="pub-meta">S. Chaudhari, Om Kathalkar, V. S. Kandala, N. Nilesh · US Patent Published, Mar 2023</div>
  </div>

</div>

<!-- ── RESEARCH PROJECTS ── -->
<div class="cv-section">
  <div class="cv-section-title">Research Projects</div>

  <div class="proj-entry">
    <div class="proj-header">
      <div class="proj-name">TURING — Horizon Europe Project</div>
      <div class="proj-year">2026 – Present</div>
    </div>
    <div class="proj-fund">Horizon Europe · NTUA / ICCS, Greece</div>
    <div class="proj-desc">Efficient and autonomous execution of AI algorithms — scalable inference, trustworthy AI, and deployable AI pipelines for real-world industrial systems.</div>
  </div>

  <div class="proj-entry">
    <div class="proj-header">
      <div class="proj-name">PANDORA — Horizon Europe Project</div>
      <div class="proj-year">2024 – 2025</div>
    </div>
    <div class="proj-fund">Horizon Europe · Ericsson Research, Bangalore</div>
    <div class="proj-desc">Network-aware and trustworthy AI for AMRs — robust path planning, communication-aware decision-making, and reliable operation in industrial environments.</div>
  </div>

  <div class="proj-entry">
    <div class="proj-header">
      <div class="proj-name">IoT-Enabled Smart Cities: Pollution, Health &amp; Governance</div>
      <div class="proj-year">2019 – 2023</div>
    </div>
    <div class="proj-fund">PRIF &amp; Department of Science and Technology, India · IIIT Hyderabad</div>
    <div class="proj-desc">Image-based AQI monitoring integrating traffic visuals and environmental cues for scalable, low-cost smart city governance.</div>
  </div>

  <div class="proj-entry">
    <div class="proj-header">
      <div class="proj-name">Remote Labs Platform</div>
      <div class="proj-year">2021 – 2022</div>
    </div>
    <div class="proj-fund">PRIF &amp; Department of Science and Technology, India · IIIT Hyderabad</div>
    <div class="proj-desc">Large-scale remote laboratory platform to democratize STEM education for thousands of rural and underrepresented students across India.</div>
  </div>

</div>

<!-- ── SKILLS ── -->
<div class="cv-section">
  <div class="cv-section-title">Skills</div>

  <div class="skill-group">
    <div class="skill-label">Areas of Interest</div>
    <span class="skill-badge">Machine &amp; Deep Learning</span>
    <span class="skill-badge">Edge AI</span>
    <span class="skill-badge">Internet of Things</span>
    <span class="skill-badge">NLP</span>
    <span class="skill-badge">Agentic &amp; Gen AI</span>
    <span class="skill-badge">Efficient Inference</span>
  </div>

  <div class="skill-group">
    <div class="skill-label">Tools &amp; Frameworks</div>
    <span class="skill-badge">PyTorch</span>
    <span class="skill-badge">TensorFlow</span>
    <span class="skill-badge">CUDA</span>
    <span class="skill-badge">Nvidia Sionna</span>
    <span class="skill-badge">Scikit-learn</span>
    <span class="skill-badge">Django</span>
    <span class="skill-badge">LaTeX</span>
    <span class="skill-badge">N8N</span>
  </div>

  <div class="skill-group">
    <div class="skill-label">Hardware</div>
    <span class="skill-badge">Jetson Xavier NX</span>
    <span class="skill-badge">Raspberry Pi</span>
    <span class="skill-badge">Arduino</span>
    <span class="skill-badge">ESP Series</span>
  </div>

</div>

<!-- ── AWARDS ── -->
<div class="cv-section">
  <div class="cv-section-title">Awards &amp; Honors</div>

  <div class="award-entry">
    <div class="award-num">1</div>
    <div class="award-text"><strong>iHub-Data Research Fellowship</strong> (Aug 2023) — MS by Research at IIIT Hyderabad; fully covered research funding and tuition based on academic merit.</div>
  </div>
  <div class="award-entry">
    <div class="award-num">2</div>
    <div class="award-text"><strong>Winner — International Environmental Sensing Project Competition</strong> (Mar 2023), University of Helsinki, Finland; top position among teams from multiple countries.</div>
  </div>
  <div class="award-entry">
    <div class="award-num">3</div>
    <div class="award-text"><strong>AIR-1 Gold Award — e-Yantra Ideas Competition</strong>, IIT Bombay; national-level competition featuring 100+ top engineering college teams across India.</div>
  </div>
  <div class="award-entry">
    <div class="award-num">4</div>
    <div class="award-text"><strong>Student of the Year</strong> (May 2023) among 1000+ undergraduates at SVPCET, Nagpur, for outstanding academic performance, leadership, and overall contributions.</div>
  </div>
  <div class="award-entry">
    <div class="award-num">5</div>
    <div class="award-text"><strong>Best Project Award</strong> (Dec 2022) for an innovative and technically rigorous undergraduate final-year project.</div>
  </div>
  <div class="award-entry">
    <div class="award-num">6</div>
    <div class="award-text"><strong>Student of the Department (ETC)</strong>, SVPCET, Nagpur — consistent research contributions, academic excellence, and departmental engagement.</div>
  </div>

</div>

</div>
