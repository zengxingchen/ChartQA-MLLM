
import matplotlib.pyplot as plt

# Given data
data = [
    {'Week': 1, 'Cups of Coffee': 150}, {'Week': 2, 'Cups of Coffee': 130},
    {'Week': 3, 'Cups of Coffee': 165}, {'Week': 4, 'Cups of Coffee': 123},
    {'Week': 5, 'Cups of Coffee': 140}, {'Week': 6, 'Cups of Coffee': 158},
    {'Week': 7, 'Cups of Coffee': 175}, {'Week': 8, 'Cups of Coffee': 149},
    {'Week': 9, 'Cups of Coffee': 161}, {'Week': 10, 'Cups of Coffee': 113},
    {'Week': 11, 'Cups of Coffee': 107}, {'Week': 12, 'Cups of Coffee': 142},
    {'Week': 13, 'Cups of Coffee': 189}, {'Week': 14, 'Cups of Coffee': 171},
    {'Week': 15, 'Cups of Coffee': 140}
]

# Extracting 'Cups of Coffee' values for the histogram
cups_of_coffee = [week_data['Cups of Coffee'] for week_data in data]

# Create a histogram
plt.figure(figsize=(10, 6))  # Sets the figure size
plt.hist(cups_of_coffee, bins=8, color='skyblue', edgecolor='black')

# Adding visual enhancements
plt.title('Histogram of Cups of Coffee Consumed Per Week Over 15 Weeks', fontsize=15)
plt.xlabel('Cups of Coffee', fontsize=12)
plt.ylabel('Frequency/Number of Weeks', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', alpha=0.75)

# Display the histogram
plt.show()