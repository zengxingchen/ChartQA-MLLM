
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
new_product_sales = [
    120, 110, 105, 100, 90, 80, 70, 65, 60, 55, 50, 45
]

# Create the plot
plt.figure(figsize=(12, 8))  # Change the size of the chart
plt.plot(months, new_product_sales, marker='o', color="#1F77B4", linewidth=2)  # Change color and add markers

# Annotations
for i, sales in enumerate(new_product_sales):
    plt.annotate(f"{sales}", (months[i], sales), textcoords="offset points", xytext=(0, 5),
                 ha='center', color="#D62728")

# Improve the visual appeal with labels, title, and grid
plt.xlabel('Month')
plt.ylabel('New Product Sales')
plt.title('Monthly New Product Sales Analysis', pad=20)
plt.grid(True)
plt.gca().invert_yaxis()  # Invert y-axis

# Show the plot
plt.show()