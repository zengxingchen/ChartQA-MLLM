
import matplotlib.pyplot as plt

# Data
months = ['2022-Jan', '2022-Feb', '2022-Mar', '2022-Apr', '2022-May', '2022-Jun', '2022-Jul', '2022-Aug', '2022-Sep', '2022-Oct', '2022-Nov', '2022-Dec']
visitor_count = [500, 600, 700, 1200, 1500, 1800, 2200, 2000, 1700, 1600, 1100, 900]

# Plotting the line chart
plt.figure(figsize=(12, 6))  # Adjusted width and height
plt.plot(months, visitor_count, color='#1f77b4', marker='s', linestyle='-', linewidth=2)  # Different color and marker style

# Annotate a specific point with the label
plt.annotate('Peak Season', xy=('2022-Jul', 2200), xytext=('2022-May', 1800),
             arrowprops=dict(facecolor='#ff0000', arrowstyle='->'))

# Adding a title and labels
plt.title('Monthly Visitor Count to National Parks in 2022', pad=20)  # Changed topic and added padding
plt.xlabel('Month')
plt.ylabel('Visitor Count')

# Show the plot
plt.show()