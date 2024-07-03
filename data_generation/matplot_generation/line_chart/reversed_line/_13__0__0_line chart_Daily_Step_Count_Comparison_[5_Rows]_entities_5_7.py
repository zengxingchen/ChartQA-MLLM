
import matplotlib.pyplot as plt

# Data
months = ['2022-Jan', '2022-Feb', '2022-Mar', '2022-Apr', '2022-May', '2022-Jun', '2022-Jul', '2022-Aug', '2022-Sep', '2022-Oct', '2022-Nov', '2022-Dec']
visitor_count = [2000, 2200, 2100, 2500, 2300, 2400, 2600, 2700, 2300, 2200, 2100, 2000]

# Plotting the line chart
plt.figure(figsize=(14, 8))  # Adjusted width and height
plt.plot(months, visitor_count, color='#2ca02c', marker='o', linestyle='-', linewidth=2)  # Different color and marker style

# Annotate a specific point with the label
plt.annotate('Highest Visitors', xy=('2022-Aug', 2700), xytext=('2022-May', 2300),
             arrowprops=dict(facecolor='#d62728', arrowstyle='->'))

# Adding a title and labels
plt.title('Monthly Visitor Count to Historical Sites in 2022', pad=20)  # Changed topic and added padding
plt.xlabel('Month')
plt.ylabel('Visitor Count')

# Show the plot
plt.show()