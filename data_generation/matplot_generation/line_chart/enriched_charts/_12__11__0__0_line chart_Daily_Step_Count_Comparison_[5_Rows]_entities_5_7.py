
import matplotlib.pyplot as plt

# Data
months = ['2022-Jan', '2022-Feb', '2022-Mar', '2022-Apr', '2022-May', '2022-Jun', '2022-Jul', '2022-Aug', '2022-Sep', '2022-Oct', '2022-Nov', '2022-Dec']
visitors = [1500, 1400, 1800, 1600, 2100, 2300, 2500, 2600, 2400, 2200, 2000, 1800]

# Plotting the line chart
plt.figure(figsize=(16, 8))  # Adjusted width and height
plt.plot(months, visitors, color='#1E90FF', marker='s', linestyle='-.', linewidth=2)  # Different color and marker style

# Annotate a specific point with the label
plt.annotate('Peak Season', xy=('2022-Jul', 2500), xytext=('2022-Apr', 1600),
             arrowprops=dict(facecolor='#FF6347', arrowstyle='->'))

# Adding a title and labels
plt.title('Monthly Visitors to a National Park in 2022', pad=20)  # Changed topic and added padding
plt.xlabel('Month')
plt.ylabel('Number of Visitors')

# Show the plot
plt.show()