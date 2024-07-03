
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
production_cost = [1000, 1500, 1600, 2000, 2100, 2500, 2700, 3000, 3200, 3500]
revenue = [2000, 2500, 2700, 3000, 3200, 3500, 3700, 4000, 4200, 4500]

# Scatter plot
plt.figure(figsize=(12, 7))  # Width:12, Height:7
plt.scatter(days, production_cost, color='#FF6347', label='Production Cost')  # Tomato Red
plt.scatter(days, revenue, color='#4682B4', label='Revenue')  # Steel Blue

# Customize the plot
plt.title('Business Performance Over 10 Days', pad=20)
plt.xlabel('Day')
plt.ylabel('Amount ($)')
plt.legend(loc='upper left')
plt.grid(True)

# Show the plot
plt.show()