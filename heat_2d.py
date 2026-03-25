import numpy as np
import matplotlib.pyplot as plt
import os

# -----------------------------
# Create results folder
# -----------------------------
os.makedirs("results", exist_ok=True)

# -----------------------------
# Grid parameters
# -----------------------------
nx, ny = 50, 50
Lx, Ly = 1.0, 1.0

dx = Lx / (nx - 1)
dy = Ly / (ny - 1)

# -----------------------------
# Physical parameter
# -----------------------------
alpha = 0.01
dt = 0.01   # CHANGE THIS later for instability test
nt = 200

# -----------------------------
# Stability condition
# -----------------------------
r_x = alpha * dt / dx**2
r_y = alpha * dt / dy**2

print(f"r_x = {r_x:.4f}, r_y = {r_y:.4f}")

if r_x + r_y > 0.5:
    print("⚠️ UNSTABLE configuration!")
else:
    print("✅ Stable configuration")

# -----------------------------
# Initialize temperature field
# -----------------------------
T = np.zeros((nx, ny))

# Boundary conditions
T[:, 0] = 100
T[:, -1] = 0
T[0, :] = 75
T[-1, :] = 50

# -----------------------------
# Store snapshots
# -----------------------------
snapshots = {}
snapshots[0] = T.copy()

# -----------------------------
# Time stepping
# -----------------------------
for n in range(nt):
    T_new = T.copy()

    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            T_new[i, j] = (
                T[i, j]
                + r_x * (T[i + 1, j] - 2*T[i, j] + T[i - 1, j])
                + r_y * (T[i, j + 1] - 2*T[i, j] + T[i, j - 1])
            )

    T = T_new.copy()

    # Save snapshots
    if n == nt//2:
        snapshots["mid"] = T.copy()

snapshots["final"] = T.copy()

# -----------------------------
# Plot snapshots
# -----------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

titles = ["Initial", "Mid", "Final"]

for i, (key, title) in enumerate(zip(snapshots.keys(), titles)):
    im = axes[i].imshow(snapshots[key], origin='lower')
    axes[i].set_title(title)
    axes[i].set_xlabel("X")
    axes[i].set_ylabel("Y")

fig.colorbar(im, ax=axes.ravel().tolist())
plt.tight_layout()

# Save image
import os

save_path = os.path.join(os.getcwd(), "results", "heat_evolution.png")
plt.savefig(save_path, dpi=300)

print("Saved at:", save_path)

plt.show()