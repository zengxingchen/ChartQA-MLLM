
import matplotlib.pyplot as plt

# Data from chart table
data = [
    {'Activity': 'Book Borrowing', 'Percentage of Visitors': 40.0},
    {'Activity': 'Study Space Use', 'Percentage of Visitors': 25.0},
    {'Activity': 'Internet Use', 'Percentage of Visitors': 15.0},
    {'Activity': 'Community Events', 'Percentage of Visitors': 8.0},
    {"Activity": "Children's Programs", 'Percentage of Visitors': 5.0},
    {'Activity': 'Research Assistance', 'Percentage of Visitors': 3.0},
    {'Activity': 'Book Sales', 'Percentage of Visitors': 2.0},
    {'Activity': 'Exhibitions', 'Percentage of Visitors': 1.0},
    {'Activity': 'Gaming', 'Percentage of Visitors': 0.5},
    {'Activity': 'Other Services', 'Percentage of Visitors': 0.5}
]

# Extracting activities and their corresponding percentages
activities = [item['Activity'] for item in data]
percentages = [item['Percentage of Visitors'] for item in data]

# Define colors and explode options for emphasis
colors = plt.cm.tab20.colors  # Using color map with enough unique colors
explode = (0.1, 0.05, 0, 0, 0, 0, 0, 0, 0, 0)  # Emphasize 'Book Borrowing' and 'Study Space Use'

# Create pie chart
plt.figure(figsize=(10, 6))
plt.pie(
    percentages, 
    explode=explode, 
    labels=activities, 
    colors=colors, 
    autopct='%1.1f%%',    # Add percentages with one decimal
    startangle=140,        # Rotate start of the pie chart for better positioning
    shadow=True,           # Add shadow for a 3D look
    wedgeprops={'edgecolor': 'black'},  # Add edge color to the wedges
    textprops={'fontsize': 9}  # Control text properties for clarity
)

# Title and show the pie chart
plt.title('Library Visitors Distribution by Activity')
plt.tight_layout()
plt.show()