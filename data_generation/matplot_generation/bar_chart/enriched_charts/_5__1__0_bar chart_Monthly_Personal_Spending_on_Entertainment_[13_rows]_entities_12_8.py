
import matplotlib.pyplot as plt

# Data points
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 
          'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Columbus', 
          'Indianapolis', 'Fort Worth', 'Charlotte', 'Seattle', 'Denver', 'Washington D.C.', 'Boston', 
          'El Paso', 'Nashville', 'Detroit', 'Portland', 'Las Vegas', 'Memphis', 'Baltimore', 'Milwaukee', 
          'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Kansas City', 'Atlanta', 'Miami', 'New Orleans', 
          'Tampa', 'Orlando', 'Cleveland']
meteor_showers = [5, 12, 7, 15, 3, 9, 10, 4, 11, 6, 13, 17, 8, 14, 7, 16, 14, 13, 12, 9, 8, 3, 14, 
                  11, 15, 2, 16, 10, 6, 5, 4, 5, 6, 12, 15, 18, 20, 17, 19, 11]

# Colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#57FF33', '#5733FF', '#FF5733', '#33FFA1', '#FF3357', 
          '#A133FF', '#33A1FF', '#FF57A1', '#A157FF', '#33FF57', '#57A1FF', '#FF3357', '#A133FF', '#33FF57', 
          '#FF33A1', '#57A1FF', '#5733FF', '#FF5733', '#33FF57', '#FF3357', '#A157FF', '#33FFA1', '#FF33A1', 
          '#5733FF', '#FF5733', '#33FF57', '#57A1FF', '#FF3357', '#A133FF', '#33FF57', '#FF33A1', '#57FF33', 
          '#5733FF', '#FF5733', '#33FFA1', '#FF3357']

# Create a horizontal bar chart
plt.figure(figsize=(12, 18))
plt.barh(cities, meteor_showers, color=colors, height=0.5)

# Modify the ticks, labels, and title
plt.xlabel('Average Monthly Meteor Showers')
plt.title('Average Monthly Meteor Showers in Different Cities')
plt.yticks(rotation=0)
plt.xlim(0, 25)  # Assuming the meteor showers range between 0 and 25

# Display the plot
plt.tight_layout()
plt.show()