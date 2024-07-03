
import matplotlib.pyplot as plt

# Table data represented as lists
topics = ['Artificial Intelligence', 'Quantum Computing', 'Blockchain Technology', 'Augmented Reality', 
          '5G Networks', 'Cybersecurity', 'Renewable Energy', 'Biotechnology', 
          'Autonomous Vehicles', 'Robotics', 'Nanotechnology', 'Space Exploration']
values = [75, 50, 60, 45, 70, 65, 55, 48, 72, 62, 58, 68]

# Custom color codes for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6', '#33FFF6', '#F633FF', '#F6FF33', 
          '#33A6FF', '#A6FF33', '#FF8C33', '#A6FF33']

# Setting the size of the plot
plt.figure(figsize=(12, 10))

# Creating a vertical bar chart
plt.bar(topics, values, color=colors, width=0.6)

# Customizing the plot
plt.ylabel('Significance Score')
plt.title('Significance of Future Technologies')
plt.ylim(40, max(values) + 10)  # Adjusting y-axis limits for better clarity
plt.xticks(rotation=45, ha='right')  # Rotating x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Adding a grid for the y-axis

# Display the plot
plt.tight_layout()  # Adjust layout to make room for rotated labels
plt.show()