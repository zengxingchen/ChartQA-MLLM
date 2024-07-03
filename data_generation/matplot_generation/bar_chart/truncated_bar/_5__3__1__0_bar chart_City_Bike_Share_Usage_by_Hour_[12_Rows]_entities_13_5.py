
import matplotlib.pyplot as plt

# Data
topics = [
    'Arts & Design', 'Future Technologies & Society', 'Education & Learning',
    'Food & Nutrition', 'Politics & Governance', 'Health & Psychology',
    'Science & Nature', 'Business & Entrepreneurship', 'Fashion & Beauty',
    'Astronomy & Space Exploration', 'History & Archaeology', 'Sports & Fitness',
    'Music & Performing Arts', 'Environment & Climate Change', 'Culture & Society',
    'Entertainment & Leisure', 'Economics & Finance', 'Literature & Writing',
    'Philosophy & Ethics', 'Travel & Adventure'
]
hours_spent = [
    5, 8, 6.5, 4.5, 7, 6, 8.5, 5.5, 4, 9, 6, 7.5, 5.2, 7.8, 6.1,
    8, 6.7, 7.2, 5.8, 7.3
]

# Colors for each bar
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6',
    '#c4e17f', '#76d7c4', '#f7d358', '#e59866', '#f0b27a', '#af7ac5',
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6',
    '#c4e17f', '#76d7c4'
]

# Plotting the bar chart vertically
plt.figure(figsize=(14, 10))  # Change width and height of the chart
plt.bar(topics, hours_spent, color=colors, edgecolor='black', width=0.7)  # Change width for bars and apply color scheme

# Chart title and labels
plt.title('Average Weekly Hours Spent on Different Topics', fontsize=18, pad=20)
plt.ylabel('Average Hours Spent', fontsize=14)

# Setting the ylim to start from a specific value
plt.ylim(3, 10)

# Rotating the x labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the chart
plt.tight_layout()
plt.show()