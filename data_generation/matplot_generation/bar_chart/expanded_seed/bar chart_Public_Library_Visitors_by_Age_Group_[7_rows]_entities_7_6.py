
import matplotlib.pyplot as plt
import numpy as np

# Data from the provided dictionary
data = [
    {'Age Group': '0-12', 'Visits on Monday': 120, 'Visits on Tuesday': 140, 'Visits on Wednesday': 130, 'Visits on Thursday': 110, 'Visits on Friday': 100},
    {'Age Group': '13-18', 'Visits on Monday': 80, 'Visits on Tuesday': 75, 'Visits on Wednesday': 85, 'Visits on Thursday': 90, 'Visits on Friday': 95},
    {'Age Group': '19-30', 'Visits on Monday': 60, 'Visits on Tuesday': 70, 'Visits on Wednesday': 65, 'Visits on Thursday': 68, 'Visits on Friday': 75},
    {'Age Group': '31-45', 'Visits on Monday': 70, 'Visits on Tuesday': 65, 'Visits on Wednesday': 68, 'Visits on Thursday': 72, 'Visits on Friday': 80},
    {'Age Group': '46-60', 'Visits on Monday': 50, 'Visits on Tuesday': 55, 'Visits on Wednesday': 53, 'Visits on Thursday': 58, 'Visits on Friday': 60},
    {'Age Group': '61+', 'Visits on Monday': 30, 'Visits on Tuesday': 25, 'Visits on Wednesday': 35, 'Visits on Thursday': 40, 'Visits on Friday': 38},
    {'Age Group': 'Unknown', 'Visits on Monday': 5, 'Visits on Tuesday': 10, 'Visits on Wednesday': 7, 'Visits on Thursday': 6, 'Visits on Friday': 9}
]

# Extracting data for plotting
age_groups = [d['Age Group'] for d in data]
monday_visits = [d['Visits on Monday'] for d in data]
tuesday_visits = [d['Visits on Tuesday'] for d in data]
wednesday_visits = [d['Visits on Wednesday'] for d in data]
thursday_visits = [d['Visits on Thursday'] for d in data]
friday_visits = [d['Visits on Friday'] for d in data]

# Define the width of the bars and the positions
bar_width = 0.15
r1 = np.arange(len(monday_visits))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]

# Start plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Create the bars
ax.bar(r1, monday_visits, color='b', width=bar_width, edgecolor='grey', label='Monday')
ax.bar(r2, tuesday_visits, color='r', width=bar_width, edgecolor='grey', label='Tuesday')
ax.bar(r3, wednesday_visits, color='g', width=bar_width, edgecolor='grey', label='Wednesday')
ax.bar(r4, thursday_visits, color='y', width=bar_width, edgecolor='grey', label='Thursday')
ax.bar(r5, friday_visits, color='m', width=bar_width, edgecolor='grey', label='Friday')

# Add labels, title, and legend
ax.set_xlabel('Age Group', fontweight='bold')
ax.set_ylabel('Number of Visits', fontweight='bold')
ax.set_title('Visits by Age Group and Day of the Week')
ax.set_xticks([r + bar_width*2 for r in range(len(monday_visits))]) #Adjust the position of the x-ticks
ax.set_xticklabels(age_groups)
ax.legend()

# Display the chart
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()