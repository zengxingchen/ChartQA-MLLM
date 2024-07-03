
import matplotlib.pyplot as plt

# Data from the table provided
years = ['2015','2016','2017','2018','2019','2020','2021', '2022', '2023', '2024']
sales = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240]
marketing = [120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
development = [80, 85, 90, 95, 100, 110, 120, 130, 140, 150]
support = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# Stacking data
marketing_bottom = [sales[i] for i in range(len(sales))]
development_bottom = [marketing_bottom[i] + marketing[i] for i in range(len(marketing))]
support_bottom = [development_bottom[i] + development[i] for i in range(len(development))]

# Setting figure size
plt.figure(figsize=(12, 10))

# Plotting data
bar_width = 0.5
plt.bar(years, sales, width=bar_width, color='#3498db', edgecolor='white', label='Sales')
plt.bar(years, marketing, bottom=sales, width=bar_width, color='#2ecc71', edgecolor='white', label='Marketing')
plt.bar(years, development, bottom=marketing_bottom, width=bar_width, color='#e74c3c', edgecolor='white', label='Development')
plt.bar(years, support, bottom=development_bottom, width=bar_width, color='#f1c40f', edgecolor='white', label='Support')

# Adding numerical labels
for i in range(len(years)):
    plt.text(i, sales[i] / 2, str(sales[i]), ha='center', va='center', color='white')
    plt.text(i, sales[i] + marketing[i] / 2, str(marketing[i]), ha='center', va='center', color='white')
    plt.text(i, sales[i] + marketing[i] + development[i] / 2, str(development[i]), ha='center', va='center', color='white')
    plt.text(i, sales[i] + marketing[i] + development[i] + support[i] / 2, str(support[i]), ha='center', va='center', color='white')

# Adding titles and labels
plt.ylabel('Annual Revenue (in millions)')
plt.xlabel('Year')
plt.title('Annual Revenue by Department over Years', pad=20)
plt.legend(loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()