
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hours_of_exercise = [1.5, 2.0, 1.8, 2.5, 2.2, 2.8, 3.0, 3.2, 2.9, 3.5]
happiness_score = [7.2, 7.8, 7.4, 8.0, 7.6, 8.3, 8.4, 8.6, 8.5, 8.9]

# Scatter plot
plt.figure(figsize=(12, 8))  # Width:12, Height:8
plt.scatter(days, hours_of_exercise, color='#FF33A1', label='Hours of Exercise')  # Pink
plt.scatter(days, happiness_score, color='#33FF8A', label='Happiness Score')  # Green

# Customize the plot
plt.title('Correlation Between Exercise and Happiness Over 10 Days', pad=20)
plt.xlabel('Day')
plt.ylabel('Measurements')
plt.legend(loc='upper left')
plt.grid(True)

# Show the plot
plt.show()