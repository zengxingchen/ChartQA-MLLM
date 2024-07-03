import matplotlib.pyplot as plt

# Data
years = range(2010, 2025)
annual_book_sales = [1500, 1600, 1750, 1900, 2100, 2300, 2600, 2900, 3200, 3500, 3800, 4100, 4500, 4900, 5300]

# Plot
fig, ax = plt.subplots(figsize=(16, 8))

# Plotting the area chart
ax.fill_between(years, annual_book_sales, color="#1E90FF", alpha=0.7, label='Annual Book Sales')

# Titles and labels
ax.set_title('Annual Book Sales from 2010 to 2024', fontsize=20, pad=20)
ax.set_xlabel('Year', fontsize=15)
ax.set_ylabel('Number of Sales', fontsize=15)

# Customizing the y-axis to get a better understanding of scales
ax.set_yscale('linear')

# Annotation
for i, txt in enumerate(annual_book_sales):
    ax.annotate(txt, (years[i], annual_book_sales[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Legend
ax.legend(loc='upper left')

plt.show()