---
title: "MIS 302F exam pipeline"
summary: "A pipeline that turns my lecture transcripts into an exam blueprint, draft questions, audits, and a Canvas-ready export, with four stops for my review."
audience: "My MIS 302F exams"
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
  - { src: "/assets/snapshots/mis302f-assessment-engine/01-overview.png", alt: "Diagram: eight pipeline stages from Ingest to Export, split between Claude Cowork and Python, with four review stops marked below.", caption: "Overview: where each stage runs and where it waits for me." }
  - { src: "/assets/snapshots/mis302f-assessment-engine/02-architecture.png", alt: "Architecture map: nine named agents in Claude Cowork and Python lanes, each with its output, and four instructor review points.", caption: "Architecture: every agent by name, what it hands on, and the four review stops." }
  - { src: "/assets/snapshots/mis302f-assessment-engine/03-audit-gate.png", alt: "Flowchart: five judgment audits and three rule audits feed one check; blocking findings go to instructor review before the set is locked.", caption: "The audit gate: blocking findings stop the run until I repair or override them." }
tools: ["Claude Cowork", "Claude Code", "Python"]
division_of_labor: "Python handles counting, validation, locking, and packaging; Claude Cowork handles classification, drafting, and the judgment audits; I review at four checkpoints. [needs you: anything to add]"
dates: "June to September 2026"
relevant_to: ["Building with AI"]
requirements: [R2, R4, R5, R8, R9, R10]
aied_strands: [assessment]
why_learning: "Each question traces back to what was taught in a specific lecture, so the exam measures the course students actually had, not the course I planned."
order: 6
placeholder: false
---

## What I built

A pipeline for building multiple-choice exams from what was actually taught. It runs in stages: it takes in lecture transcripts and course materials, maps the topics, builds a blueprint with a fixed difficulty mix, drafts questions, audits them, locks the approved set, and packages it for import into Canvas. Eight audits check the finished set, and any blocking finding stops the run until I repair or override it.

I've used it for both Summer 2026 exams and the first Fall 2026 exam. The diagrams on this page show how it's put together; no real exam content appears here.

## How I built it

The work is split by the kind of judgment it needs. Python handles everything deterministic: counting, schema checks, checksums, and packaging. Claude Cowork handles the semantic work: classifying content, drafting questions, and evaluating evidence. The pipeline stops at four points for my review: flagged transcript segments, flagged topics, the blueprint (which only I can approve), and any blocking audit finding. No stage can run until the one before it has finished.

The build started from written rules for each stage, data schemas for each hand-off, test cases, and fictional sample data to test against. The Python implementation was generated on June 3, 2026, and three follow-up releases tightened the schemas, test specifications, and sample data.

## What it changed

<span class="needs">[needs you: time saved, quality changes, anything students or colleagues noticed.]</span>

## What I'd change next

<span class="needs">[needs you]</span>
