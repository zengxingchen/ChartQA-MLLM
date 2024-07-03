
import matplotlib.pyplot as plt

# Input data
data = [
    {'Activity': 'Walking', 'Number of Visitors': 1500},
    {'Activity': 'Picnicking', 'Number of Visitors': 800},
    {'Activity': 'Jogging', 'Number of Visitors': 500},
    {'Activity': 'Playground', 'Number of Visitors': 450},
    {'Activity': 'Tennis', 'Number of Visitors': 300},
    {'Activity': 'Basketball', 'Number of Visitors': 200},
    {'Activity': 'Bird Watching', 'Number of Visitors': 150},
    {'Activity': 'Gardening', 'Number of Visitors': 100}
]

# Extracting activity labels and corresponding visitor numbers
activities = [entry['Activity'] for entry in data]
visitors = [entry['Number of Visitors'] for entry in data]

# Define pie chart colors for better distinction
colors = [
    '#ff9999','#66b3ff','#99ff99','#ffcc99',
    '#c2c2f0','#ffb3e6','#c4e17f','#f9bb2d'
]

# Creating the pie chart
plt.figure(figsize=(10, 7))  # Set the figure size
plt.pie(
    visitors,
    labels=activities,
    autopct='%1.1f%%',  # Show percentages on the slices
    startangle=90,       # Start angle of the first slice
    colors=colors,       # Assign colors to slices
    shadow=True          # Add a shadow for a 3D effect
)

# Title of the pie chart
plt.title('Park Activities Popularity')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Display the pie chart
plt.show()