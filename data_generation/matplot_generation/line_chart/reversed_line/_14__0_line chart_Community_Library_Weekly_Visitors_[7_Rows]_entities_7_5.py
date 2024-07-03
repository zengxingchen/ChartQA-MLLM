
import matplotlib.pyplot as plt

# Define the data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
population = [8000000, 8050000, 8100000, 8150000, 8200000, 8250000, 8300000, 
              8350000, 8400000, 8450000, 8500000, 8550000]

# Create the line chart
plt.figure(figsize=(12, 6))  # Changed width and height of the chart
plt.plot(months, population, color='#3498DB', marker='o')  # Changed color scheme and added markers

# Customize the trend of the data by simulating a sudden population drop in July
population[6] = 8200000
plt.plot(months, population, linestyle='--', color='#E74C3C')  # Overlaying the modified trend line

# Assign annotation to the chart
for i, pop in enumerate(population):
    plt.annotate(f"{pop}", (months[i], population[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Monthly Population in NYC (Simulating July Population Drop)')
plt.xlabel('Month')
plt.ylabel('Population')
plt.gca().invert_yaxis()  # Invert y-axis
plt.grid(True)

# Display the plot
plt.show()