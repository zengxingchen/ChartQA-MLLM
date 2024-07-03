
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
training_hours = [20, 25, 30, 35, 40, 45, 50, 55, 50, 45, 30, 25]
performance_score = [55, 60, 70, 80, 90, 100, 110, 105, 95, 85, 65, 60]

# Convert month names to numbers for plotting
month_numbers = [i+1 for i, _ in enumerate(months)]

# Scatter plot
plt.figure(figsize=(12, 6))  # Change the size of the plot
plt.scatter(month_numbers, training_hours, c=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                                              '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                                              '#bcbd22', '#17becf', '#aec7e8', '#ffbb78'],
            s=performance_score, alpha=0.6)  # Size corresponds to performance score, improved color scheme

# Customize the axes
plt.xticks(month_numbers, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Training Hours')
plt.title('Training Hours vs Performance Score Per Month', pad=20)
plt.xlim(0, 13)  # Set the limit to include all months

# Show the plot
plt.tight_layout()  # Adjust layout to fit the figure neatly
plt.show()