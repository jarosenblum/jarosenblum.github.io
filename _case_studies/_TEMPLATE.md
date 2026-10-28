---
# Copy this file to _case_studies/<slug>.md. Fields marked REQUIRED are
# enforced by scripts/check_cases.rb before publishing.
title: ""                 # REQUIRED
summary: ""               # REQUIRED. One line: what it is and who it is for. Descriptive only.
audience: ""              # REQUIRED
status: ""                # REQUIRED. live | in use | beta | prototype | early alpha | partial
link_mode: ""             # REQUIRED. live | walkthrough | excerpt
caveat: ""                # REQUIRED when status is beta or early alpha, or paid_key is true
paid_key: false
links:
  live: ""
  repo: ""
  repo_public_audited: false   # repo links render only when true (public AND passed the audit)
downloads: []             # - label: Download for Mac
                          #   url: https://github.com/jarosenblum/jarosenblum.github.io/releases/...
                          #   note: Apple Silicon, macOS 11 or later
request_key: false        # shows a "Request a key" email button
screenshots:              # REQUIRED: 3 to 5, every app, live or not; alt text required
  - src: ""
    alt: ""
    caption: ""
tools: []                 # REQUIRED. e.g. Claude Code, Codex, ChatGPT
division_of_labor: ""     # REQUIRED. What I did, what the AI did, what collaborators did
dates: ""                 # REQUIRED
relevant_to: []           # plain-language tags shown publicly (D8)
requirements: []          # internal R-IDs; never rendered
aied_strands: []          # ids from _data/strands.yml
why_learning: ""          # 2–4 sentences; renders under "Why this matters for learning"
order: 99
placeholder: true         # set to false once P3 copy is in; the checker blocks publishing while true
---

## What I built

[P3]

## How I built it

[P3]

## What it changed

[P3]

## What I'd change next

[P3]
