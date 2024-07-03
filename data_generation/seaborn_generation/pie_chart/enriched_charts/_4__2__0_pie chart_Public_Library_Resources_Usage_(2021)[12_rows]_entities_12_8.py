
import matplotlib.pyplot as plt

# Data to plot
labels = 'Fashion & Beauty', 'Sports & Fitness', 'Business & Entrepreneurship', 'Travel & Adventure', 'Literature & Writing', 'Food & Nutrition', 'Entertainment & Leisure', 'Music & Performing Arts', 'Education & Learning'
sizes = [25, 20, 15, 18, 10, 12, 8, 5, 7]
colors = ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7', '#999999', '#F4A582']

# Plot
plt.figure(figsize=[12, 8])  # Set the width and height of the chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Interests by Topic')
plt.show()