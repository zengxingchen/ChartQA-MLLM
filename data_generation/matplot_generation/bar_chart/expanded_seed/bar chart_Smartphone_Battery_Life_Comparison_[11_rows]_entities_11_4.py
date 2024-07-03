
import matplotlib.pyplot as plt
import numpy as np

# Given data
data = [
    {'Model': 'iPhone 12', 'Brand': 'Apple', 'Release Year': 2020, 'Battery Capacity (mAh)': 2815, 'Talk Time (Hours)': 20, 'Standby Time (Hours)': 65},
    {'Model': 'Galaxy S21', 'Brand': 'Samsung', 'Release Year': 2021, 'Battery Capacity (mAh)': 4000, 'Talk Time (Hours)': 22, 'Standby Time (Hours)': 75},
    {'Model': 'Pixel 5', 'Brand': 'Google', 'Release Year': 2020, 'Battery Capacity (mAh)': 4080, 'Talk Time (Hours)': 25, 'Standby Time (Hours)': 70},
    {'Model': 'OnePlus 8T', 'Brand': 'OnePlus', 'Release Year': 2020, 'Battery Capacity (mAh)': 4500, 'Talk Time (Hours)': 23, 'Standby Time (Hours)': 72},
    {'Model': 'iPhone 11', 'Brand': 'Apple', 'Release Year': 2019, 'Battery Capacity (mAh)': 3110, 'Talk Time (Hours)': 17, 'Standby Time (Hours)': 65},
    {'Model': 'Galaxy S20', 'Brand': 'Samsung', 'Release Year': 2020, 'Battery Capacity (mAh)': 4000, 'Talk Time (Hours)': 19, 'Standby Time (Hours)': 71},
    {'Model': 'Pixel 4a', 'Brand': 'Google', 'Release Year': 2020, 'Battery Capacity (mAh)': 3140, 'Talk Time (Hours)': 24, 'Standby Time (Hours)': 72},
    {'Model': 'OnePlus 7T', 'Brand': 'OnePlus', 'Release Year': 2019, 'Battery Capacity (mAh)': 3800, 'Talk Time (Hours)': 20, 'Standby Time (Hours)': 70},
    {'Model': 'Moto G Power', 'Brand': 'Motorola', 'Release Year': 2020, 'Battery Capacity (mAh)': 5000, 'Talk Time (Hours)': 35, 'Standby Time (Hours)': 100},
    {'Model': 'iPhone SE (2nd gen)', 'Brand': 'Apple', 'Release Year': 2020, 'Battery Capacity (mAh)': 1821, 'Talk Time (Hours)': 15, 'Standby Time (Hours)': 50},
    {'Model': 'Xiaomi Mi 11', 'Brand': 'Xiaomi', 'Release Year': 2021, 'Battery Capacity (mAh)': 4600, 'Talk Time (Hours)': 24, 'Standby Time (Hours)': 85}
]

# Separate data lists for plotting
models = [d['Model'] for d in data]
battery_capacities = [d['Battery Capacity (mAh)'] for d in data]
talk_times = [d['Talk Time (Hours)'] for d in data]

# Setup for bar chart
bar_width = 0.35
index = np.arange(len(models))

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(14, 8))

# First bar chart with Battery Capacities
battery_bars = ax.bar(index, battery_capacities, bar_width, label='Battery Capacity (mAh)', color='skyblue', hatch='*')

# Second bar chart with Talk Time, with an offset on the x-axis
talk_time_bars = ax.bar(index + bar_width, talk_times, bar_width, label='Talk Time (Hours)', color='lightgreen', hatch='/')

# Adding labels, title, and legend
ax.set_xlabel('Smartphone Models', fontsize=12)
ax.set_ylabel('Battery Capacity and Talk Time', fontsize=12)
ax.set_title('Battery Capacity (mAh) and Talk Time (Hours) by Smartphone Model', fontsize=14)
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(models, fontsize=10, rotation=45, ha='right')
ax.legend()

# Display all battery capacities and talk times above the bars
for bar in battery_bars:
    height = bar.get_height()
    ax.annotate('{}'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

for bar in talk_time_bars:
    height = bar.get_height()
    ax.annotate('{}'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()