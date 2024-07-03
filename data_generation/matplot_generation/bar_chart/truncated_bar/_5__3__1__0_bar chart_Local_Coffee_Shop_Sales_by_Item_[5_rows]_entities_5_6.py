
import matplotlib.pyplot as plt

# Data for plotting
categories = [
    "Entertainment", "Music", "Travel", "Education", "Sports", "Fashion", "Health",
    "Environment", "Technology", "Economics", "Literature", "Science", "History", "Politics"
]
values = [
    35, 40, 20, 55, 25, 60, 50, 45, 70, 65, 30, 75, 15, 10
]

# Changing figure size
plt.figure(figsize=(10, 12))

# Plotting - vertical bar chart
bar_width = 0.8
plt.bar(categories, values, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF8F33', '#33FFEC',
    '#B833FF', '#FFE933', '#FF3333', '#33FFA5', '#8F33FF', '#FF3338',
    '#33FFD7', '#FF3380'
], width=bar_width)

# Customize chart
plt.ylabel('Value', fontsize=14)
plt.xlabel('Category', fontsize=14)
plt.title('Popularity of Various Topics in 2024', fontsize=16)

# Set y-axis limits
plt.ylim(5, 80)

# Resize bar width
plt.xticks(rotation=45, fontsize=10)

# Show plot
plt.show()