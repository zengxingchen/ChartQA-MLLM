
import matplotlib.pyplot as plt
from datetime import datetime

# Your data
data = [
    {'Date': '2023-01-01', 'Person A': 4567, 'Person B': 7890, 'Person C': 6745, 'Person D': 5678, 'Person E': 9870},
    {'Date': '2023-01-02', 'Person A': 5896, 'Person B': 7980, 'Person C': 7560, 'Person D': 6789, 'Person E': 10890},
    {'Date': '2023-01-03', 'Person A': 6400, 'Person B': 7200, 'Person C': 8020, 'Person D': 7090, 'Person E': 11234},
    {'Date': '2023-01-04', 'Person A': 6890, 'Person B': 8300, 'Person C': 8790, 'Person D': 7450, 'Person E': 10021}
]

# Parsing the dates from the string format to datetime objects for plotting
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]

# Separate data for each person
values_a = [d['Person A'] for d in data]
values_b = [d['Person B'] for d in data]
values_c = [d['Person C'] for d in data]
values_d = [d['Person D'] for d in data]
values_e = [d['Person E'] for d in data]

# Create the plot
plt.figure(figsize=(10,6))

# Plot each person's data with a distinctive style
plt.plot(dates, values_a, color='blue', marker='o', linestyle='-', label='Person A')
plt.plot(dates, values_b, color='red', marker='v', linestyle='--', label='Person B')
plt.plot(dates, values_c, color='green', marker='s', linestyle='-.', label='Person C')
plt.plot(dates, values_d, color='purple', marker='^', linestyle=':', label='Person D')
plt.plot(dates, values_e, color='orange', marker='*', linestyle='-', label='Person E')

# Add title and labels
plt.title('Daily Values per Person')
plt.xlabel('Date')
plt.ylabel('Values')

# Rotate and format the x-axis labels
plt.xticks(dates, [d.strftime('%Y-%m-%d') for d in dates], rotation=45)

# Adding a legend
plt.legend()

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()