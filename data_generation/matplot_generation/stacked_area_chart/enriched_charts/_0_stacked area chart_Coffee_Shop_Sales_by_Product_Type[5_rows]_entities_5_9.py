
import matplotlib.pyplot as plt

# Table data of monthly sales for Software, Hardware, and Accessories
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
software_sales = [12000, 18000, 21000, 23000, 25000, 27000, 30000, 28000, 26000, 27000, 29000, 31000]
hardware_sales = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 21000, 22000, 23000, 24000, 25000]
accessories_sales = [8000, 9500, 10500, 12000, 13000, 14000, 15000, 16500, 17000, 17500, 18000, 19000]

# Stacked area chart
plt.figure(figsize=(12, 8))
plt.stackplot(months, software_sales, hardware_sales, accessories_sales, 
              labels=['Software', 'Hardware', 'Accessories'],
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Customizing the plot with titles, labels and annotations
plt.title('Monthly Sales Data for XYZ Corporation')
plt.xlabel('Month')
plt.ylabel('Sales (USD)')
plt.legend(loc='upper left')
plt.xticks(rotation=45)

# Annotation example
peak_software_sales = max(software_sales)
peak_month = months[software_sales.index(peak_software_sales)]
plt.annotate(f'Peak Software Sales\n{peak_software_sales} USD',
             xy=(peak_month, peak_software_sales),
             xytext=(peak_month, peak_software_sales + 5000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.tight_layout()
plt.show()