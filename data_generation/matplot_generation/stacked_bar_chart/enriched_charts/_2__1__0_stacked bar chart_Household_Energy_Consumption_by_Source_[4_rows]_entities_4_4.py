
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
physical_health = [12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000]
mental_health = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000]
nutrition = [17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000]
exercise = [14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000]

fig, ax = plt.subplots(figsize=(14, 8))  # Change width and height of the chart

bar_width = 0.4  # Change width of bars

# Plotting data (change direction of chart to horizontal)
p1 = ax.barh(months, physical_health, bar_width, color='#1f77b4', label='Physical Health')
p2 = ax.barh(months, mental_health, bar_width, left=physical_health, color='#ff7f0e', label='Mental Health')
p3 = ax.barh(months, nutrition, bar_width, left=[i+j for i,j in zip(physical_health, mental_health)], color='#2ca02c', label='Nutrition')
p4 = ax.barh(months, exercise, bar_width, left=[i+j+k for i,j,k in zip(physical_health, mental_health, nutrition)], color='#d62728', label='Exercise')

ax.set_xlabel('Hours')
ax.set_title('Monthly Health Activities Comparison')
ax.set_yticks([i for i in range(len(months))])
ax.set_yticklabels(months)
ax.legend()

# Add numerical labels to each bar segment
for i in range(len(months)):
    ax.text(physical_health[i] / 2, i, str(physical_health[i]), ha='center', va='center', color='white')
    ax.text(physical_health[i] + mental_health[i] / 2, i, str(mental_health[i]), ha='center', va='center', color='white')
    ax.text(physical_health[i] + mental_health[i] + nutrition[i] / 2, i, str(nutrition[i]), ha='center', va='center', color='white')
    ax.text(physical_health[i] + mental_health[i] + nutrition[i] + exercise[i] / 2, i, str(exercise[i]), ha='center', va='center', color='white')

# Customize the grid
plt.grid(which='major', linestyle='--', linewidth='0.5', color='black')
plt.show()