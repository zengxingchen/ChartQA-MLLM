
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
steps = [8000, 7500, 8200, 8700, 9000, 9500, 10000, 9700, 9300, 8800, 8500, 8200]

plt.figure(figsize=(14, 8))  # Adjust width and height of the chart
plt.plot(months, steps, marker='o', linestyle='-', color='#3498db')  # Specific hex color

# Annotation for the highest step count
plt.annotate('Peak Step Count', xy=('July', 10000), xytext=('September', 10500),
             arrowprops=dict(facecolor='#2ecc71', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Average Daily Step Count')
plt.title('Average Daily Step Count in 2023', pad=20)

# Showing the plot
plt.show()