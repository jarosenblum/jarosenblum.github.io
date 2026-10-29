---
title: "StatWiseAI tutorial"
summary: "A prototype that turns a nine-page responsible-AI tutorial for researchers into short modules with decision trees, prompt builders, and checklists."
audience: "Researchers learning to use StatWiseAI for data analysis"
status: "prototype"
link_mode: "walkthrough"
caveat: ""
paid_key: false
links:
  live: ""
  repo: ""
  repo_public_audited: false
downloads: []
request_key: false
screenshots:
  - { src: "/assets/snapshots/statwiseai/01-home.png", alt: "The StatWiseAI tutorial home page: a learning path of nine modules on the left and an overview of how the path works.", caption: "The learning path: nine short modules." }
  - { src: "/assets/snapshots/statwiseai/02-module-1.png", alt: "Module 1, Start Here: Responsible Use Rules, with a placeholder for a short video and an interactive check on what can be uploaded.", caption: "Module 1 starts with what you can and can't put into the tool." }
  - { src: "/assets/snapshots/statwiseai/03-module-3.png", alt: "A prompt builder form with fields for the research question, data source, outcome and covariates, and the assembled prompt below.", caption: "A prompt builder for data-analysis questions." }
  - { src: "/assets/snapshots/statwiseai/04-module-9.png", alt: "Module 9, Templates and Checklists: reusable prompt templates and a privacy checklist.", caption: "Templates and a privacy checklist to take away." }
tools: ["[needs you: confirm Claude Code]", "HTML, CSS, JavaScript"]
division_of_labor: "[needs you: your role vs. the center's]"
dates: "July 2026"
relevant_to: ["Building with AI", "Turning strategy into learning sequences"]
requirements: [R2, R4, R3, R5, R6]
aied_strands: [ai-literacy, adoption]
why_learning: "Researchers use a new tool responsibly when the rules are in front of them at the moment they need them, not in a policy page they read once. A teaching layer that links every step back to the official wording does that without rewriting the policy."
order: 5
placeholder: false
---

## What I built

A media-supported prototype for a research center at UT Austin's School of Nursing <span class="needs">[needs you: OK to name the center?]</span>. It turns the center's nine-page StatWiseAI tutorial into nine short modules:

1. Start here: responsible use
2. AI basics for researchers
3. Prompting for data analysis
4. Working with dataset documentation
5. Reviewing AI outputs
6. Requesting code in R, Python, SAS, Stata, or SPSS
7. Reproducibility and prompt history
8. Practice use cases with HRS and NHANES-style data
9. Templates and checklists

Each module replaces long blocks of text with an interactive support: a decision tree, a prompt builder, a comparison card, or a checklist. Module 1 is a gate, because its rules apply to every later module.

## How I built it

The design started from a full read of all nine source pages, classifying what kind of learning support each one needed. Two rules shaped the build. Every module links back to its source page, and no policy language is paraphrased, so the teaching layer can't drift from the official wording.

The architecture plan has two horizons. The short-term site is what's shown here. The long-term version uses the same page shell for a sandbox where researchers practice prompting a constrained model of StatWiseAI, alongside short videos of real sessions. Gaps for both were left open on purpose, so the second phase doesn't mean rebuilding the first.

## What it changed

<span class="needs">[needs you: whether the center has used or adopted it.]</span>

## What I'd change next

Build phase 2: the prompting sandbox and the short videos that show real sessions.
