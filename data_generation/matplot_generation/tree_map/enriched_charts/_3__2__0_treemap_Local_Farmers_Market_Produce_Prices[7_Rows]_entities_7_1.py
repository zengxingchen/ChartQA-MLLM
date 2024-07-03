
import matplotlib.pyplot as plt
import squarify

# Data points
countries = [
    'USA', 'China', 'UK', 'Germany', 'France', 'Japan', 'Italy', 'Canada',
    'Spain', 'Australia', 'South Korea', 'Brazil', 'India', 'Russia',
    'Netherlands', 'Sweden', 'Norway', 'Mexico', 'Denmark', 'Switzerland',
    'Belgium', 'Austria', 'Finland', 'Ireland', 'New Zealand', 'Greece',
    'Poland', 'Portugal', 'Turkey', 'Others'
]
book_sales = [
    750, 540, 320, 280, 220, 180, 150, 140, 130, 120, 110, 105, 100, 90, 85, 80, 
    75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 200
]

# Color scheme
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF5733', '#33FFF0', '#3377FF', 
    '#57FF33', '#A833FF', '#5733FF', '#33FF57', '#FF5733', '#5733FF', '#FF3357', 
    '#57FF33', '#33FF57', '#3357FF', '#FF5733', '#33FF57', '#5733FF', '#33FFF0', 
    '#3377FF', '#FF33A8', '#33FF57', '#A833FF', '#5733FF', '#FF5733', '#FF33A8', 
    '#33FF57', '#D3D3D3'
]

plt.figure(figsize=(16, 12))
squarify.plot(sizes=book_sales, label=countries, color=colors, alpha=0.8)

# Chart details
plt.title('Global Book Sales by Country in 2023 (millions)', fontsize=20, y=1.02)
plt.axis('off')

plt.show()