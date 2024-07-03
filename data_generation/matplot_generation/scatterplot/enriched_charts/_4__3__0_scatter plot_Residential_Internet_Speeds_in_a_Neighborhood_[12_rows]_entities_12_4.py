
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
average_daily_water_intake = [2.5, 2.8, 3.0, 3.5, 4.0, 4.2, 4.5, 4.7, 4.3, 3.8, 3.2, 2.7]
number_of_fruits_consumed = [3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4]

# Convert month names to numbers for plotting
month_numbers = [i+1 for i, _ in enumerate(months)]

# Scatter plot
plt.figure(figsize=(14, 7))  # Change the size of the plot
plt.scatter(month_numbers, average_daily_water_intake, 
            c=['#FF6347', '#4682B4', '#3CB371', '#FF1493',
               '#FFD700', '#ADFF2F', '#20B2AA', '#FF4500',
               '#9400D3', '#00BFFF', '#FF69B4', '#32CD32'],
            s=[fruit * 20 for fruit in number_of_fruits_consumed], alpha=0.7)  # Size corresponds to number of fruits consumed

# Customize the axes
plt.xticks(month_numbers, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Average Daily Water Intake (Liters)')
plt.title('Monthly Average Daily Water Intake vs. Number of Fruits Consumed')
plt.xlim(0, 13)  # Set the limit to include all months

# Show the plot
plt.tight_layout()  # Adjust layout to fit the figure neatly
plt.show()