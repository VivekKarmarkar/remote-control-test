# 🚶 I Built a 10-Page Physics Report While Walking — Here's How

## Claude Code's Remote Control Workflow: A Practical Guide

---

What if you could write code, generate plots, compile LaTeX documents, and push to GitHub — all from your phone, while going for a walk?

That's exactly what I did. Using **Claude Code** on my laptop and the **Claude mobile app** on my phone, I built a complete scientific computing project without touching a keyboard. Here's the workflow, the gotchas, and why it works.

---

## 🔧 The Setup

The idea is dead simple:

1. **Your laptop runs Claude Code** — the CLI tool that can read files, write code, run scripts, and manage git
2. **Your phone connects to the same session** — via the Claude app
3. **You give instructions in plain English** — Claude does the heavy lifting
4. **You verify on GitHub** — every commit is instantly viewable on your phone

That's it. Your laptop is the engine. Your phone is the steering wheel. GitHub is the rearview mirror.

---

## 🚀 Getting Started

Here's the exact protocol:

1. Run `/remote-control` in your current Claude Code session
2. Go to your phone → Claude Code app → tap **Code** → check if the session appears
3. Send a hello message to verify things are working
4. Do a test run:
   - **4a.** Ask Claude to write a Hello World Python script, generate a plot, commit and push
   - **4b.** Ask Claude for the GitHub link
   - **4c.** Open the link on your phone to verify
5. Go for a walk
6. Watch the magic happen while you walk

---

## ✅ What Works (Tested)

| Skill | Status |
|-------|--------|
| Permissions handling | ✅ |
| Plan mode | ✅ |
| Multi-agent swarms | ✅ |
| Git management | ✅ |
| Python coding | ✅ |
| Matplotlib plotting | ✅ |
| LaTeX report writing | ✅ |
| PDF creation | ✅ |

---

## ⚠️ Gotchas

A few things I learned the hard way:

- **Have your phone charger with you.** Intense sessions drain battery fast
- **Use a power bank.** Especially for longer walks
- **If the session hangs:** navigate to another chat and come back, or type "hey, are you there?" — the equivalent of hitting refresh

---

## 🔬 The Test: A Full Scientific Computing Project

To stress-test this workflow, I didn't start with "Hello World." I went straight for a real project: **the nonlinear pendulum**.

Starting from a single sentence — *"write Python code to solve the differential equation for a pendulum with large angle"* — the session grew into:

- A **10-page LaTeX report** with an abstract, 4 figures, 13 equations, stability analysis, and a bibliography
- **4 Python scripts** (RK4 integrator, trajectory comparison, period ratio, phase portrait)
- A **10-agent AI review swarm** (3 student agents, 3 teacher agents, 2 pedagogy experts, 2 data scientists) that analyzed the report and produced a prioritized revision plan
- A **clean repo** with `code/`, `plots/`, `report/` folders and a README

All while walking. Every intermediate result was committed to GitHub, where I verified it on my phone.

---

## 🎯 What Projects Is This Optimal For?

**Scientific computing.** Anything where the output is code, data, documents, or plots that GitHub can render. The workflow shines when you have a clear vision but don't want to type code on a tiny screen.

It's less suited for tasks requiring rapid visual iteration on a large screen — like fine-tuning a web UI or editing video.

---

## 💡 The Key Insight

The phone workflow works because of one simple loop:

> **You direct → Claude executes → Git captures → GitHub displays**

Your phone never needs to display code. It only needs to display *results*. And GitHub handles that beautifully — rendered markdown, inline images, PDF preview, syntax-highlighted code.

The laptop does the work. The phone does the thinking.

---

*All code and the full report are available at [github.com/VivekKarmarkar/remote-control-test](https://github.com/VivekKarmarkar/remote-control-test)*
