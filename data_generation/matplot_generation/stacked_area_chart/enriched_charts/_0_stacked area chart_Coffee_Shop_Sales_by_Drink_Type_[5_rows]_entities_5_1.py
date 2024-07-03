
import matplotlib.pyplot as plt

# Table data represented as lists
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
electronics = [12000, 15000, 18000, 20000, 22000, 25000, 27000, 30000, 28000, 26000, 24000, 23000]
clothing = [5000, 5500, 6000, 6500, 7000, 7200, 7500, 7700, 8000, 8500, 9000, 9500]
home_decor = [8000, 7500, 9000, 9500, 10000, 11000, 11500, 12000, 12500, 10500, 10000, 9500]
books = [3000, 3200, 3400, 3700, 4000, 4500, 4700, 5000, 5300, 5500, 5800, 6000]

# Create a stacked area chart
plt.figure(figsize=(12, 6))  # Change width and height of the chart
plt.stackplot(months, electronics, clothing, home_decor, books, 
              colors=['#1E90FF', '#3CB371', '#FFD700', '#FF6347'])  # Modify the color scheme

# Add title and labels
plt.title('Monthly Sales Data by Product Category', fontdict={'fontsize': 15})
plt.xlabel('Month')
plt.ylabel('Sales (in USD)')

# Assign annotation/text label on the chart for the peak of Electronics
peak_sales_month = months[electronics.index(max(electronics))]
peak_sales_value = max(electronics)
plt.text(peak_sales_month, peak_sales_value, 'Peak for Electronics', ha='center', va='top')

# Display the chart
plt.show()