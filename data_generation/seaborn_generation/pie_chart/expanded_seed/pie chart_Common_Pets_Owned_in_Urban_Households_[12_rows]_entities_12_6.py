
import matplotlib.pyplot as plt

# Data
data = [{'Pet Type': 'Dogs', 'Percentage of Households': 40},
        {'Pet Type': 'Cats', 'Percentage of Households': 30},
        {'Pet Type': 'Fish', 'Percentage of Households': 12},
        {'Pet Type': 'Birds', 'Percentage of Households': 6},
        {'Pet Type': 'Hamsters', 'Percentage of Households': 2},
        {'Pet Type': 'Guinea Pigs', 'Percentage of Households': 2},
        {'Pet Type': 'Turtles', 'Percentage of Households': 1},
        {'Pet Type': 'Rabbits', 'Percentage of Households': 1},
        {'Pet Type': 'Snakes', 'Percentage of Households': 1},
        {'Pet Type': 'Lizards', 'Percentage of Households': 1},
        {'Pet Type': 'Frogs', 'Percentage of Households': 1},
        {'Pet Type': 'Others', 'Percentage of Households': 3}]

# Extracting data
pet_types = [item['Pet Type'] for item in data]
percentages = [item['Percentage of Households'] for item in data]

# Creating pie chart
fig, ax = plt.subplots()
ax.pie(percentages, labels=pet_types, autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Title for the pie chart
plt.title('Percentage of Households by Pet Type')

# Display the pie chart
plt.show()