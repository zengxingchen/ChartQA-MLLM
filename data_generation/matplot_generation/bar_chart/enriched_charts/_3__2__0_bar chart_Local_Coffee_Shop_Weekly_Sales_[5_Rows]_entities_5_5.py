
import matplotlib.pyplot as plt

# Generate data points
categories = [
    "Painting", "Sculpture", "Architecture", "Photography", "Graphic Design",
    "Fashion Design", "Interior Design", "Product Design", "Animation", 
    "Calligraphy", "Illustration", "Digital Art"
]
values = [150, 120, 110, 140, 130, 170, 160, 145, 155, 125, 135, 150]

plt.figure(figsize=(14, 8))  # Change the width and height of the chart

# Create a horizontal bar chart with specified bar width and colors
plt.barh(categories, values, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#9edae5', '#e7969c'], height=0.6)

plt.xlabel('Number of Students', fontsize=14)
plt.title('Enrollment in Different Art & Design Disciplines in 2023', fontsize=16)
plt.xlim(0, 200)  # Adjusted to give some space for readability

plt.tight_layout()
plt.show()