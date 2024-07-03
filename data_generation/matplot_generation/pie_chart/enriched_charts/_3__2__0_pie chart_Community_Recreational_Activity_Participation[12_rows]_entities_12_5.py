
import matplotlib.pyplot as plt

# Data points
education_types = ['Primary Education', 'Secondary Education', 'Higher Education', 'Vocational Training', 'Adult Education', 'Special Education', 'Online Education', 'Others']
percentage_share = [25.0, 30.0, 20.0, 10.0, 5.0, 3.0, 5.0, 2.0]

# Colors using hexadecimal color codes
colors = ['#FF6347', '#FFD700', '#32CD32', '#1E90FF', '#FF69B4', '#8A2BE2', '#00CED1', '#FF4500']

# Plotting the pie chart
plt.figure(figsize=(10, 8))  # Width and height of the chart
plt.pie(percentage_share, labels=education_types, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Distribution of Education Types in 2023', pad=20)

# Display the chart
plt.show()