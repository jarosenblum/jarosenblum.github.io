---
title: "UGS 302: Generative AI Literacy"
summary: "The design system behind a first-year signature course I'm teaching in Fall 2026: one course model drives the schedule graphics, rubrics, templates, and checks."
audience: "First-year students at UT Austin"
status: "in use"
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
  - { src: "", alt: "", caption: "" }
  - { src: "", alt: "", caption: "" }
  - { src: "", alt: "", caption: "" }
tools: ["[needs you: tools — e.g. Claude Code, Python, JavaScript]"]
division_of_labor: "[needs you: what you designed vs. what AI tools generated]"
dates: "Summer to Fall 2026"
relevant_to: ["Building with AI", "Turning strategy into learning sequences", "Changing course late", "Reflective practice"]
requirements: [R1, R2, R4, R8, R9, R3, R10]
aied_strands: [ai-literacy]
why_learning: "Students learn AI literacy by doing what the course is about: writing with AI and documenting how they did it. The prompt journal makes that process visible to them and to me, which is where the conversation about judgment starts."
order: 2
placeholder: false
---

## What I built

UGS 302 is a first-year signature course on generative AI literacy. Each student picks an under-acknowledged historical figure connected to their field and develops that character across three milestones: a proposal, a research brief, and a short narrative in which the character meets a contested AI scenario that their team has agreed on. Every milestone includes a prompt journal documenting how the student used AI.

Behind the course is a single course model, a file that defines every graded component: its weight, due date, AI-use condition, and what it depends on. The schedule graphics and a validation script are generated from that file, so the course can't quietly disagree with itself. Build scripts generate the decks, rubrics, templates, and character cards from the same sources.

I also built two Claude skills for students. One checks a draft section against the assignment's rules and reports what to fix. The other helps a team with its script: it reviews the team's blocking, suggests fixes, and drafts dialogue in each character's voice.

## How I built it

Before the term, I used a simulation that walked two student personas through the semester week by week, tracking workload, perceived learning, and enjoyment. Four rounds of that simulation shaped the design. One milestone was redesigned into a scenario-free character introduction, a co-authorship workshop was set for week 8, and a team milestone moved to week 11 with a 14-day window.

The rebuilt visual strategy opens with a table of what the first version got wrong and how each error was corrected.

## What it changed

<span class="needs">[needs you: what you've seen this term — student work, prompt journals, anything you've adjusted.]</span>

## What I'd change next

<span class="needs">[needs you]</span>
