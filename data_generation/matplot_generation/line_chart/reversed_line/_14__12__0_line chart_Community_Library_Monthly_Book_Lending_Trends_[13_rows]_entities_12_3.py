
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
avg_monthly_sales = [
    2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200
]

# Create the plot
plt.figure(figsize=(12, 6))  # Change the size of the chart
plt.plot(months, avg_monthly_sales, marker='o', color="#FF5733", linewidth=2)  # Change color and add circle markers

# Annotations
for i, sales in enumerate(avg_monthly_sales):
    plt.annotate(sales, (months[i], sales), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#2E86C1")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Month')
plt.ylabel('Average Monthly Sales')
plt.title('Average Monthly Sales Over a Year', pad=20)
plt.grid(True)
plt.gca().invert_yaxis()

# Show the plot
plt.show()