
import matplotlib.pyplot as plt

# Data points
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 
          'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Columbus', 
          'Indianapolis', 'Fort Worth', 'Charlotte', 'Seattle', 'Denver', 'Washington D.C.', 'Boston', 
          'El Paso', 'Nashville', 'Detroit', 'Portland', 'Las Vegas', 'Memphis', 'Baltimore', 'Milwaukee', 
          'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Kansas City', 'Atlanta', 'Miami', 'New Orleans', 
          'Tampa', 'Orlando', 'Cleveland']
rainfall = [75, 50, 85, 130, 25, 95, 110, 30, 105, 40, 120, 160, 55, 90, 100, 115, 140, 150, 60, 80, 70, 20, 145, 
            125, 135, 15, 155, 65, 45, 35, 28, 22, 48, 92, 138, 170, 200, 165, 175, 98]

# Colors for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', 
          '#17becf', '#1a55b2', '#f58230', '#3e9651', '#7b6888', '#6b486b', '#a05d56', '#d0743c', '#ffbb78', 
          '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5', '#1f78b4', 
          '#ff9896', '#8c564b', '#c7c7c7', '#17becf', '#9467bd', '#d62728', '#98df8a', '#ff7f0e', '#bcbd22', 
          '#f58230', '#3e9651', '#6b486b', '#ffbb78']

# Create a vertical bar chart
plt.figure(figsize=(14, 10))
plt.bar(cities, rainfall, color=colors, width=0.7)

# Modify the ticks, labels, and title
plt.ylabel('Average Rainfall (mm)')
plt.title('Average Monthly Rainfall in Different Cities')
plt.xticks(rotation=90)
plt.ylim(0, 220)  # Assuming the rainfall ranges between 0 and 220 mm

# Display the plot
plt.tight_layout()
plt.show()