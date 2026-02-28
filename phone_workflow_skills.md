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

## Gotchas

- Phone running out of battery — have your charger with you
- If sessions get intense, use a power bank

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
