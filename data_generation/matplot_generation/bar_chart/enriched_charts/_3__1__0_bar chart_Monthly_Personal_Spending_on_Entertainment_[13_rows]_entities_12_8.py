
import matplotlib.pyplot as plt

# Data points
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 
          'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 
          'Charlotte', 'Indianapolis', 'San Francisco', 'Seattle', 'Denver', 'Washington D.C.', 'Boston', 
          'El Paso', 'Nashville', 'Detroit', 'Portland', 'Las Vegas', 'Memphis', 'Baltimore', 'Milwaukee', 
          'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Kansas City', 'Atlanta', 'Miami', 'New Orleans', 
          'Tampa', 'Orlando', 'Cleveland']
population = [8419, 3980, 2716, 2320, 1680, 1584, 1547, 1426, 1344, 1031, 964, 902, 918, 890, 885, 876, 873, 
              744, 727, 712, 692, 682, 671, 670, 652, 644, 633, 602, 590, 563, 543, 542, 523, 508, 501, 
              486, 391, 394, 308, 383]

# Colors for each bar
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c4e17f', '#6d7fce', 
          '#ffb347', '#ffcc33', '#ffb7b2', '#ffdf80', '#b3b3cc', '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', 
          '#c2c2f0', '#ffb3e6', '#ff6666', '#c4e17f', '#6d7fce', '#ffb347', '#ffcc33', '#ffb7b2', '#ffdf80', 
          '#b3b3cc', '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c4e17f', 
          '#6d7fce', '#ffb347', '#ffcc33', '#ffb7b2']

# Create a horizontal bar chart
plt.figure(figsize=(16, 12))
plt.barh(cities, population, color=colors, height=0.5)

# Modify the ticks, labels, and title
plt.xlabel('Population (in thousands)')
plt.title('Population of Different Cities in the US')
plt.xticks(rotation=0)
plt.xlim(0, 9000)  # Adjusting the limit to fit the highest population value

# Display the plot
plt.tight_layout()
plt.show()