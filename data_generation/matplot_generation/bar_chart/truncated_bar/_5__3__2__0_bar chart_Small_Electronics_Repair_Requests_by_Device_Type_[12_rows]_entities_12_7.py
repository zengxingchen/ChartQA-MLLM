
import matplotlib.pyplot as plt

# Data
days = [str(day) for day in range(1, 31)]
steps_count = [
    3000, 3200, 3500, 3700, 3900, 4200, 4500, 4700, 5000, 5300,
    5500, 5800, 6000, 6200, 6500, 6700, 7000, 7200, 7500, 7800,
    8000, 8300, 8500, 8800, 9000, 9200, 9500, 9700, 10000, 10300
]

# Creating the figure and specifying figure size
plt.figure(figsize=(14, 10))

# Creating the bar chart
plt.bar(days, steps_count, width=0.6, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1', 
    '#FF8F33', '#33D4FF', '#D4FF33', '#5733FF', '#FF3333', '#33FF33', 
    '#3333FF', '#FF33D4', '#D433FF', '#33FFD4', '#FFA133', '#33A1FF', 
    '#A1FF33', '#3333A1', '#FF5733', '#33FF57', '#3357FF', '#FF33A1', 
    '#A133FF', '#33FFA1', '#FF8F33', '#33D4FF', '#D4FF33', '#5733FF'
])

# Adding labels and title
plt.xlabel('Day of the Month')
plt.ylabel('Steps Count')
plt.title('Daily Steps Count in a Fitness Challenge - June 2023')

# Setting y-axis limit
plt.ylim(2500, 10500)

# Show the plot
plt.show()