# import matplotlib.pyplot as plt
# import numpy as np
# import os
#
# colors_bb = ["blue", "cornflowerblue", "steelblue", "deepskyblue", "lightskyblue"]
# colors_bo = ["red", "tomato", "coral", "salmon", "lightsalmon"]
#
# # Plot all body+brain runs
# for run in range(1, 6):
#     fname = f"fitness_body_brain_run{run}.txt"
#     if os.path.exists(fname):
#         data = np.loadtxt(fname)
#         plt.plot(data, color=colors_bb[run-1], linestyle="--", alpha=0.6, label=f"Body+Brain Run {run}")
#
# # Plot all brain-only runs
# for run in range(1, 6):
#     fname = f"fitness_brain_only_run{run}.txt"
#     if os.path.exists(fname):
#         data = np.loadtxt(fname)
#         plt.plot(data, color=colors_bo[run-1], linestyle="-", alpha=0.6, label=f"Brain Only Run {run}")
#
# # Plot averages on top
# for label, color, ls in [("body_brain", "blue", "--"), ("brain_only", "red", "-")]:
#     runs = []
#     for run in range(1, 6):
#         fname = f"fitness_{label}_run{run}.txt"
#         if os.path.exists(fname):
#             runs.append(np.loadtxt(fname))
#     if runs:
#         avg = np.mean(runs, axis=0)
#         plt.plot(avg, color=color, linestyle=ls, linewidth=2.5,
#                  label=f"{label.replace('_', ' + ').title()} Average")
#
# plt.xlabel("Generation")
# plt.ylabel("Best Fitness (x displacement)")
# plt.title("Body+Brain vs Brain-Only Evolution (5 Runs Each)")
# plt.legend(fontsize=7)
# plt.tight_layout()
# plt.savefig("comparison_plot.png")
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
import os

fig, ax = plt.subplots(figsize=(10, 6))

# Collect all runs for averaging
bb_runs = []
bo_runs = []

# Plot individual runs with low opacity, no legend entries
for run in range(1, 6):
    fname = f"fitness_body_brain_run{run}.txt"
    if os.path.exists(fname):
        data = np.loadtxt(fname)
        bb_runs.append(data)
        ax.plot(data, color="blue", linestyle="--", alpha=0.15, linewidth=1)

for run in range(1, 6):
    fname = f"fitness_brain_only_run{run}.txt"
    if os.path.exists(fname):
        data = np.loadtxt(fname)
        bo_runs.append(data)
        ax.plot(data, color="red", linestyle="-", alpha=0.15, linewidth=1)

# Plot averages with full opacity and legend labels
if bb_runs:
    avg = np.mean(bb_runs, axis=0)
    ax.plot(avg, color="blue", linestyle="--", linewidth=2.5, label="Body + Brain")

if bo_runs:
    avg = np.mean(bo_runs, axis=0)
    ax.plot(avg, color="red", linestyle="-", linewidth=2.5, label="Brain Only")

ax.set_xlabel("Generation")
ax.set_ylabel("Best Fitness (x displacement)")
ax.set_title("Body+Brain vs Brain-Only Evolution (5 Runs Each)")
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig("comparison_plot.png")
plt.show()