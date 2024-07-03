
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
visitors = [1500, 1600, 1750, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600]
revenue = [8000, 8200, 8600, 8700, 8800, 9000, 9200, 9300, 9400, 9500, 9600, 9700]
complaints = [15, 18, 10, 12, 9, 14, 13, 11, 17, 16, 19, 20]
new_subscriptions = [500, 520, 600, 610, 620, 650, 680, 700, 710, 730, 740, 750]

# Stacked Bar Chart
plt.figure(figsize=(12, 8))  # Change width and height of the chart
bar_height = 0.6  # Change height of bars

# Creating a horizontal bar chart
plt.barh(months, visitors, color='#FF4500', edgecolor='white', height=bar_height, label='Visitors')
plt.barh(months, revenue, left=visitors, color='#1E90FF', edgecolor='white', height=bar_height, label='Revenue')
plt.barh(months, complaints, left=[i+j for i,j in zip(visitors, revenue)], color='#32CD32', edgecolor='white', height=bar_height, label='Complaints')
plt.barh(months, new_subscriptions, left=[i+j+k for i,j,k in zip(visitors, revenue, complaints)], color='#FFD700', edgecolor='white', height=bar_height, label='New Subscriptions')

# Adding numerical labels to each bar segment
for i, month in enumerate(months):
    plt.text(visitors[i] / 2, i, str(visitors[i]), ha='center', va='center', color='white', weight='bold')
    plt.text(visitors[i] + revenue[i] / 2, i, str(revenue[i]), ha='center', va='center', color='white', weight='bold')
    plt.text(visitors[i] + revenue[i] + complaints[i] / 2, i, str(complaints[i]), ha='center', va='center', color='white', weight='bold')
    plt.text(visitors[i] + revenue[i] + complaints[i] + new_subscriptions[i] / 2, i, str(new_subscriptions[i]), ha='center', va='center', color='white', weight='bold')

plt.xlabel('Metrics')  # Change to appropriate label
plt.title('Monthly Website Performance Metrics', pad=20)  # Change the headline
plt.yticks(rotation=0)  # Appropriately adjusting for horizontal chart
plt.legend(loc='lower right')

# Display the plot
plt.show()