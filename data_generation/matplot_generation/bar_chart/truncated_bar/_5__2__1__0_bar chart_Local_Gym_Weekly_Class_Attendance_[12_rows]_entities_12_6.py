
import matplotlib.pyplot as plt

# Data
topics = ['Travel', 'Future Technologies', 'History', 'Environment', 'Food',
          'Health', 'Entertainment', 'Fashion', 'Philosophy', 'Science',
          'Literature', 'Sports', 'Education', 'Business', 'Culture', 'Art',
          'Music', 'Economics', 'Astronomy', 'Politics']
books_published = [850, 670, 560, 430, 780,
                   650, 720, 540, 300, 620,
                   750, 510, 600, 680, 450, 370,
                   520, 580, 430, 640]

# Create vertical bar chart
plt.figure(figsize=(12, 9))  # Change width and height of the chart
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8633', 
          '#33FF86', '#8633FF', '#FF3380', '#3380FF', '#80FF33',
          '#FF3386', '#3386FF', '#FF5733', '#33FF57', '#3357FF', 
          '#FF33A8', '#FF8633', '#33FF86', '#8633FF', '#FF3380']

plt.bar(topics, books_published, color=colors, width=0.6)  # Change direction of chart and bar width

# Customizing the plot
plt.ylabel('Number of Books Published')
plt.title('Number of Books Published by Topic (2021)', pad=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Setting y-axis limit to start from a specific value
plt.ylim(250, 900)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()