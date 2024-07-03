
import matplotlib.pyplot as plt

# Subject scores data
subjects = [
    "Apples", "Bananas", "Cherries", "Dates", "Elderberries", 
    "Figs", "Grapes", "Honeydew", "Indian Figs", 
    "Jackfruit", "Kiwis", "Lemons"
]
values = [75, 80, 90, 85, 78, 92, 87, 81, 84, 88, 86, 89]

# New color scheme using specific color codes for each subject
colors = [
    '#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', 
    '#DC143C', '#20B2AA', '#FF4500', '#DA70D6', 
    '#00BFFF', '#FFDAB9', '#7B68EE'
]

# Create horizontal bar chart
plt.figure(figsize=(14, 8))  # Width and height of the chart
plt.barh(subjects, values, color=colors, height=0.6)  # Bar color and band height

# Set the title and labels
plt.title('Favorite Fruits Popularity', fontsize=18, pad=20)
plt.xlabel('Popularity Score', fontsize=14)
plt.ylabel('Fruit', fontsize=14)

# Set y-axis limit starting from 70
plt.xlim(70, 100)

# Display the bar chart
plt.show()