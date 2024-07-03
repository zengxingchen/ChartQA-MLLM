
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
visitors = [1500, 1600, 1750, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600]
revenue = [8000, 8200, 8600, 8700, 8800, 9000, 9200, 9300, 9400, 9500, 9600, 9700]
complaints = [15, 18, 10, 12, 9, 14, 13, 11, 17, 16, 19, 20]
new_subscriptions = [500, 520, 600, 610, 620, 650, 680, 700, 710, 730, 740, 750]

# Stacked Bar Chart
plt.figure(figsize=(16, 10))  # Change width and height of the chart
bar_width = 0.4  # Change width of bars

# Creating a vertical bar chart
plt.bar(months, visitors, color='#FF6347', edgecolor='white', width=bar_width, label='Visitors')
plt.bar(months, revenue, bottom=visitors, color='#4682B4', edgecolor='white', width=bar_width, label='Revenue')
plt.bar(months, complaints, bottom=[i+j for i,j in zip(visitors, revenue)], color='#3CB371', edgecolor='white', width=bar_width, label='Complaints')
plt.bar(months, new_subscriptions, bottom=[i+j+k for i,j,k in zip(visitors, revenue, complaints)], color='#FFD700', edgecolor='white', width=bar_width, label='New Subscriptions')

plt.ylabel('Metrics')  # Change to appropriate label
plt.title('Monthly Website Performance Metrics', pad=20)  # Change the headline
plt.xticks(rotation=45)  # Appropriately adjusting for vertical chart
plt.legend(loc='upper left')

# Display the plot
plt.show()