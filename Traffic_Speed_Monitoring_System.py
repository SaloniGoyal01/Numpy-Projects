import numpy as np                     # NumPy is used for numerical operations
import matplotlib.pyplot as plt        # Matplotlib is used for plotting charts

# 🔐 Fixing the random seed so the random numbers stay the same every time you run the code (for consistency)
np.random.seed(42)

# 🚗 Generate 100 random vehicle speeds using normal distribution
# loc = mean (70 km/h), scale = standard deviation (10), size = 100 data points
speeds = np.random.normal(loc=70, scale=10, size=100)

# 💯 Round the speed values to 1 decimal place for neatness
speeds = np.round(speeds, 1)

# 🛑 Set the speed limit to 80 km/h
speed_limit = 80

# 📈 Display basic analysis in the console
print("🚦 Traffic Speed Monitoring System")
print(f"📌 Total Vehicles Recorded: {len(speeds)}")                     # Number of vehicles
print(f"📊 Average Speed: {np.mean(speeds):.2f} km/h")                  # Mean speed
print(f"🚀 Max Speed: {np.max(speeds):.2f} km/h")                       # Highest speed
print(f"🐢 Min Speed: {np.min(speeds):.2f} km/h")                       # Lowest speed
print(f"📉 Standard Deviation: {np.std(speeds):.2f} km/h")              # How spread out the speeds are

# 📉 Plot a histogram to show how speeds are distributed
plt.figure(figsize=(10, 5))  # Set the size of the plot

# Create the histogram: 
# x-axis = speed ranges, y-axis = number of vehicles in that range
plt.hist(speeds, bins=10, color='skyblue', edgecolor='black', label='Vehicle Speeds')

# 🔴 Draw a vertical line at the speed limit (for visual reference)
plt.axvline(speed_limit, color='red', linestyle='--', label='Speed Limit')

# 🎨 Add chart title and axis labels
plt.title("Traffic Speed Distribution")        # Main title of the chart
plt.xlabel("Speed (km/h)")                    # Label for the x-axis
plt.ylabel("Number of Vehicles")              # Label for the y-axis

# 📋 Show the legend so we know what the lines/colors mean
plt.legend()

# Add a grid to the chart for easier reading
plt.grid(True)

# Automatically adjust layout for better spacing
plt.tight_layout()

# 🎥 Display the plot
plt.show()
