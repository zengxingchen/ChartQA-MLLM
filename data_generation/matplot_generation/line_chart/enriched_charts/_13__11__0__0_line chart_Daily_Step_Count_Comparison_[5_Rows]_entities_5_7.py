
import matplotlib.pyplot as plt

# Data
months = ['2022-Jan', '2022-Feb', '2022-Mar', '2022-Apr', '2022-May', '2022-Jun', '2022-Jul', '2022-Aug', '2022-Sep', '2022-Oct', '2022-Nov', '2022-Dec']
visitors = [4800, 4600, 4700, 4500, 4300, 4200, 4100, 3900, 3800, 3600, 3400, 3200]

# Plotting the line chart
plt.figure(figsize=(12, 6))
plt.plot(months, visitors, color='#2E86C1', marker='s', linestyle='-', linewidth=2)

# Annotate a specific point with the label
plt.annotate('Visitor Drop', xy=('2022-Aug', 3900), xytext=('2022-May', 4300),
             arrowprops=dict(facecolor='#E74C3C', arrowstyle='->'))

# Adding a title and labels
plt.title('Monthly Visitors of E-Commerce Store in 2022', pad=20)
plt.xlabel('Month')
plt.ylabel('Visitors')

# Show the plot
plt.gca().invert_yaxis()  # Invert the y-axis
plt.show()