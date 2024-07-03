
import matplotlib.pyplot as plt

# Data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
book_sales = [120000, 150000, 180000, 220000, 250000, 270000, 300000, 330000, 360000, 390000, 410000]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))  # changing width and height

# Plotting the area chart
ax.fill_between(years, book_sales, color="#4b0082", alpha=0.5, label='Book Sales')

# Titles and labels
ax.set_title('Book Sales Over the Years', fontsize=18, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Books Sold', fontsize=14)

# Customizing the y-axis to get a better understanding of scales
ax.set_yscale('linear')

# Legend
ax.legend(loc='upper right')

# Annotation
for i, txt in enumerate(book_sales):
    ax.annotate(txt, (years[i], book_sales[i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.show()