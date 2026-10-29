---
title: "SpeedGrader Rubric Review"
summary: "A Mac app that drafts rubric-based grading recommendations for an instructor to review in Canvas SpeedGrader. It never submits a grade."
audience: "Instructors grading written work against a Canvas rubric"
status: "in use"
link_mode: "walkthrough"
caveat: ""
paid_key: false
links:
  live: ""
  repo: ""
  repo_public_audited: false
downloads:
  - { label: "Download for Mac", url: "/downloads/SpeedGrader-Rubric-Review-macOS-v0.1.0.zip", note: "Apple Silicon, macOS 11 or later, v0.1.0, 18 MB. Needs a key." }
request_key: true
screenshots:
  - { src: "", alt: "", caption: "" }
  - { src: "", alt: "", caption: "" }
  - { src: "", alt: "", caption: "" }
tools: ["Claude Code", "Python"]
division_of_labor: "[needs you: what you decided and wrote vs. what Claude Code generated]"
dates: "July to September 2026"
relevant_to: ["Building with AI", "Building to think", "Reflective practice"]
requirements: [R2, R7, R9, R8, R10]
aied_strands: [assessment]
why_learning: "Feedback is only useful if an instructor can see where it came from. Tying every recommendation to a passage the instructor can check, and keeping the grade decision with the instructor, is how I think AI belongs in assessment: as a draft that shows its evidence, not a verdict."
order: 1
placeholder: false
---

## What I built

A desktop app for grading written work against a rubric. It loads the rubric directly from Canvas's rubric export, along with the assignment description, then drafts a recommendation for each criterion and quotes the passages in the submission that support it. The instructor reads the draft and enters the grade in SpeedGrader themselves.

There are three things it will never do: submit a grade, publish anything to a course, or claim that a submission was written by AI. Those limits are written into the app's rules, not left to habit. Every quote it cites is checked against the submission text, and any quote it can't find is flagged for the instructor instead of being shown as evidence.

## How I built it

I built it with Claude Code over six weeks: first commit July 31, 2026, latest September 10, 38 commits in all. The build started from written rules for each stage: what it may and may not do, what it hands to the next stage, and where a person has to sign off. The rules come with tests, and 112 of them currently pass.

Real course data never enters the code repository. Each person who runs the app uses their own API key, which the app stores outside the project, so no shared key ships inside the download.

I also audited it on real work. A line-by-line check of two of its evaluations found that some "quote not found" flags were false alarms, that a name-redaction step had silently removed an author's surname from a works-cited list, and that the app was using only three of the rubric's five performance tiers. Each finding is logged in the backlog with a proposed fix.

## What it changed

<span class="needs">[needs you: what changed for you or for colleagues who use it — time per batch, consistency, who else grades with it.]</span>

## What I'd change next

- Check quotes that join two passages with an ellipsis piece by piece, so they stop raising false alarms.
- Show the instructor exactly which word a name redaction replaced.
- Add a way to change a saved API key from inside the app.
- Build the second track, which packages course pages and quizzes for import into Canvas. It's designed but not yet built.
