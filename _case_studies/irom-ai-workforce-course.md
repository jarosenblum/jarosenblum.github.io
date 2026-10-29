---
title: "AI, Orchestration and the Value Chain"
summary: "The design for a new MIS course where students govern AI agents instead of writing code, built from five parallel research workstreams."
audience: "MIS undergraduates entering the job market"
status: "prototype"
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
  - { src: "/assets/snapshots/irom-ai-workforce-course/01-unit.png", alt: "Unit structure for a spreadsheet migration agent: five phases (diagnose, classify, checkpoint, build, defend), each with a judgment question, an activity, a deliverable, and a weight.", caption: "Unit structure: each phase pairs a judgment question with something students produce." }
  - { src: "/assets/snapshots/irom-ai-workforce-course/02-architecture.png", alt: "A map of the agent's seven reusable skills, from parsing a workbook to checking that migrated formulas give the same answers, and the gated workflows that sequence them.", caption: "The agent students design: its skills and how they connect." }
  - { src: "/assets/snapshots/irom-ai-workforce-course/03-case.png", alt: "A worked case: moving a shipment workbook from VLOOKUP to XLOOKUP, with the current formula, the migrated formula, and an audit check side by side.", caption: "A sample case, with an audit check on every change." }
tools: []
division_of_labor: ""
dates: "July 2026"
relevant_to: ["Turning strategy into learning sequences", "Changing course late", "Building with AI"]
requirements: [R4, R8, R2, R3, R5]
aied_strands: [workforce]
why_learning: "Entry-level MIS roles increasingly ask graduates to configure and supervise AI tools, not build them from scratch. Grading students on governance decisions, rather than on code, puts the course's weight where that work actually is."
order: 7
placeholder: false
---

## What I built

The design for a course in UT Austin's IROM department for MIS majors about to enter the job market. It draws on five research workstreams run in parallel: workforce AI literacy and adoption, business workflow redesign, adoption by technology and role, value-chain vendor positioning, and the gap between adoption and governance. Those feed into a 15-week schedule built around fixed technology cases.

In one sample unit, students take over an AI agent that migrates spreadsheet lookups from VLOOKUP to XLOOKUP. The seven skills the agent uses come pre-built and are treated as a black box, with their provenance disclosed: AI-generated, not hand-verified by the instructor. The orchestration template is deliberately incomplete, and some of its gates are wrong, so the students' first task is to audit what they've been handed. Because the technical layer is the same for everyone, differences in grades come from governance judgment, not code quality.

## How I built it

Each research finding carries an evidence tier: verified primary source, vendor self-report, or trade press. That way the course design can tell strong evidence from weak.

Midway through, the course was renamed and restructured, moving from one open project to three fixed technology cases. The design documents keep the superseded versions instead of deleting them, so each decision can be traced.
