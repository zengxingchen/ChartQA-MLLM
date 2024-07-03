
import matplotlib.pyplot as plt

# Table data represented as lists
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
walking = [15000, 16000, 18000, 20000, 22000, 25000, 27000, 29000, 31000, 32000, 33000, 34000]
running = [3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500]
cycling = [12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000]
swimming = [5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200]

# Create a stacked area chart
plt.figure(figsize=(14, 8))  # Change width and height of the chart
plt.stackplot(months, walking, running, cycling, swimming, 
              colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A8'])  # Modify the color scheme

# Add title and labels
plt.title('Monthly Step Count by Activity Type', fontdict={'fontsize': 18})
plt.xlabel('Month')
plt.ylabel('Steps Counted')

# Add legend
plt.legend(['Walking', 'Running', 'Cycling', 'Swimming'], loc='upper left')

# Assign annotation/text label on the chart for the peak of Walking
peak_steps_month = months[walking.index(max(walking))]
peak_steps_value = max(walking)
plt.text(peak_steps_month, peak_steps_value, 'Peak for Walking', ha='center', va='bottom')

# Display the chart
plt.show()