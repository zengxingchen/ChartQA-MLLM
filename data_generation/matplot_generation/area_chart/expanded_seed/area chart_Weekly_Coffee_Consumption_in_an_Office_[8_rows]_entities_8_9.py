
import matplotlib.pyplot as plt

# provided data
data = [
    {'Week': 'Week 1', 'Cups of Coffee': 250},
    {'Week': 'Week 2', 'Cups of Coffee': 210},
    {'Week': 'Week 3', 'Cups of Coffee': 230},
    {'Week': 'Week 4', 'Cups of Coffee': 220},
    {'Week': 'Week 5', 'Cups of Coffee': 260},
    {'Week': 'Week 6', 'Cups of Coffee': 240},
    {'Week': 'Week 7', 'Cups of Coffee': 230},
    {'Week': 'Week 8', 'Cups of Coffee': 250}
]

# extract the weeks and cup counts into separate lists for plotting
weeks = [item['Week'] for item in data]
cups_of_coffee = [item['Cups of Coffee'] for item in data]

# generate the x-axis indices based on the number of weeks
x_indices = range(len(weeks))

# create the area chart
plt.fill_between(x_indices, cups_of_coffee, color="skyblue", alpha=0.4)

# provide the annotations on each data point
for i, cup_count in enumerate(cups_of_coffee):
    plt.text(x_indices[i], cup_count + 5, str(cup_count), ha='center')

# set the x-axis to display the weeks
plt.xticks(x_indices, weeks)

# adding titles and labels
plt.title('Cups of Coffee Consumed Over 8 Weeks')
plt.xlabel('Week')
plt.ylabel('Cups of Coffee')

# add grid lines for better readability
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# show the plot
plt.show()