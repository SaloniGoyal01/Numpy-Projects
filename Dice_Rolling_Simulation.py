import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)    # Set seed so we get the same random result every time (for testing)
rolls = np.random.randint(1, 7, size=1000)    # Simulate 1000 dice rolls (numbers from 1 to 6)
unique, counts = np.unique(rolls, return_counts=True)    # Count how many times each number (1–6) appears

# Print each number and how many times it was rolled
for i,j in zip(unique, counts):
    print(f"Number {i} rolled {j} times")

# 📉 Create a bar chart for the dice roll results
plt.bar(unique, counts, color='green', edgecolor='black')

plt.title("Dice Roll Simulation (1000 Rolls)")
plt.xlabel("Dice Face")
plt.ylabel("Frequency")
plt.xticks(unique)        # 🔢 Set the tick marks on x-axis to exactly 1 to 6 (not 0 to 6)

# Add horizontal dashed grid lines on y-axis for better readability
# plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

