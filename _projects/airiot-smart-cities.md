---
layout: page
title: Vision-Based Air Quality Estimation for Smart Cities
description: TRAQID dataset and AQIFormer for scalable, sensor-free AQI monitoring
importance: 2
category: work
related_publications: true
---

## Overview

Urban air quality monitoring traditionally depends on dense sensor deployments, which are expensive, sparse, and difficult to maintain.  

This project explored **camera-based AQI estimation** as a scalable alternative, integrating traffic imagery and environmental context to support smart city governance.

The work was conducted at **IIIT Hyderabad (SPCRC Lab)** under the broader initiative on IoT-enabled smart cities.

---

## Problem

- AQI sensors are costly and require maintenance.
- Sparse deployment limits spatial resolution.
- Pollution hotspots are difficult to monitor in real-time.
- Cross-city generalization remains challenging.

We asked:

> Can visual traffic data combined with environmental signals estimate AQI reliably?

---

## TRAQID – Traffic-Related Air Quality Image Dataset

To enable research in vision-based pollution modeling, we created:

**TRAQID**

- 26,678+ traffic-related images
- Co-located AQI and meteorological data
- Multi-condition coverage (day, night, varying traffic density)
- Designed for real-world deployment scenarios

Presented as a **Spotlight Paper at ICVGIP 2024** and among the most downloaded papers of the conference.

---

## AQIFormer – Transformer-Based Multi-View Architecture

We proposed **AQIFormer**, a transformer-based model that integrates:

- Multi-view traffic imagery
- Meteorological inputs
- Context-aware feature fusion

### Key Results

- 90% AQI classification accuracy
- 88% performance during night conditions
- 81.67% cross-city transfer accuracy
- Strong generalization across domains

These results demonstrated that camera-based AQI estimation can serve as a **low-cost, scalable alternative** to sensor-heavy deployments.

---

## Contributions

- Designed end-to-end dataset pipeline (image + AQI + weather integration)
- Proposed multi-view transformer-based architecture
- Conducted cross-city generalization experiments
- Demonstrated robustness across lighting conditions

---

## Impact

- Enables low-cost environmental intelligence
- Supports smart city planning and governance
- Reduces dependency on dense sensor infrastructure
- Bridges Computer Vision and IoT systems

---

## Related Publications

- TRAQID – ICVGIP 2024 (Spotlight)
- AQIFormer – ICVGIP 2024
- Protocol for Hunting PM2.5 Emission Hot Spots – EnvSys 2023
