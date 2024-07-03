
import matplotlib.pyplot as plt
import numpy as np

# Your provided data
data = [
    {'Category': 'Fiction', ' Week 1': ' 22%', ' Week 2': ' 20%', ' Week 3': ' 23%', ' Week 4': ' 26%', ' Week 5': ' 24%', ' Week 6': ' 25%', ' Week 7': ' 20%', ' Week 8': ' 22%', ' Week 9': ' 23%', ' Week 10': ' 21%'},
    # ... (continuation of the other categories)
]

# Processing the data
categories = [entry['Category'] for entry in data]
weeks = [' Week ' + str(i) for i in range(1, 11)]

# Initialize a dictionary of lists for each week
percentages = {week: [] for week in weeks}

# Fill in the dictionary with data, converting percentage strings to floats
for entry in data:
    for week in weeks:
        percent_value = float(entry[week].strip().replace('%', ''))
        percentages[week].append(percent_value)

# The data needs to be in an array form where each row represents a category and each column represents a week
stacked_data = np.array([percentages[week] for week in weeks]).T  # Transpose the matrix

# Plotting
fig, ax = plt.subplots()

# We will create a stacked bar chart by plotting each week's data on top of each other
bottom = np.zeros(len(categories))  # Start with 0 for the bottom of the first set of bars
for i, week in enumerate(weeks):
    ax.bar(categories, stacked_data[:, i], bottom=bottom, label=week)
    bottom += stacked_data[:, i]  # Update the bottom to be the top of the last bar

# Formatting the chart with a title, legend, and axis labels
ax.set_title('Book Sales by Category Over 10 Weeks')
ax.legend(title='Weeks')
ax.set_xlabel('Categories')
ax.set_ylabel('Percentage (%)')

# Convert the y-axis labels to percentage format
def to_percent(y, position):
    # Ignore the passed-in position. This has the effect of scaling the default tick locations.
    s = str(int(100 * y))
    return s + '%'

formatter = plt.FuncFormatter(to_percent)
ax.yaxis.set_major_formatter(formatter)

# Show the plot
plt.xticks(rotation=45, ha="right")  # Rotate the x-axis labels for better readability
plt.tight_layout()  # Fit the plot neatly into the figure area
plt.show()