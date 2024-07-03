
import matplotlib.pyplot as plt

# Data from the given table
age_groups = ['0-8', '9-12', '13-18', '19-25', '26+']
average_daily_screen_time = [1.5, 2.5, 4.0, 5.0, 4.5]

# Create a cumulative data list for the area chart
cumulative_data = [0] + [sum(average_daily_screen_time[:i+1]) for i in range(len(average_daily_screen_time))]

# Prepare the figure and axis
fig, ax = plt.subplots()

# Colors for each age group (just for diversifying the visuals)
colors = ['skyblue', 'salmon', 'lightgreen', 'violet', 'gold']

# Create an area chart (stackplot)
ax.stackplot(age_groups, cumulative_data, colors=colors, alpha=0.5)

# Adding data points on top of the area chart
for i in range(len(age_groups)):
    ax.scatter(age_groups[i], cumulative_data[i+1], color='black')  # Use black for the data point
    ax.text(age_groups[i], cumulative_data[i+1], f'{average_daily_screen_time[i]}h', 
            va='bottom', ha='center')  # Annotate the data point value

# Beautify the plot
ax.set_xlabel('Age Group')
ax.set_ylabel('Cumulative Average Daily Screen Time (hours)')
ax.set_title('Cumulative Average Daily Screen Time by Age Group')
plt.xticks(age_groups)  # Ensure all age groups are included as x-axis ticks
ax.margins(0.05)  # Add a small margin to the plot
plt.tight_layout()  # Adjust the layout to avoid cutting off labels

# Show the plot
plt.show()