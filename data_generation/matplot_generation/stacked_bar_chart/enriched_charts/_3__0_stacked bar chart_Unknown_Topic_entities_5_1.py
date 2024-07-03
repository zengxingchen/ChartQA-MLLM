
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
marketing = [120, 130, 140, 125, 135, 145, 150, 155, 160, 165, 170, 175]
sales = [150, 170, 160, 180, 175, 165, 180, 190, 185, 195, 200, 205]
it = [200, 190, 210, 220, 215, 225, 230, 235, 240, 245, 250, 255]
hr = [90, 80, 85, 95, 100, 110, 105, 115, 120, 125, 130, 135]

# Stacked Bar Chart
plt.figure(figsize=(12, 10))  # Change width and height of the chart
bar_width = 0.6  # Change width of bars

# Creating a vertical bar chart
plt.bar(months, marketing, color='#4CAF50', edgecolor='white', width=bar_width, label='Marketing')
plt.bar(months, sales, bottom=marketing, color='#2196F3', edgecolor='white', width=bar_width, label='Sales')
plt.bar(months, it, bottom=[i+j for i,j in zip(marketing, sales)], color='#FFC107', edgecolor='white', width=bar_width, label='IT')
plt.bar(months, hr, bottom=[i+j+k for i,j,k in zip(marketing, sales, it)], color='#F44336', edgecolor='white', width=bar_width, label='HR')

plt.ylabel('Revenue in $1000s')
plt.title('Monthly Revenue by Department')
plt.xticks(rotation=45)
plt.legend(loc='upper left')

# Adding numerical labels to each bar segment
for i in range(len(months)):
    plt.text(i, marketing[i]/2, str(marketing[i]), ha='center', va='center', color='white')
    plt.text(i, marketing[i] + sales[i]/2, str(sales[i]), ha='center', va='center', color='white')
    plt.text(i, marketing[i] + sales[i] + it[i]/2, str(it[i]), ha='center', va='center', color='white')
    plt.text(i, marketing[i] + sales[i] + it[i] + hr[i]/2, str(hr[i]), ha='center', va='center', color='white')

# Display the plot
plt.show()