import numpy as np
import matplotlib.pyplot as plt

#  Fix random seed for reproducibility
np.random.seed(40)

#  Simulate 60 minutes (0–59)
minutes = np.arange(60)

# ❤️ Create a natural-looking heart rate pattern
base_rate = 70 + 30 * np.sin(minutes / 10)     # Heartbeat rises and falls with exercise
noise = np.random.normal(0, 5, size=60)        # Add slight randomness (like real data)
heart_rate = base_rate + noise                 # Final simulated heart rate

plt.figure(figsize=(12, 6))   # Sets the figure size (width = 12, height = 6)

# Plots the heart rate data:
# x = minutes, y = heart_rate
# color = red to look like pulse
# linewidth = 2 makes the line bolder
# label = 'Heart Rate' used in legend
plt.plot(minutes, heart_rate, color='red', linewidth=2, label='Heart Rate')

# Highlight max heart rate
max_hr = np.max(heart_rate)
max_min = np.argmax(heart_rate)

# Adds a blue dot at the maximum heart rate.
# zorder=5 puts the point above the line, not hidden.
plt.scatter(max_min, max_hr, color='blue', zorder=5)

plt.text(max_min + 1, max_hr, f"Max: {int(max_hr)} bpm", color='blue')

# Add zones (Safe & High)
plt.fill_between(minutes, 60, 100, color='green', alpha=0.1, label='Safe Zone')
plt.fill_between(minutes, 100, 140, color='orange', alpha=0.1, label='High Zone')

plt.title("❤️ Heart Rate Monitoring Simulation (1 Hour Exercise)", fontsize=14)
plt.xlabel("Time (minutes)")
plt.ylabel("Heart Rate (bpm)")

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right')
plt.tight_layout()

plt.show()
