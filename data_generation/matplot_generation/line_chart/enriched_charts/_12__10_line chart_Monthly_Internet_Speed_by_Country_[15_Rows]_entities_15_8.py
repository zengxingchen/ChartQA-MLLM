
import matplotlib.pyplot as plt

# Data provided in the question
chart_data = [
    {'Month': 'January', 'Reading (hours)': 5, 'Writing (hours)': 7, 'Research (hours)': 8, 'Discussions (hours)': 10},
    {'Month': 'February', 'Reading (hours)': 6, 'Writing (hours)': 6.5, 'Research (hours)': 9, 'Discussions (hours)': 11},
    {'Month': 'March', 'Reading (hours)': 7, 'Writing (hours)': 6, 'Research (hours)': 10, 'Discussions (hours)': 12},
    {'Month': 'April', 'Reading (hours)': 8, 'Writing (hours)': 5.5, 'Research (hours)': 11, 'Discussions (hours)': 13},
    {'Month': 'May', 'Reading (hours)': 9, 'Writing (hours)': 5, 'Research (hours)': 12, 'Discussions (hours)': 14},
    {'Month': 'June', 'Reading (hours)': 10, 'Writing (hours)': 4.5, 'Research (hours)': 13, 'Discussions (hours)': 15},
    {'Month': 'July', 'Reading (hours)': 9, 'Writing (hours)': 5, 'Research (hours)': 12, 'Discussions (hours)': 14},
    {'Month': 'August', 'Reading (hours)': 8, 'Writing (hours)': 5.5, 'Research (hours)': 11, 'Discussions (hours)': 13},
    {'Month': 'September', 'Reading (hours)': 7, 'Writing (hours)': 6, 'Research (hours)': 10, 'Discussions (hours)': 12},
    {'Month': 'October', 'Reading (hours)': 6, 'Writing (hours)': 6.5, 'Research (hours)': 9, 'Discussions (hours)': 11},
    {'Month': 'November', 'Reading (hours)': 5, 'Writing (hours)': 7, 'Research (hours)': 8, 'Discussions (hours)': 10},
    {'Month': 'December', 'Reading (hours)': 6, 'Writing (hours)': 6.5, 'Research (hours)': 9, 'Discussions (hours)': 11}
]

# Extracting the data for plotting
months = [entry['Month'] for entry in chart_data]
reading_hours = [entry['Reading (hours)'] for entry in chart_data]
writing_hours = [entry['Writing (hours)'] for entry in chart_data]
research_hours = [entry['Research (hours)'] for entry in chart_data]
discussions_hours = [entry['Discussions (hours)'] for entry in chart_data]

# Plotting the data
plt.figure(figsize=(14, 10))

plt.plot(months, reading_hours, label='Reading', marker='o', linestyle='-', color='#1f78b4')
plt.plot(months, writing_hours, label='Writing', marker='s', linestyle='--', color='#33a02c')
plt.plot(months, research_hours, label='Research', marker='^', linestyle='-.', color='#e31a1c')
plt.plot(months, discussions_hours, label='Discussions', marker='d', linestyle=':', color='#ff7f00')

# Adding the title and labels
plt.title('Monthly Academic Activities Time Allocation', fontsize=16, pad=20)
plt.xlabel('Month')
plt.ylabel('Time (hours)')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

# Adding annotations
for i, txt in enumerate(reading_hours):
    plt.annotate(txt, (months[i], reading_hours[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Adding a legend
plt.legend(loc='upper right')

# Adjust layout to prevent clipping and show the plot
plt.tight_layout()
plt.show()