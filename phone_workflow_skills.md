# Phone Workflow Skills

Remote development workflow: give instructions from phone → Claude executes on laptop → commit & push → verify on GitHub from phone.

| Skill | Tested | Output |
|-------|--------|--------|
| Permissions handling | Yes | ✅ |
| Plan mode | Yes | ✅ |
| Agents | Yes | ✅ |
| Git management | Yes | ✅ |
| GPU access | No | ❓ |
| Python coding | Yes | ✅ |
| Matplotlib plotting | Yes | ✅ |
| LaTeX report writing | Yes | ✅ |
| PDF creation (pdflatex) | Yes | ✅ |
| PPT creation | No | ❓ |
| Web Search | No | ❓ |

## Getting started

1. Run `/remote-control` in your current Claude Code session
2. Go to your phone → Claude Code app → click on Code → check if the current session appears
3. Send a hello message to verify things are working
4a. Do a test commit and push with a Hello World Python script and a sample plot
4b. Ask Claude Code for the GitHub link
4c. Open the link on your phone to verify
5. Go for a walk
6. Watch the magic happen while you walk

## Gotchas

- Have phone charger with you
- Use power bank for phone
- If session hangs: navigate to another chat and come back, or type "hey are you there"

## What category of projects is this optimal for?

- Scientific computing
  - GPT-Bhojan ViT-finetuning (the scientific computing part)
  - PINNs failures
  - PAT scan PhD project
  - PINN-QDE writing

## Next planned test

**RNN Pendulum Predictor + Final Slides**
- Generate pendulum trajectory dataset across many parameters/initial conditions
- Train a recurrent neural network to predict time evolution (requires GPU access test)
- Compare RNN-predicted phase portrait against ground truth
- Create final presentation slides summarizing the full project
