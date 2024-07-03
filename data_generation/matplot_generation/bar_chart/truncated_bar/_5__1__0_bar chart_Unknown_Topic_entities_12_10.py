
import matplotlib.pyplot as plt

# Table data represented as lists
topics = ['Ancient History', 'Medieval History', 'Renaissance', 'Industrial Revolution', 'Modern History',
          'World War I', 'World War II', 'Cold War', 'Contemporary History', 'Future History', 'History of Science', 'Cultural History']
interest_levels = [70, 65, 80, 90, 95, 85, 100, 75, 60, 50, 55, 65]

# Custom color codes for each bar
colors = ['#8B0000', '#FF4500', '#FF6347', '#FFD700', '#ADFF2F', 
          '#32CD32', '#00FA9A', '#00CED1', '#4682B4', '#1E90FF',
          '#8A2BE2', '#D2691E']

# Setting the size of the plot
plt.figure(figsize=(14, 8))

# Creating a horizontal bar chart
plt.barh(topics, interest_levels, color=colors, height=0.5)

# Customizing the plot
plt.xlabel('Interest Level (out of 100)')
plt.title('Interest Levels in Different History Topics')
plt.xlim(40, max(interest_levels) + 10)  # Adjusting x-axis limits for better clarity
plt.grid(axis='x', linestyle='--', alpha=0.7)  # Adding a grid for the x-axis

# Display the plot
plt.show()