
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
screen_time = [3.5, 3.8, 4.0, 4.2, 4.1, 4.3, 4.5, 4.4, 4.6, 4.8, 5.0, 5.2]

# Create the plot
plt.figure(figsize=(14, 7))
plt.plot(months, screen_time, marker='o', linestyle='-', color='#1E90FF')

# Annotate the highest and lowest screen time points
plt.annotate('Highest\n5.2 hrs/day', xy=('December', 5.2), xytext=('November', 4.9),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')
plt.annotate('Lowest\n3.5 hrs/day', xy=('January', 3.5), xytext=('February', 3.3),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')

# Title and labels
plt.title('Monthly Average Screen Time of Teenagers (hours/day)', pad=20)
plt.xlabel('Month')
plt.ylabel('Average Screen Time (hours/day)')
plt.gca().invert_yaxis()

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()