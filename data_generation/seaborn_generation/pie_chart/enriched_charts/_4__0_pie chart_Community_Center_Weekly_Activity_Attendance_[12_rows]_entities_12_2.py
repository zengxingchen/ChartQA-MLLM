
import matplotlib.pyplot as plt

# Data setup
topics = ['Health', 'Education', 'Science', 'Arts', 'Sports', 'Technology', 'History']
values = [45, 20, 15, 10, 5, 3, 2]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666']

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))  # width and height of the chart
ax.pie(values, labels=topics, autopct='%1.1f%%', colors=colors, startangle=90)
ax.set_title('Distribution of Interests in Different Topics')

# Show plot
plt.show()