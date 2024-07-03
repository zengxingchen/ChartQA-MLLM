
import matplotlib.pyplot as plt

# Table data represented as lists
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
technology = [1500, 1700, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800]
healthcare = [1200, 1300, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200]
finance = [1800, 2000, 2100, 2400, 2500, 2700, 2900, 3100, 3300, 3500, 3700, 3900]
energy = [1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200]

# Create a stacked area chart
plt.figure(figsize=(16, 9))  # Change width and height of the chart
plt.stackplot(months, technology, healthcare, finance, energy, 
              colors=['#1E88E5', '#D81B60', '#FFC107', '#004D40'])  # Modify the color scheme

# Add title and labels
plt.title('Monthly Stock Prices by Sector', fontdict={'fontsize': 18}, loc='center')
plt.xlabel('Month')
plt.ylabel('Stock Prices')

# Add legend
plt.legend(['Technology', 'Healthcare', 'Finance', 'Energy'], loc='upper left')

# Assign annotation/text label on the chart for the peak of Finance
peak_papers_month = months[finance.index(max(finance))]
peak_papers_value = max(finance)
plt.text(peak_papers_month, peak_papers_value, 'Peak for Finance', ha='center', va='top')

# Display the chart
plt.show()