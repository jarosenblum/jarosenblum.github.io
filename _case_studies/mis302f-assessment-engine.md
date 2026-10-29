---
title: "MIS 302F exam pipeline"
summary: "A pipeline that turns my lecture transcripts into an exam blueprint, draft questions, audits, and a Canvas-ready export, with me approving each stage."
audience: "Built for my MIS 302F exams"
status: "in use"
link_mode: "excerpt"
caveat: ""
paid_key: false
links:
  live: ""
  repo: ""
  repo_public_audited: false
downloads: []
request_key: false
screenshots:
  - { src: "", alt: "", caption: "" }
  - { src: "", alt: "", caption: "" }
  - { src: "", alt: "", caption: "" }
tools: ["Claude Cowork", "Claude Code", "Python"]
division_of_labor: "Python handles the counting, validation, and packaging; Claude Cowork handles classification, drafting, and evidence checks; I approve each stage. [needs you: anything to add]"
dates: "June to September 2026"
relevant_to: ["Building with AI"]
requirements: [R2, R4, R5, R8, R9, R10]
aied_strands: [assessment]
why_learning: "Each question traces back to what was taught in a specific lecture, so the exam measures the course students actually had, not the course I planned."
order: 6
placeholder: false
---

## What I built

A pipeline for building multiple-choice exams from what was actually taught. It runs in stages: it takes in lecture transcripts and course materials, maps the topics, builds a blueprint with a fixed difficulty mix, drafts questions, audits them, locks the approved set, and packages it for import into Canvas. Nothing exports until all eight separate audit passes are clean.

I've used it for both Summer 2026 exams and the first Fall 2026 exam. The excerpts on this page use its fictional sample data, never real exam content.

## How I built it

The work is split by the kind of judgment it needs. Python handles everything deterministic: counting, schema checks, checksums, and packaging. Claude Cowork handles the semantic work: classifying content, drafting questions, and evaluating evidence. I sit at the checkpoints and authorize each stage before the next one runs.

The build started from written rules for each stage, data schemas for each hand-off, test cases, and fictional sample data to test against. The Python implementation was generated on June 3, 2026, and three follow-up releases tightened the schemas, test specifications, and sample data.

## What it changed

<span class="needs">[needs you: time saved, quality changes, anything students or colleagues noticed.]</span>

## What I'd change next

<span class="needs">[needs you]</span>
