
import matplotlib.pyplot as plt

# Data points
degrees = ["Bachelor's Degree", "Master's Degree", "Associate Degree", "Doctoral Degree", "Professional Degree", "Diploma", "Certificate", "Others"]
percentages = [40.0, 25.0, 10.0, 8.0, 7.0, 5.0, 3.0, 2.0]

# Colors using hexadecimal color codes
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6', '#f1c40f', '#e67e22', '#1abc9c', '#34495e']

# Plotting the pie chart
plt.figure(figsize=(10, 8))  # Width and height of the chart
plt.pie(percentages, labels=degrees, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title("Distribution of Degrees Earned in 2023", pad=20)

# Display the chart
plt.show()