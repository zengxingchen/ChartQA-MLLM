
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Age Group': '0-5 years', 'Monday': 1.0, 'Tuesday': 0.8, 'Wednesday': 1.2, 'Thursday': 1.0, 'Friday': 1.1},
    {'Age Group': '6-12 years', 'Monday': 2.0, 'Tuesday': 2.1, 'Wednesday': 2.2, 'Thursday': 2.3, 'Friday': 2.0},
    {'Age Group': '13-18 years', 'Monday': 4.0, 'Tuesday': 4.1, 'Wednesday': 3.8, 'Thursday': 4.0, 'Friday': 4.2},
    {'Age Group': '19-35 years', 'Monday': 3.5, 'Tuesday': 3.6, 'Wednesday': 3.7, 'Thursday': 3.8, 'Friday': 3.4},
    {'Age Group': '36-50 years', 'Monday': 2.8, 'Tuesday': 2.9, 'Wednesday': 3.0, 'Thursday': 2.9, 'Friday': 2.7}
]

# Extracting day labels for the X axis
days = list(data[0].keys())[1:]

# Setting up the plot
plt.figure(figsize=(10, 7))

# Various markers and linestyles for visual encoding
markers = ['o', 's', 'D', '^', 'v']
linestyles = ['-', '--', '-.', ':', '-']
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Plotting each age group with their respective visual encodings
for age_data, marker, linestyle, color in zip(data, markers, linestyles, colors):
    age_group = age_data['Age Group']
    values = [age_data[day] for day in days]
    
    plt.plot(days, values, marker=marker, linestyle=linestyle, color=color, label=age_group)

# Adding the legend, which uses the labels defined in the loop above
plt.legend(title='Age Group')

# Titles and labels
plt.title('Weekly Data by Age Group')
plt.xlabel('Day of the Week')
plt.ylabel('Data Points')

# Adding grid for better readability
plt.grid(True)

# Display the plot
plt.show()