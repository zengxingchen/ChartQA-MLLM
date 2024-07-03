
import matplotlib.pyplot as plt

# Data
months = ['2022-Jan', '2022-Feb', '2022-Mar', '2022-Apr', '2022-May', '2022-Jun', '2022-Jul', '2022-Aug', '2022-Sep', '2022-Oct', '2022-Nov', '2022-Dec']
visitor_count = [1800, 1750, 1600, 1500, 1400, 1300, 1250, 1100, 1050, 1000, 950, 900]

# Plotting the line chart
plt.figure(figsize=(14, 8))  # Adjusted width and height
plt.plot(months, visitor_count, color='#2ca02c', marker='o', linestyle='--', linewidth=2)  # Different color and marker style

# Annotate a specific point with the label
plt.annotate('Significant Drop', xy=('2022-Jul', 1250), xytext=('2022-Apr', 1600),
             arrowprops=dict(facecolor='#d62728', arrowstyle='->'))

# Adding a title and labels
plt.title('Monthly Visitor Count to National Parks in 2022', pad=20)  # Changed topic and added padding
plt.xlabel('Month')
plt.ylabel('Visitor Count')
plt.gca().invert_yaxis()  # Invert the y-axis

# Show the plot
plt.show()