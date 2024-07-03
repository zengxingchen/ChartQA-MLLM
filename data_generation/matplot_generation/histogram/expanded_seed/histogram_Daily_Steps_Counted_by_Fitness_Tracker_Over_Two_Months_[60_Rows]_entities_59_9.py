
import matplotlib.pyplot as plt 
from datetime import datetime

# Provided data
data = [
    {'Date': '2023-01-01', ' Steps': 4750},
    {'Date': '2023-01-02', ' Steps': 8300},
    {'Date': '2023-01-03', ' Steps': 6900},
    {'Date': '2023-01-04', ' Steps': 7800},
    {'Date': '2023-01-05', ' Steps': 5600},
    {'Date': '2023-01-06', ' Steps': 8500},
    {'Date': '2023-01-07', ' Steps': 9000},
    {'Date': '2023-01-08', ' Steps': 4000},
    {'Date': '2023-01-09', ' Steps': 7500},
    {'Date': '2023-01-10', ' Steps': 5500},
    {'Date': '2023-01-11', ' Steps': 6200},
    {'Date': '2023-01-12', ' Steps': 8700},
    {'Date': '2023-01-13', ' Steps': 9900},
    {'Date': '2023-01-14', ' Steps': 7500},
    {'Date': '2023-01-15', ' Steps': 5300}
]

# Parse the steps data
steps = [entry[' Steps'] for entry in data]

# Creating the histogram
plt.figure(figsize=(10, 6))   # Set the figure size
n, bins, patches = plt.hist(steps, bins=5, color='skyblue', edgecolor='black')

# Assigning different colors for each bar in histogram
colors = ['orange', 'green', 'blue', 'red', 'purple']
for patch, color in zip(patches, colors):
    patch.set_facecolor(color)

# Adding gridlines
plt.grid(axis='y', alpha=0.75)

# Adding labels and title
plt.xlabel('Steps')
plt.ylabel('Frequency')
plt.title('Histogram of Daily Steps')

# Defining the date format for x-axis
def format_func(value, tick_number):
    # Find the closest integer tick to the current one
    index = int(round(value))
    if 0 <= index < len(data):
        date_str = data[index]['Date']
        return datetime.strptime(date_str, '%Y-%m-%d').strftime('%m-%d')
    return ''

# Adding x ticks
plt.xticks(ticks=np.arange(len(data)), labels=[format_func(i, None) for i in range(len(data))], rotation=45)

# Annotating data points with number of steps
for i in range(len(data)):
    plt.text(i, steps[i], str(steps[i]), ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()