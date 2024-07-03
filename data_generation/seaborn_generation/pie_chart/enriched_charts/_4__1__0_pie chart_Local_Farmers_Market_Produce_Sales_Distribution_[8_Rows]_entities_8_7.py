
import matplotlib.pyplot as plt

# Data
topics = ["Ancient Egypt", "Roman Empire", "Greek Mythology", "Medieval Europe", "Renaissance Art", "Industrial Revolution", "World Wars", "Modern History", "Contemporary Issues"]
values = [320, 250, 180, 200, 150, 100, 220, 170, 130]

# Colors
colors = [
    "#FF6347",  # Ancient Egypt
    "#FFD700",  # Roman Empire
    "#ADFF2F",  # Greek Mythology
    "#20B2AA",  # Medieval Europe
    "#9370DB",  # Renaissance Art
    "#FF4500",  # Industrial Revolution
    "#1E90FF",  # World Wars
    "#32CD32",  # Modern History
    "#FF69B4",  # Contemporary Issues
]

# Create pie chart
plt.figure(figsize=(12, 10))  # width and height in inches
plt.pie(values, labels=topics, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Popular Historical Topics in 2023', pad=20)

# Show plot
plt.show()