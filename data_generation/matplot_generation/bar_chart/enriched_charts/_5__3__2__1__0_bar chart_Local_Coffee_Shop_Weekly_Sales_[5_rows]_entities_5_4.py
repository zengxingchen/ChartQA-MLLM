
import matplotlib.pyplot as plt

# Data
sectors = ['Technology', 'Healthcare', 'Finance', 'Energy', 'Consumer Goods', 'Industrial',
           'Telecommunications', 'Utilities', 'Real Estate', 'Materials', 'Consumer Services',
           'Transportation', 'Media', 'Retail', 'Hospitality']
revenue = [80.5, 67.3, 55.2, 49.8, 44.1, 37.6, 35.9, 33.7, 31.8, 29.4, 27.1, 25.8, 23.5, 22.7, 20.3]

# Color scheme using color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFF5', '#FFB833',
          '#8D33FF', '#33FFBD', '#FF3333', '#33FF77', '#335BFF', '#FF339E',
          '#33FFDD', '#FF8533', '#8DFF33']

# Create horizontal bar chart
plt.figure(figsize=(12, 10))
bars = plt.barh(sectors, revenue, color=colors, height=0.5)

# Adjusting the width of bars
for bar in bars:
    bar.set_height(0.4)

# Changing the layout and labels
plt.xlabel('Revenue (billions)', fontsize=12)
plt.title('Top Revenue-Generating Sectors in 2023', fontsize=16)
plt.xlim(min(revenue) * 0.9, max(revenue) * 1.1)  # Set x-axis limit higher to accommodate labels

# Adding value labels on the right of each bar
for i, v in enumerate(revenue):
    plt.text(v + 1, i, str(v), color='black', va='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()