
import matplotlib.pyplot as plt

# Data points
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 
          'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Columbus', 
          'Indianapolis', 'Fort Worth', 'Charlotte', 'Seattle', 'Denver', 'Washington D.C.', 'Boston', 
          'El Paso', 'Nashville', 'Detroit', 'Portland', 'Las Vegas', 'Memphis', 'Baltimore', 'Milwaukee', 
          'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Kansas City', 'Atlanta', 'Miami', 'New Orleans', 
          'Tampa', 'Orlando', 'Cleveland']
population_growth_rate = [0.5, 1.2, 0.8, 1.5, 2.1, 0.7, 2.3, 1.0, 1.8, 1.3, 2.5, 1.7, 0.9, 1.4, 1.1, 1.9, 2.0, 
                          1.6, 1.4, 0.8, 0.6, 1.2, 2.2, 0.3, 1.5, 2.4, 0.9, 0.4, 0.7, 1.1, 1.0, 1.3, 1.8, 1.2, 2.1, 
                          1.0, 0.5, 1.4, 2.2, 0.3]

# Colors for each bar
colors = ['#a83232', '#327ba8', '#32a836', '#a89d32', '#a83291', '#32a891', '#9d32a8', '#3269a8', '#32a884', 
          '#a86932', '#32a86b', '#a83259', '#32a87a', '#8a32a8', '#a8328a', '#32a855', '#327aa8', '#a87632', 
          '#a83241', '#32a8b3', '#32a832', '#a83269', '#32a855', '#8a327a', '#a8328a', '#327ba8', '#32a876', 
          '#32a8b3', '#a86932', '#32a84e', '#8a32a8', '#a83259', '#32a832', '#327ba8', '#32a869', '#a83241', 
          '#32a855', '#8a327a', '#a83291', '#32a84e']

# Create a horizontal bar chart
plt.figure(figsize=(16, 12))
plt.barh(cities, population_growth_rate, color=colors, height=0.6)

# Modify the ticks, labels, and title
plt.xlabel('Population Growth Rate (%)')
plt.title('Population Growth Rate of Major US Cities', pad=20)
plt.xlim(0.2, 2.7)  # Set y-axis limits to start from a value other than zero

# Display the plot
plt.tight_layout()
plt.show()