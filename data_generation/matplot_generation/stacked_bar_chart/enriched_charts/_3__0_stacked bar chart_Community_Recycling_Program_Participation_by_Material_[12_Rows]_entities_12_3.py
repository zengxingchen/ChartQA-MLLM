
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
math = [78, 82, 85, 90, 88, 82, 85, 80, 88, 85, 78, 90]
science = [85, 78, 80, 82, 85, 90, 88, 78, 82, 85, 82, 88]
english = [82, 88, 90, 85, 80, 88, 82, 85, 90, 88, 85, 78]
history = [90, 85, 82, 88, 78, 85, 80, 82, 85, 90, 88, 82]

# Stacked bar chart data accumulation
bars_science = np.add(math, science).tolist()
bars_english = np.add(bars_science, english).tolist()

# Modify the color scheme using hexadecimal color codes
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

fig, ax = plt.subplots(figsize=(12, 8)) # Change size of the chart

# Creating the vertical bar chart
ax.bar(months, math, color=colors[0], edgecolor='white', width=0.6, label='Math')
ax.bar(months, science, bottom=math, color=colors[1], edgecolor='white', width=0.6, label='Science')
ax.bar(months, english, bottom=bars_science, color=colors[2], edgecolor='white', width=0.6, label='English')
ax.bar(months, history, bottom=bars_english, color=colors[3], edgecolor='white', width=0.6, label='History')

# Customizing the vertical stacked bar chart with the new topic: 'Monthly Student Performance'
plt.title('Monthly Student Performance in Different Subjects', pad=20)
plt.xlabel('Month')
plt.ylabel('Scores')
plt.yticks(np.arange(0, 301, 20))
plt.xticks(months)
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the final plot
plt.show()