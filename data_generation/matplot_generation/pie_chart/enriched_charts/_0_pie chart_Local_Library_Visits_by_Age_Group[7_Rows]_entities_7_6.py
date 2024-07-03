
import matplotlib.pyplot as plt

# Data to plot
labels = ['Car', 'Public Transit', 'Bike', 'Walk', 'Work From Home', 
          'Motorcycle', 'Taxi', 'Ridesharing']
sizes = [52, 16, 5, 14, 8, 1, 2, 2]
colors = [
    '#FF9999', '#66B2FF', '#99FF99', '#FFCC99', 
    '#FFE5CC', '#FF6666', '#C2C2F0','#F0E68C']

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        startangle=140)

# Title
plt.title('City Commuting Methods')

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()