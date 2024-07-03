
import matplotlib.pyplot as plt

# Table data represented as lists
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
          'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
          'Austin', 'Jacksonville', 'San Francisco', 'Indianapolis', 'Columbus',
          'Fort Worth', 'Charlotte', 'Detroit', 'El Paso', 'Seattle',
          'Denver', 'Washington D.C.', 'Boston', 'Nashville']
populations = [8.4, 4.0, 2.7, 2.3, 1.7, 1.6, 1.5, 1.4, 1.3, 1.0, 0.96, 0.92, 0.88,
               0.87, 0.85, 0.84, 0.82, 0.67, 0.68, 0.74, 0.73, 0.71, 0.69, 0.68]

# Custom color codes for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A6', '#33FFF6', '#F633FF', '#F6FF33',
          '#33A6FF', '#A6FF33', '#FF8C33', '#A6FF33', '#FF5733', '#33FF57', '#3357FF', '#57FF33',
          '#FF33A6', '#33FFF6', '#F633FF', '#F6FF33', '#33A6FF', '#A6FF33', '#FF8C33', '#A6FF33']

# Setting the size of the plot
plt.figure(figsize=(12, 10))

# Creating a vertical bar chart
plt.bar(cities, populations, color=colors, width=0.6)

# Customizing the plot
plt.ylabel('Population (Millions)')
plt.title('Population of Major US Cities')
plt.ylim(0.6, max(populations) + 0.5)  # Adjusting y-axis limits for truncation
plt.xticks(rotation=45, ha='right')  # Rotating x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Adding a grid for the y-axis

# Display the plot
plt.tight_layout()
plt.show()