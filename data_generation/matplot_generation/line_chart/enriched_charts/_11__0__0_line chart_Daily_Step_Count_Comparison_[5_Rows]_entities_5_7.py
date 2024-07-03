
import matplotlib.pyplot as plt

# Data
months = ['2022-Jan', '2022-Feb', '2022-Mar', '2022-Apr', '2022-May', '2022-Jun', '2022-Jul', '2022-Aug', '2022-Sep', '2022-Oct', '2022-Nov', '2022-Dec']
revenue = [3200, 3400, 3600, 3800, 3900, 4200, 4100, 4300, 4500, 4700, 4600, 4800]

# Plotting the line chart
plt.figure(figsize=(14, 7))  # Adjusted width and height
plt.plot(months, revenue, color='#FF5733', marker='o', linestyle='--', linewidth=2)  # Different color and marker style

# Annotate a specific point with the label
plt.annotate('Revenue Drop', xy=('2022-Jul', 4100), xytext=('2022-Apr', 3800),
             arrowprops=dict(facecolor='#2ECC71', arrowstyle='->'))

# Adding a title and labels
plt.title('Monthly Revenue of E-Commerce Store in 2022', pad=20)  # Changed topic and added padding
plt.xlabel('Month')
plt.ylabel('Revenue (in USD)')

# Show the plot
plt.show()