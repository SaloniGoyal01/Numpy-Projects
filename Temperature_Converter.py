import numpy as np
import matplotlib.pyplot as plt

# 🌡️ Temperature data in Celsius (recorded for 10 days)
celsius = np.array([22.5, 23.0, 21.7, 25.1, 26.3, 24.5, 20.2, 22.8, 23.4, 25.6])

# 🔁 Convert Celsius to Fahrenheit using formula: F = C * 9/5 + 32
fahrenheit = celsius * 9 / 5 + 32

# 📊 Temperature Data Analysis (Mean, Median, Min, Max, Std Deviation)
print("📈 Temperature Data Analysis:")
print(f"Mean(C): {np.mean(celsius):.2f}, (F): {np.mean(fahrenheit):.2f}")           # Average
print(f"Median(C): {np.median(celsius):.2f}, (F): {np.median(fahrenheit):.2f}")     # Middle value
print(f"Min(C): {np.min(celsius):.2f}, (F): {np.min(fahrenheit):.2f}")              # Lowest value
print(f"Max(C): {np.max(celsius):.2f}, (F): {np.max(fahrenheit):.2f}")              # Highest value
print(f"Standard Deviation(C): {np.std(celsius):.2f}, (F): {np.std(fahrenheit):.2f}")  # Spread

# 📈 Create a new figure (plot area) with specific width and height in inches
plt.figure(figsize=(10, 5))

# 🔴 Plot the Celsius data as a red line with circular markers
plt.plot(celsius, label='Celsius', marker='o', color='red')

# 🔵 Plot the Fahrenheit data as a blue line with square markers
plt.plot(fahrenheit, label='Fahrenheit', marker='s', color='blue')


plt.title("Temperature Trends Over 10 Days")
plt.xlabel("Days")
plt.ylabel("Temperature")

# 🔍 Display the legend (uses 'label' values from plt.plot)
plt.legend()

# ➕ Show grid lines in the background for better readability
plt.grid(True)

# 🧩 Adjust layout to prevent overlap of labels, title, etc.
plt.tight_layout()

# 🖼️ Display the final plot window
plt.show()
