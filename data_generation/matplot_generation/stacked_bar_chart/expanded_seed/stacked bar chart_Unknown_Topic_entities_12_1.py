
import matplotlib.pyplot as plt

# Data provided in the question
data = [
    {'Month': 'January', ' Dogs': 50, ' Cats': 35, ' Rabbits': 20, ' Birds': 10, ' Reptiles': 5},
    {'Month': 'February', ' Dogs': 45, ' Cats': 30, ' Rabbits': 22, ' Birds': 12, ' Reptiles': 4},
    {'Month': 'March', ' Dogs': 60, ' Cats': 40, ' Rabbits': 25, ' Birds': 14, ' Reptiles': 6},
    {'Month': 'April', ' Dogs': 55, ' Cats': 42, ' Rabbits': 28, ' Birds': 15, ' Reptiles': 7},
    {'Month': 'May', ' Dogs': 70, ' Cats': 50, ' Rabbits': 30, ' Birds': 16, ' Reptiles': 8},
    {'Month': 'June', ' Dogs': 65, ' Cats': 48, ' Rabbits': 35, ' Birds': 18, ' Reptiles': 9},
    {'Month': 'July', ' Dogs': 75, ' Cats': 55, ' Rabbits': 38, ' Birds': 20, ' Reptiles': 10},
    {'Month': 'August', ' Dogs': 80, ' Cats': 60, ' Rabbits': 40, ' Birds': 22, ' Reptiles': 11},
    {'Month': 'September', ' Dogs': 65, ' Cats': 45, ' Rabbits': 30, ' Birds': 15, ' Reptiles': 7},
    {'Month': 'October', ' Dogs': 70, ' Cats': 50, ' Rabbits': 32, ' Birds': 17, ' Reptiles': 9},
    {'Month': 'November', ' Dogs': 60, ' Cats': 42, ' Rabbits': 28, ' Birds': 13, ' Reptiles': 6},
    {'Month': 'December', ' Dogs': 55, ' Cats': 38, ' Rabbits': 25, ' Birds': 12, ' Reptiles': 5}
]

# Extracting data for the plot
months = [d['Month'] for d in data]
dogs = [d[' Dogs'] for d in data]
cats = [d[' Cats'] for d in data]
rabbits = [d[' Rabbits'] for d in data]
birds = [d[' Birds'] for d in data]
reptiles = [d[' Reptiles'] for d in data]

# Configuration of the stacked bar chart
bar_width = 0.5  # Width of the bars
index = range(len(months))  # Position of bars on x-axis

# Plotting the stacked bars
plt.bar(index, dogs, bar_width, label='Dogs', color='b')
plt.bar(index, cats, bar_width, bottom=dogs, label='Cats', color='r')
plt.bar(index, rabbits, bar_width, bottom=[i+j for i,j in zip(dogs, cats)], label='Rabbits', color='g')
plt.bar(index, birds, bar_width, bottom=[i+j+k for i,j,k in zip(dogs, cats, rabbits)], label='Birds', color='y')
plt.bar(index, reptiles, bar_width, bottom=[i+j+k+l for i,j,k,l in zip(dogs, cats, rabbits, birds)], label='Reptiles', color='m')

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Number of Pets')
plt.title('Monthly Pet Counts by Category')
plt.xticks(index, months, rotation=45)  # Rotate month labels to fit
plt.legend()  # Show the legend

# Display the plot
plt.tight_layout()  # Adjust layout to prevent clipping of ylabel/tick labels
plt.show()