
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
water_intake = [2000, 2100, 1950, 2050, 2200, 2300, 2150, 2250, 2100, 1950, 2000, 2100]

plt.figure(figsize=(16, 10))  # Adjust width and height of the chart
plt.plot(months, water_intake, marker='o', linestyle='-', color='#e74c3c')  # Specific hex color

# Annotation for the highest water intake
plt.annotate('Peak Water Intake', xy=('June', 2300), xytext=('August', 2400),
             arrowprops=dict(facecolor='#2ecc71', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Average Daily Water Intake (ml)')
plt.title('Average Daily Water Intake in 2023', pad=20)

# Showing the plot
plt.show()