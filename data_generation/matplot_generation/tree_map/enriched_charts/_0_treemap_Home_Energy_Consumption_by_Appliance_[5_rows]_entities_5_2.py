
import matplotlib.pyplot as plt
import squarify

# Dataset
brands = ['Toyota', 'Volkswagen', 'Ford', 'Honda', 'Chevrolet', 'Mercedes-Benz', 'BMW', 'Porsche', 'Ferrari', 'Tesla', 'Lexus', 'Audi', 'Hyundai', 'Kia', 'Renault', 'Peugeot']
sales = [10450000, 10140000, 5960000, 5150000, 4180000, 2830000, 2770000, 301000, 10000, 500000, 765000, 1827000, 4145000, 2510000, 2275000, 2060000]

# Color Scheme
colors = ['#FF5733', '#33FF57', '#3357FF', '#5710FF', '#FFD433', '#D4FF33', '#D633FF', '#FF3357', '#33FFD4', '#571033', '#5733FF', '#FF5733', '#33D4FF', '#57FF33', '#FFF333', '#FF33D4']

plt.figure(figsize=(12, 8))

# Creating the treemap
squarify.plot(sizes=sales, label=brands, color=colors, alpha=0.7)

# Adding a title
plt.title('Global Car Brand Sales Volume (Units Sold)', fontsize=14, weight='bold')

# Removing the axes
plt.axis('off')

# Display the plot
plt.show()