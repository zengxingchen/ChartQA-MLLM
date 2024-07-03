
import matplotlib.pyplot as plt

# Data
age_group = ['Infants', 'Toddlers', 'Preschool', 'School Age', 'Teens', 
             'Young Adults', 'Adults', 'Middle Age', 'Seniors']
average_sleep_hours = [14, 12, 11, 10, 9, 8, 7, 6.5, 6]

# Create horizontal bar chart
plt.figure(figsize=(10, 8))
colors = ['#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231',
          '#911eb4', '#42d4f4', '#f032e6', '#bfef45']

plt.barh(age_group, average_sleep_hours, color=colors, height=0.6)

# Customizing the plot
plt.xlabel('Average Sleep Hours')
plt.title('Average Hours of Sleep per Night by Age Group (2020)')
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()