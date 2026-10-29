---
title: "Relaxing Patterns"
summary: "A mindfulness app for iPhone and iPad that combines touch, ambient audio, animation, and paced reflective prompts into one calm, open-ended session."
audience: "Anyone who wants a few quiet minutes away from the endless scroll"
status: "live"
link_mode: "live"
caveat: ""
paid_key: false
links:
  live: "https://apps.apple.com/us/app/relaxing-patterns/id6763662279"
  live_label: "View on the App Store"
  repo: ""
  repo_public_audited: false
downloads: []
request_key: false
screenshots:
  - { src: "/assets/snapshots/relaxing-patterns/01-screen.png", alt: "Soft, blurred circles of colored light on a dark background, with the prompt Let your attention follow the circles.", caption: "An opening prompt. Touch makes and moves the light." }
  - { src: "/assets/snapshots/relaxing-patterns/02-screen.png", alt: "Warm orange and red light patterns on a dark background, with the prompt Let the sound deepen.", caption: "Later in a session, the prompts point to the sound." }
  - { src: "/assets/snapshots/relaxing-patterns/03-screen.png", alt: "Blue and green light patterns on a dark background, in a cooler palette.", caption: "One of several palettes for different moods." }
  - { src: "/assets/snapshots/relaxing-patterns/04-loop.png", alt: "Diagram: touch sets one of seven interaction states that drive ambient sound and animation; a session clock paces reflective prompts and a slow drift in the sound.", caption: "How touch, sound, motion and time respond to each other." }
tools: ["Codex", "SwiftUI", "AVAudioEngine"]
division_of_labor: ""
dates: "2026"
relevant_to: ["Multimodal design", "Building with AI", "Changing course late"]
requirements: [R2, R7, R8]
aied_strands: [game-based]
why_learning: "Calm is a design problem across several senses at once: what a touch does, what you hear next, how fast things move, and when the app says something. The same questions run through learning design: pacing, feedback that responds to what a person does, and no pressure to perform."
order: 3
placeholder: false
---

## What I built

A mindfulness app on the App Store for iPhone and iPad. There are no accounts and no goals: you tap and drag to make soft patterns of light, and the sound, motion, and prompts respond. It's built for one quiet minute or a longer session.

It works across four channels at once:

- **Touch.** Taps and drag gestures create the patterns, and how you touch matters. The app tells apart seven states, from idle and slow touch to bright touch, active gesture, deep, and reset.
- **Audio.** Each state has its own ambient loop. When your touch moves the app into a new state, it crossfades between loops, so the sound follows your hands without sudden cuts. Short tones answer interactions and briefly lower the ambient bed so they don't pile up.
- **Animation.** Patterns move on slow, 12-second easing cycles, and you can switch between several color palettes for different moods.
- **Prompts.** Short reflective lines appear in three phases: opening cues, orientation cues, then sparse cues and milestone messages as time passes.

What keeps a session going is its clock. The same timer that paces the prompts also shifts the sound: the tone and reverb drift slowly as the minutes pass. A longer session keeps changing without asking anything of you. The app collects no data.

## How I built it

I built it with Codex in SwiftUI, with the sound running through Apple's audio engine: looping players feed a mixer, then an equalizer and reverb, which the session clock adjusts over time.

I shipped it in stages, with the base app first and additional pattern packs planned as in-app purchases for a later update. A breath-aware version that listened through the microphone was moved to its own branch before release, so the released app stays touch-only, and the main code was checked to confirm none of that experiment remained.

## What it changed

As of October 28, 2026, the App Store lists 5 ratings averaging 5.0.
