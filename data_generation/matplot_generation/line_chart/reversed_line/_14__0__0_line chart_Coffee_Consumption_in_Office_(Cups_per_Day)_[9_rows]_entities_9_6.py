import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
viewership = [105, 90, 80, 150, 200, 220, 240, 230, 210, 190, 170, 160]

plt.figure(figsize=(14, 8))  # Adjust width and height of the chart
plt.plot(months, viewership, marker='o', linestyle='-', color='#3498db')  # Specific hex color

# Annotation for the highest viewership
plt.annotate('Peak Viewership', xy=('July', 240), xytext=('September', 250),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Average Monthly Viewership (millions)')
plt.title('Average Monthly TV Show Viewership in 2023')

# Invert y-axis
plt.gca().invert_yaxis()

# Showing the plot
plt.show()