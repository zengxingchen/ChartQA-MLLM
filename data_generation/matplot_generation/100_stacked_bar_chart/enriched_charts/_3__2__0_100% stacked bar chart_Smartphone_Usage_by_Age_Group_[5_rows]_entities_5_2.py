
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010']
type_a = [20, 22, 25, 30, 27, 25, 20, 28, 25, 22, 30]
type_b = [30, 28, 25, 20, 23, 30, 35, 27, 30, 33, 25]
type_c = [25, 27, 30, 20, 28, 25, 25, 25, 20, 25, 20]
type_d = [25, 23, 20, 30, 22, 20, 20, 20, 25, 20, 25]

bar_width = 0.7

# Convert data to percentage
total = np.array(type_a) + np.array(type_b) + np.array(type_c) + np.array(type_d)
type_a_percent = np.array(type_a) / total * 100
type_b_percent = np.array(type_b) / total * 100
type_c_percent = np.array(type_c) / total * 100
type_d_percent = np.array(type_d) / total * 100

# Stacked bar chart
fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(categories, type_a_percent, color='#1f77b4', edgecolor='white', height=bar_width, label='Type A')
ax.barh(categories, type_b_percent, left=type_a_percent, color='#ff7f0e', edgecolor='white', height=bar_width, label='Type B')
ax.barh(categories, type_c_percent, left=type_a_percent + type_b_percent, color='#2ca02c', edgecolor='white', height=bar_width, label='Type C')
ax.barh(categories, type_d_percent, left=type_a_percent + type_b_percent + type_c_percent, color='#d62728', edgecolor='white', height=bar_width, label='Type D')

# Add title and labels
ax.set_title('Distribution of Various Types Over Years', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Year')

# Legend
ax.legend(loc='lower right', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()