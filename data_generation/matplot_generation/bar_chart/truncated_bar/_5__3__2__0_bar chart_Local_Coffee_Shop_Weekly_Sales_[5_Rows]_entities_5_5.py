
import matplotlib.pyplot as plt

# Generate data points
categories = [
    "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science",
    "Astronomy", "Earth Science", "Environmental Science", "Engineering", 
    "Medicine", "Psychology", "Sociology"
]
values = [180, 170, 160, 175, 190, 185, 165, 155, 200, 195, 150, 145]

plt.figure(figsize=(10, 12))  # Change the width and height of the chart

# Create a vertical bar chart with specified bar width and colors
plt.bar(categories, values, color=[
    '#4B0082', '#FF6347', '#4682B4', '#32CD32', '#FFD700', 
    '#DC143C', '#8A2BE2', '#00CED1', '#FF4500', '#8B4513', 
    '#6A5ACD', '#00FA9A'], width=0.5)

plt.ylabel('Number of Researchers', fontsize=14)
plt.title('Number of Researchers in Different Science Fields in 2023', fontsize=16)
plt.ylim(140, 210)  # Adjusted to start from 140 for better visualization

plt.tight_layout()
plt.show()