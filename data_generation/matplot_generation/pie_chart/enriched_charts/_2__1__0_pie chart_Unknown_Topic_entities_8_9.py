
import matplotlib.pyplot as plt

# Data points
education_categories = ['STEM Education', 'Arts & Humanities', 'Vocational Training', 'Online Learning', 'Special Education', 'Adult Education', 'Others']
percentage = [20.0, 15.0, 18.0, 22.0, 8.0, 12.0, 5.0]
colors = ['#ff6666', '#ffcc99', '#66b3ff', '#99ff99', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Create a pie chart
plt.figure(figsize=(10, 7))  # Modify the width and height of the chart
plt.pie(percentage, labels=education_categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Market Share of Education Categories in 2023', pad=20)

# Display the chart
plt.show()