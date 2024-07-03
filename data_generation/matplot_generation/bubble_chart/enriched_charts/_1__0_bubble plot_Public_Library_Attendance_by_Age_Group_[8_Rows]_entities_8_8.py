
import matplotlib.pyplot as plt

# Data
age_groups = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']
physical_activity = [1.2, 2.8, 2.5, 1.9, 1.5, 1.2, 1.1, 0.9, 0.7]
number_of_participants = [120000, 250000, 220000, 180000, 150000, 130000, 110000, 90000, 70000]

# Custom colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']

# Set figure size
plt.figure(figsize=(14, 9))

# Scatter plot with bubble sizes
bubble_sizes = [n / 1000 for n in number_of_participants]  # Scaling the number of participants for bubble size
plt.scatter(age_groups, physical_activity, s=bubble_sizes, c=colors, alpha=0.6)

# Labels and title
plt.xlabel('Age Group')
plt.ylabel('Average Daily Physical Activity (hours)')
plt.title('Average Daily Hours of Physical Activity by Age Group', pad=20)

# Show plot
plt.show()