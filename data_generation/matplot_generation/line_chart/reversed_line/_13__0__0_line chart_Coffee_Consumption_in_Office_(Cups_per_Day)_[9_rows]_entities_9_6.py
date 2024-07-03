
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
research_budget = [85, 100, 95, 110, 120, 140, 155, 150, 145, 160, 170, 175]

plt.figure(figsize=(14, 8))  # Adjust width and height of the chart
plt.plot(months, research_budget, marker='o', linestyle='-', color='#3498db')  # Specific hex color

# Annotation for the highest research budget
plt.annotate('Peak Research Budget', xy=('December', 175), xytext=('October', 190),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Research Budget (Million $)')
plt.title('Monthly Research Budget in 2023')

# Showing the plot
plt.show()