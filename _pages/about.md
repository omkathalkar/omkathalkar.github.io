---
layout: about
title: about
permalink: /
subtitle: <a href='https://www.iiit.ac.in/'>IIIT Hyderabad</a> & <a href='https://www.ericsson.com/en/reports-and-papers/research-papers?locs=68304,46951'>Ericsson Research</a>.

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
  - title: "Pallotti Pride: Academic Excellence Highlight"
    source: "SVPCET on LinkedIn"
    date: "Nov 2025"
    url: "https://www.linkedin.com/posts/svpcet_pallottipride-academicexcellence-iiithyderabad-activity-7399380317415043072-DqaQ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC0VN4YBQvS18pO1WK9FhGAaxhBbffT3vzs"
    thumbnail: "/assets/img/featured/pallotti-linkedin.jpg"

  - title: "Om Rajendra Kathalkar – IIIT-H Monthly News"
    source: "IIIT Hyderabad Blog"
    date: "Nov 2025"
    url: "https://blogs.iiit.ac.in/monthly_news/om-rajendra-kathalkar/"
    thumbnail: "/assets/img/featured/iiit-ms.jpg"

  - title: "Sensor-Free Method Wins Environmental Sensing Competition"
    source: "IIIT Hyderabad Blog"
    date: "Feb 2023"
    url: "https://blogs.iiit.ac.in/aqi/"
    thumbnail: "/assets/img/featured/Team-Vayu.jpg"

  - title: "IoT-based AQI Estimation – Detailed Project Story"
    source: "IIIT Hyderabad Research"
    date: "2022"
    url: "https://mobility.iiit.ac.in/air_quality-blog.php"
    thumbnail: "/assets/img/featured/air_quality.png"
---  

👋 Hi, I am an MS by Research student at IIIT Hyderabad and a Research Scholar at the [Signal Processing and Communication Research Centre (SPCRC)](https://spcrc.iiit.ac.in/), supervised by [Prof. Sachin Chaudhari](https://faculty.iiit.ac.in/~sachin.c/) (SPCRC, IIIT Hyderabad) and [Prof. Anoop M. Namboodiri](https://faculty.iiit.ac.in/~anoop/) ([CVIT](https://cvit.iiit.ac.in/), IIIT Hyderabad). Please find my resume **[here](https://drive.google.com/file/d/1G9_sc6aL1YrccvRaF4GdNbe4v1RDtdvo/view?usp=sharing)**. My research focuses on developing **efficient and adaptive AI systems** that can operate reliably in **resource-constrained and real-world environments**, with applications spanning **environmental sensing, smart cities, and robotics**. My [publications](https://omkathalkar.github.io/publications/) reflect these contributions, and I have been awarded the [iHub-Data Fellowship](https://ihub-data.ai/archives/blogs/5998/) for my MS research.  

I am currently a **Researcher at Ericsson Research**, contributing to the European [PANDORA project](https://pandora-heu.eu/). My work centers on **network-aware path planning for autonomous mobile robots (AMRs)**, where I design algorithms that integrate **AI inference with wireless network dynamics**. By combining **edge intelligence and adaptive decision-making**, my research aims to ensure reliable robot navigation in dynamic industrial environments, even under constrained connectivity.  


I completed my B.E. in Electronics and Telecommunication at [St. Vincent Pallotti College of Engineering and Technology, Nagpur](https://www.stvincentngp.edu.in/) (SVPCET), with the guidance of [Dr. Shriraghavan R. Madbushi](https://www.stvincentngp.edu.in/faculties/view/34). At SVPCET, I achieved AIR-1 in the Gold Award at the e-Yantra Ideas Competition organized by IIT Bombay, received the **Student of the Year award** for the engineering 2023 batch and for the Electronics and Telecommunication Department, and secured the Best Project Award for my final-year project.

In my free time, I enjoy reading, playing cricket, hockey, and badminton, hiking, and writing short stories and poetry. I was born and raised in [Amravati, Maharashtra](https://en.wikipedia.org/wiki/Amravati), one of India’s oldest continuously inhabited cities.

### Research 

My research interests encompass various domains, including Edge AI, Internet of Things, Computer Vision, Machine & Deep Learning, and Environmental Sensing.


### Teaching

I am passionate about education and mentoring. At [NSE TalentSprint](https://talentsprint.com/?srsltid=AfmBOoruCeg3vOWrY0fkSuGi06p49esrpKXLBN8X7ubhhi0VJYEteYo8), I mentor the [AIML certification program](https://talentsprint.com/course/ai-machine-learning-iiit-hyderabad), transforming industry professionals into ML practitioners through intensive training in neural architectures, NLP, and computer vision. I guide teams from concept to deployment, helping professionals implement production-ready AI solutions. At IIIT Hyderabad's IoT & Embedded Workshop Lab, I pioneer the implementation of ML models on [Qualcomm's QIDK platform](https://www.qualcomm.com/developer/hardware/qualcomm-innovators-development-kit), where I teach undergrad and postgrad students to break through edge computing barriers. Students learn to optimize ML models for mobile platforms, focusing on real-time inference and efficient resource utilization on Snapdragon SoCs. Beyond urban centres, I've reached 200+ students in rural engineering colleges, introducing them to ML and IoT fundamentals.

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
