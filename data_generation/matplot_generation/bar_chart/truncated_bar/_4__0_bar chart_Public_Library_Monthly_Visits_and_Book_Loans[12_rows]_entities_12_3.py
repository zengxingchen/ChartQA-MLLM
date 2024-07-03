
import matplotlib.pyplot as plt

# Data from the table above
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
          'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 
          'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte',
          'Indianapolis', 'San Francisco', 'Seattle', 'Denver', 'Washington']
weekly_workout_hours = [4.5, 5.2, 3.9, 6.1, 5.8, 4.7, 6.3, 5.0, 6.0, 4.8, 
                        5.5, 6.2, 5.9, 4.4, 5.1, 5.6, 5.7, 4.9, 6.4, 4.6]

# Setting colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357', 
          '#A1D6E2', '#1995AD', '#BCBABE', '#766F64', '#8BB8B8',
          '#3B9C9C', '#5D4C46', '#778C85', '#D1B499', '#A2885F',
          '#FF9966', '#66FF99', '#9966FF', '#FF6699']

# Increase the width and height of the chart
plt.figure(figsize=(14, 10))

# Change the direction of the chart to vertical and modify the bar width
plt.bar(cities, weekly_workout_hours, color=colors, width=0.6)

# Setting y-axis limits to truncate the bar chart
plt.ylim(3.5, 7)

# Customizing the chart with titles and labels
plt.ylabel('Average Weekly Workout Hours')
plt.title('Average Weekly Workout Hours Across Various U.S. Cities')
plt.xticks(rotation=45, ha='right')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Display the bar chart
plt.tight_layout()
plt.show()