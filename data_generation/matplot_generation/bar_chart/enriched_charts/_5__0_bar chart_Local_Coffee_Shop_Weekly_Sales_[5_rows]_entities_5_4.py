
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
total_articles = [50, 45, 60, 70, 65, 68, 55, 72, 74, 70, 65, 62]

# Color scheme using specific color codes
colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B',
          '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF', '#AEC7E8', '#FFBB78']

# Create vertical bar chart
plt.figure(figsize=(10, 12))
bars = plt.bar(months, total_articles, color=colors, width=0.6)

# Adjusting the width of bars
for bar in bars:
    bar.set_width(0.5)

# Changing the layout and labels
plt.ylabel('Total Articles', fontsize=12)
plt.title('Monthly Publication Count in a Magazine', fontsize=16)
plt.ylim(40, max(total_articles) * 1.1)  # Set y-axis limit higher to accommodate labels

# Adding value labels on top of each bar
for i, v in enumerate(total_articles):
    plt.text(i, v + 2, str(v), color='black', ha='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()