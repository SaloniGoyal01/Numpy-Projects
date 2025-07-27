import numpy as np
import matplotlib.pyplot as plt

#  Create a 10x10 empty grid (all values 0 initially)
pattern = np.zeros((10, 10))

for i in range(5) :    # 5 rows
    for j in range(10):     # 10 columns
        pattern[i, j] = (i + j) % 2

plt.imshow(pattern, cmap='viridis')    # Show pattern with 'viridis' color map (green-blue gradient)
plt.title("🟩 Geometric Grid Pattern")
plt.axis('off')
plt.show()        