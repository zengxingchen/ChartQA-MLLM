
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Month': 'January', 'Children (0-12)': 450, 'Teens (13-18)': 200, 'Adults (19-59)': 700, 'Seniors (60+)': 350},
    {'Month': 'February', 'Children (0-12)': 420, 'Teens (13-18)': 190, 'Adults (19-59)': 650, 'Seniors (60+)': 330},
    {'Month': 'March', 'Children (0-12)': 500, 'Teens (13-18)': 210, 'Adults (19-59)': 730, 'Seniors (60+)': 370},
    {'Month': 'April', 'Children (0-12)': 480, 'Teens (13-18)': 220, 'Adults (19-59)': 750, 'Seniors (60+)': 360},
    {'Month': 'May', 'Children (0-12)': 520, 'Teens (13-18)': 230, 'Adults (19-59)': 780, 'Seniors (60+)': 380},
    {'Month': 'June', 'Children (0-12)': 540, 'Teens (13-18)': 240, 'Adults (19-59)': 800, 'Seniors (60+)': 390},
    {'Month': 'July', 'Children (0-12)': 560, 'Teens (13-18)': 250, 'Adults (19-59)': 820, 'Seniors (60+)': 400},
    {'Month': 'August', 'Children (0-12)': 580, 'Teens (13-18)': 260, 'Adults (19-59)': 840, 'Seniors (60+)': 420},
    {'Month': 'September', 'Children (0-12)': 550, 'Teens (13-18)': 245, 'Adults (19-59)': 810, 'Seniors (60+)': 410},
    {'Month': 'October', 'Children (0-12)': 530, 'Teens (13-18)': 235, 'Adults (19-59)': 790, 'Seniors (60+)': 390},
    {'Month': 'November', 'Children (0-12)': 490, 'Teens (13-18)': 225, 'Adults (19-59)': 770, 'Seniors (60+)': 380},
    {'Month': 'December', 'Children (0-12)': 470, 'Teens (13-18)': 215, 'Adults (19-59)': 760, 'Seniors (60+)': 370}
]

# Parsing data
months = [item['Month'] for item in data]
children_counts = [item['Children (0-12)'] for item in data]
teens_counts = [item['Teens (13-18)'] for item in data]
adults_counts = [item['Adults (19-59)'] for item in data]
seniors_counts = [item['Seniors (60+)'] for item in data]

# Setting up the bar widths
bar_width = 0.5

# Setting up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Stacking bars
bar1 = ax.bar(months, children_counts, bar_width, label='Children (0-12)', color='skyblue')
bar2 = ax.bar(months, teens_counts, bar_width, bottom=children_counts, label='Teens (13-18)', color='orange')
bar3 = ax.bar(months, adults_counts, bar_width, bottom=[i+j for i, j in zip(children_counts, teens_counts)], label='Adults (19-59)', color='lightgreen')
bar4 = ax.bar(months, seniors_counts, bar_width, bottom=[i+j+k for i, j, k in zip(children_counts, teens_counts, adults_counts)], label='Seniors (60+)', color='purple')

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Number of Individuals')
plt.title('Monthly Attendance by Age Group')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adding legend
plt.legend()

# Displaying the plot
plt.tight_layout()
plt.show()