
import matplotlib.pyplot as plt
import seaborn as sns

# Data
chart_data = [
    {'Category': 'Organic Waste', 'Percentage': 35}, 
    {'Category': 'Paper and Cardboard', 'Percentage': 27},
    {'Category': 'Plastics', 'Percentage': 13},
    {'Category': 'Glass', 'Percentage': 5},
    {'Category': 'Metal', 'Percentage': 10},
    {'Category': 'Miscellaneous', 'Percentage': 10}
]

# Extracting the categories and percentages for plotting
categories = [item['Category'] for item in chart_data]
percentages = [item['Percentage'] for item in chart_data]

# Seaborn color palette
colors = sns.color_palette('pastel', len(categories))

# Pie chart
plt.figure(figsize=(8, 8))  # Size of the figure
plt.pie(percentages, labels=categories, colors=colors, autopct='%.1f%%', startangle=140)

# Title and other visual improvements
plt.title('Waste Category Distribution')

# Show plot
plt.show()