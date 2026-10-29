---
title: "AI Literacy Evaluator"
summary: "A web app where a learner writes what they understand about AI, gets it evaluated, and refines it through follow-up questions."
audience: ""
status: "beta"
link_mode: "live"
caveat: "Beta. It runs on my own paid API key, so it may be offline or rate-limited when you visit. It doesn't store anything you enter. It's served over plain HTTP, so your browser may label it \"Not secure.\""
paid_key: true
links:
  live: "http://77.113.225.146:8501/"
  repo: ""
  repo_public_audited: false
downloads: []
request_key: false
screenshots:
  - { src: "/assets/snapshots/ai-literacy-evaluator/01-home.png", alt: "The AI Literacy Evaluator page: a Check Your Understanding box for a statement, an Evaluate button, and a follow-up question panel on the left.", caption: "The start page. You write a statement about AI in your own words." }
  - { src: "/assets/snapshots/ai-literacy-evaluator/02-statement.png", alt: "A sample statement typed into the box: Generative AI predicts likely next words from patterns in its training data, so it can sound confident even when it is wrong.", caption: "A statement ready to evaluate. Screenshots were taken without running an evaluation." }
  - { src: "/assets/snapshots/ai-literacy-evaluator/03-phone.png", alt: "The evaluator on a phone-sized screen, with the same statement box and Evaluate button stacked in one column.", caption: "It also works on a phone." }
tools: ["Streamlit", "AWS"]
division_of_labor: ""
dates: ""
relevant_to: ["Building with AI"]
requirements: [R2]
aied_strands: [ai-literacy, assessment]
why_learning: ""
order: 4
placeholder: false
---

## What I built

A web app for checking understanding of AI. A learner types a statement about what they understand, and the app evaluates it. A follow-up panel lets them ask questions and refine the statement, and a sources panel shows the knowledge base the evaluation draws on.

## How I built it

It runs as a Streamlit app on AWS.
