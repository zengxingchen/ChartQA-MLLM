
import matplotlib.pyplot as plt

# Data for each year
years = list(range(2010, 2024))
clothing = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115]
accessories = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
footwear = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
beauty_products = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# Creating a stacked area chart
plt.figure(figsize=(16, 9))
plt.stackplot(years, clothing, accessories, footwear, beauty_products, 
              colors=['#FF4500', '#32CD32', '#1E90FF', '#FFD700'])

# Adding labels and title
plt.title('Fashion Product Sales Trends (2010-2023)', fontsize=20, pad=30)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Sales (in millions)', fontsize=14)

# Adding a legend
plt.legend(['Clothing', 'Accessories', 'Footwear', 'Beauty Products'], loc='upper left')

# Annotating the last data point for Footwear
plt.annotate(f'{footwear[-1]}M Sales',
             (years[-1], sum([clothing[-1], accessories[-1], footwear[-1], beauty_products[-1]])),
             textcoords="offset points",
             xytext=(-20,10),
             ha='center',
             fontsize=12,
             color='#1E90FF')

plt.show()