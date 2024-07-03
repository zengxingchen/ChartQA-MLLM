
import matplotlib.pyplot as plt

# Data
categories = [
    'Beaches', 'Mountains', 'Cities', 'Historical Sites', 
    'Forests', 'Deserts', 'Islands'
]
percentages = [28.0, 22.0, 18.0, 15.0, 10.0, 5.0, 2.0]

# Colors
colors = [
    '#FF6347', '#4682B4', '#FFD700', '#32CD32', '#8A2BE2', 
    '#FF4500', '#20B2AA'
]

# Plot
plt.figure(figsize=(12, 8))  # Width and height of the chart
plt.pie(percentages, labels=categories, colors=colors, startangle=90, autopct='%1.1f%%')

plt.title("Preferred Travel Destinations in 2023", pad=30)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()