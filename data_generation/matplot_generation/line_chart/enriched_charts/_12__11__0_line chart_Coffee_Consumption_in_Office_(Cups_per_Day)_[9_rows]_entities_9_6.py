
import matplotlib.pyplot as plt

# Data points
years = ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
expenses = [1200, 1300, 1150, 1400, 1500, 1600, 1800, 1750, 1600, 1550, 1500, 1450]

plt.figure(figsize=(10, 6))  # Adjust width and height of the chart
plt.plot(years, expenses, marker='o', linestyle='-', color='#4682B4')  # Specific hex color

# Annotation for the highest expense
plt.annotate('Peak Expense', xy=('2025', 1800), xytext=('2026', 1850),
             arrowprops=dict(facecolor='#FF69B4', shrink=0.05))

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Expenses (in $)')
plt.title('Annual Business Expenses Over a Decade', pad=20)  # Added padding to avoid overlap

# Showing the plot
plt.show()