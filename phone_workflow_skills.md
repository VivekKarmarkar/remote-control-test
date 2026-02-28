# Phone Workflow Skills

Remote development workflow: give instructions from phone → Claude executes on laptop → commit & push → verify on GitHub from phone.

| Skill | Tested | Output |
|-------|--------|--------|
| Git management | Yes | ✅ |
| Python coding | Yes | ✅ |
| Matplotlib plotting | Yes | ✅ |
| LaTeX report writing | Yes | ✅ |
| PDF creation (pdflatex) | Yes | ✅ |
| Permissions handling | Yes | ✅ |
| PPT creation | No | ❓ |
| GPU access | No | ❓ |

## What category of projects is this optimal for?

- Scientific computing
  - PAT scan PhD project
  - PINNs failures
  - PINN-QDE writing

## Next planned test

**RNN Pendulum Predictor + Final Slides**
- Generate pendulum trajectory dataset across many parameters/initial conditions
- Train a recurrent neural network to predict time evolution (requires GPU access test)
- Compare RNN-predicted phase portrait against ground truth
- Create final presentation slides summarizing the full project
