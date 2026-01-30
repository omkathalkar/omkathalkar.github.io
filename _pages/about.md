---
layout: about
title: about
permalink: /
subtitle: <a href='https://www.ntua.gr/en/'>National Technical University of Athens (NTUA)</a>

profile:
  align: right
  image: om.jpeg
  image_circular: false
  more_info: #

news: true
teaching: true
selected_papers: true
social: true

featured_media:
  
  - title: "IIITH’s unique research pathway transforms interns into innovators"
    source: "IIITH on Hans India"
    date: "Jan 2026"
    url: "https://www.thehansindia.com/news/cities/hyderabad/iiiths-unique-research-pathway-transforms-interns-into-innovators-1037828"

  - title: "IIITH’s Alternate Admissions GATEway For Postgraduate Researchers"
    source: "IIITH Blogs"
    date: "Jan 2026"
    url: "https://blogs.iiit.ac.in/pg-standingcommittee/"

  - title: "Pallotti Pride: Academic Excellence Highlight"
    source: "SVPCET on LinkedIn"
    date: "Nov 2025"
    url: "https://www.linkedin.com/posts/svpcet_pallottipride-academicexcellence-iiithyderabad-activity-7399380317415043072-DqaQ"
    
  - title: "Om Rajendra Kathalkar – IIIT-H Monthly News"
    source: "IIIT Hyderabad Blog"
    date: "Nov 2025"
    url: "https://blogs.iiit.ac.in/monthly_news/om-rajendra-kathalkar/"

  - title: "Sensor-Free Method Wins Environmental Sensing Competition"
    source: "IIIT Hyderabad Blog"
    date: "Feb 2023"
    url: "https://blogs.iiit.ac.in/aqi/"

  - title: "IoT-based AQI Estimation – Detailed Project Story"
    source: "IIIT Hyderabad Research"
    date: "2022"
    url: "https://mobility.iiit.ac.in/air_quality-blog.php"
    
---

### Om Kathalkar  
**Doctoral Researcher @ National Technical University of Athens (NTUA), Greece**  
**Previously** — Researcher @ Ericsson Research | MS by Research @ IIIT Hyderabad  

📧 **Email me at [omkathalkar.connect@gmail.com](mailto:omkathalkar.connect@gmail.com)**  
· 💼 **[LinkedIn](https://www.linkedin.com/in/om-kathalkar/)**  · 📄 **[Resume](https://drive.google.com/file/d/1G9_sc6aL1YrccvRaF4GdNbe4v1RDtdvo/view)**

---

I am currently a **Doctoral Researcher at the National Technical University of Athens (NTUA), Greece**. My doctoral work is carried out at the **Institute of Communication and Computer Systems (ICCS)** as part of the **Horizon Europe [TURING project](https://turing-project.eu/)** (Trustworthy Unified Robust Intelligent Generative Systems).

My PhD focuses on the **efficient execution of artificial intelligence algorithms**, with a specific emphasis on **efficient AI model inference** in real-world, resource-constrained environments. Broadly, I am interested in **efficient AI and network-aware learning systems**, and in understanding how AI models behave when deployed under constraints imposed by **latency, limited compute, and imperfect wireless connectivity**—particularly in robotics and sensing-driven applications. I am advised by **Konstantinos Tserpes** ([profile](https://scholar.google.com/citations?user=e_-h5egAAAAJ&hl=el)), with an advisory panel comprising **Theodora Varvarigou** ([profile](https://scholar.google.com/citations?user=kueSeb4AAAAJ&hl=en)) and **Georgios Bouloumakis** ([profile](https://gbouloukakis.com/)).

Before starting my PhD, I worked as a **Researcher at Ericsson Research**, contributing to the European **[PANDORA](https://pandora-heu.eu/)** project. My work there focused on **network-aware path planning for autonomous mobile robots (AMRs)**, where I studied the interaction between **AI-based decision-making and wireless network conditions**. This experience shaped my current research perspective, grounding it strongly in **system-aware and deployment-oriented AI**.

Prior to Ericsson, I completed my **MS by Research at [IIIT Hyderabad](https://www.iiit.ac.in/)**, affiliated with the **[Signal Processing and Communication Research Centre (SPCRC)](https://spcrc.iiit.ac.in/)**. I was supervised by **[Prof. Sachin Chaudhari](https://faculty.iiit.ac.in/~sachin.c/)** and **[Prof. Anoop M. Namboodiri](https://faculty.iiit.ac.in/~anoop/)**. My MS research was supported by the **[iHub-Data Fellowship](https://ihub-data.ai/)** and culminated in a successfully defended thesis in **November 2025**, along with peer-reviewed publications.

Alongside research, I remain involved in **education and mentoring**, working with **[TalentSprint (Accenture)](https://talentsprint.com/)** on the **AI Infinity and AI/ML programs**, and contributing to student training initiatives at **iHub-Data, IIIT Hyderabad**.

I completed my **B.E. in Electronics and Telecommunication Engineering** from **[St. Vincent Pallotti College of Engineering and Technology, Nagpur](https://www.stvincentngp.edu.in/)**, where I received multiple academic recognitions, including **AIR-1 (Gold Award) at the e-Yantra Ideas Competition (IIT Bombay)** and **Student of the Year (Engineering, 2023 batch)**.

Outside research, I enjoy reading, playing cricket, hockey, and badminton, hiking, and writing short stories and poetry. I was born and raised in **[Amravati, Maharashtra](https://en.wikipedia.org/wiki/Amravati)**.

---

## Featured Media

Some places where my work has been highlighted.

{% if page.featured_media %}
<div class="row">
  {% for item in page.featured_media %}
  <div class="col-md-4 col-sm-6 mb-4">
    <a href="{{ item.url }}" target="_blank" class="card h-100">
      {% if item.thumbnail %}
      <img src="{{ item.thumbnail }}" class="card-img-top" alt="{{ item.title }} thumbnail">
      {% endif %}
      <div class="card-body">
        <h5 class="card-title">{{ item.title }}</h5>
        <p class="card-text">
          {% if item.source %}{{ item.source }}{% endif %}
          {% if item.date %} · {{ item.date }}{% endif %}
        </p>
      </div>
    </a>
  </div>
  {% endfor %}
</div>
{% endif %}
