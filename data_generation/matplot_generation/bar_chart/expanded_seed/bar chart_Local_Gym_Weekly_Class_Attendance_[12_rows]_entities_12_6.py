
import matplotlib.pyplot as plt
import numpy as np

# Given data
data = [
    {'Class Name': 'Yoga', 'Week 1': 30, 'Week 2': 28, 'Week 3': 32, 'Week 4': 35},
    {'Class Name': 'Pilates', 'Week 1': 25, 'Week 2': 20, 'Week 3': 22, 'Week 4': 30},
    {'Class Name': 'Spinning', 'Week 1': 33, 'Week 2': 35, 'Week 3': 30, 'Week 4': 40},
    {'Class Name': 'Zumba', 'Week 1': 40, 'Week 2': 42, 'Week 3': 38, 'Week 4': 45},
    {'Class Name': 'HIIT', 'Week 1': 50, 'Week 2': 60, 'Week 3': 55, 'Week 4': 65},
    {'Class Name': 'CrossFit', 'Week 1': 45, 'Week 2': 50, 'Week 3': 48, 'Week 4': 53},
    {'Class Name': 'Aqua Fitness', 'Week 1': 20, 'Week 2': 19, 'Week 3': 25, 'Week 4': 22},
    {'Class Name': 'Kickboxing', 'Week 1': 30, 'Week 2': 25, 'Week 3': 27, 'Week 4': 35},
    {'Class Name': 'Stretch and Tone', 'Week 1': 15, 'Week 2': 18, 'Week 3': 20, 'Week 4': 25},
    {'Class Name': 'Bodybuilding', 'Week 1': 22, 'Week 2': 20, 'Week 3': 24, 'Week 4': 30},
    {'Class Name': 'Cardio Circuit', 'Week 1': 35, 'Week 2': 38, 'Week 3': 40, 'Week 4': 42},
    {'Class Name': 'Dance', 'Week 1': 28, 'Week 2': 30, 'Week 3': 32, 'Week 4': 34}
]

# Extract class names and weekly data
class_names = [item['Class Name'] for item in data]
week_1_data = [item['Week 1'] for item in data]
week_2_data = [item['Week 2'] for item in data]
week_3_data = [item['Week 3'] for item in data]
week_4_data = [item['Week 4'] for item in data]

# Number of classes
num_classes = len(class_names)

# X positions for each class in the bar chart
x = np.arange(num_classes)

# Width of each bar
bar_width = 0.2

# Setting up the bar chart
fig, ax = plt.subplots(figsize=(15, 8))

# Placing bars for each week
bars1 = ax.bar(x - bar_width*1.5, week_1_data, bar_width, label='Week 1', color='skyblue')
bars2 = ax.bar(x - bar_width/2, week_2_data, bar_width, label='Week 2', color='orange')
bars3 = ax.bar(x + bar_width/2, week_3_data, bar_width, label='Week 3', color='green')
bars4 = ax.bar(x + bar_width*1.5, week_4_data, bar_width, label='Week 4', color='purple')

# Adding class names to the x-axis
ax.set_xticks(x)
ax.set_xticklabels(class_names, rotation=45, ha='right')

# Adding axis labels and title
ax.set_xlabel('Class Name')
ax.set_ylabel('Number of Participants')
ax.set_title('Class Attendance Over 4 Weeks')

# Adding a legend
ax.legend()

# Displaying values on top of each bar
def add_values(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_values(bars1)
add_values(bars2)
add_values(bars3)
add_values(bars4)

# Display plot
plt.tight_layout()  # Adjust the layout to make room for the rotated x-axis labels
plt.show()