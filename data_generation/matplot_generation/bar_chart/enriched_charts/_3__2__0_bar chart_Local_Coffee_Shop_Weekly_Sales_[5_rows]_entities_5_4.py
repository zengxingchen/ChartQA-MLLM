
import matplotlib.pyplot as plt

# Data
countries = ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria',
             'Bangladesh', 'Russia', 'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam']
population = [1444, 1391, 332, 276, 225, 214, 213, 166, 146, 126, 125, 118, 114, 112, 100]

# Color scheme using specific color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#F7DC6F', '#BB8FCE', '#76D7C4', '#F1948A', 
          '#F5B7B1', '#A9DFBF', '#AED6F1', '#F9E79F', '#D7BDE2', '#85C1E9', '#FAD7A0', '#EDBB99']

# Create horizontal bar chart
plt.figure(figsize=(14, 9))
bars = plt.barh(countries, population, color=colors, height=0.6)

# Adjusting the width and height of bars
for bar in bars:
    bar.set_height(0.5)

# Changing the layout and labels
plt.xlabel('Population (in millions)', fontsize=12)
plt.title('Population Data of Top 15 Most Populous Countries (2024)', fontsize=16)
plt.xlim(0, max(population) * 1.1)  # Set x-axis limit higher to accommodate labels

# Adding value labels to the right of each bar
for i, v in enumerate(population):
    plt.text(v + 10, i, str(v), color='black', va='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()