
import matplotlib.pyplot as plt

# Data points
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
art_sales = [500, 550, 580, 600, 650, 670, 690, 700, 750, 800, 700, 800, 850, 900]

# Create figure and plot
fig, ax = plt.subplots(figsize=(10, 8))

# Change the color scheme using specific hex codes
ax.plot(years, art_sales, color='#FF6347', marker='o')

# Set the title and labels
ax.set_title('Annual Global Art Sales', fontsize=16, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Art Sales (millions)', fontsize=14)

# Adding annotations/labels
for (year, sale) in zip(years, art_sales):
    ax.annotate(f'{sale}M', xy=(year, sale), textcoords="offset points", xytext=(0,10), ha='center')

# Invert y-axis
ax.invert_yaxis()

plt.grid(True)
plt.show()