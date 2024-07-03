
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
box_office = np.array([50, 45, 60, 55, 70, 65, 80, 75, 60, 70, 80, 90])
digital_sales = np.array([30, 35, 40, 45, 50, 45, 55, 50, 40, 50, 60, 70])
physical_sales = np.array([10, 15, 20, 15, 30, 25, 35, 30, 20, 25, 35, 40])
streaming = np.array([10, 5, 10, 5, 20, 15, 25, 20, 10, 15, 25, 30])

# Convert to percentages
total = box_office + digital_sales + physical_sales + streaming
box_office_percentage = box_office / total
digital_sales_percentage = digital_sales / total
physical_sales_percentage = physical_sales / total
streaming_percentage = streaming / total

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

width = 0.4
ax.bar(months, box_office_percentage, color='#FFA07A', edgecolor='white', width=width, label='Box Office Revenue')
ax.bar(months, digital_sales_percentage, color='#20B2AA', edgecolor='white', width=width, bottom=box_office_percentage, label='Digital Sales')
ax.bar(months, physical_sales_percentage, color='#778899', edgecolor='white', width=width, bottom=box_office_percentage + digital_sales_percentage, label='Physical Sales')
ax.bar(months, streaming_percentage, color='#9370DB', edgecolor='white', width=width, bottom=box_office_percentage + digital_sales_percentage + physical_sales_percentage, label='Streaming')

ax.set_ylabel('Percentage')
ax.set_title('Monthly Entertainment Revenue Distribution', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1, 0.5))

plt.show()