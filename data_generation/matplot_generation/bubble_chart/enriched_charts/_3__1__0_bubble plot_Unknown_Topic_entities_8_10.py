
import matplotlib.pyplot as plt

# Data for plotting
destinations = [
    'Harvard', 'Stanford', 'MIT', 'Cambridge', 'Oxford', 'Caltech', 'ETH Zurich', 
    'Imperial', 'UChicago', 'Princeton', 'Columbia', 'Yale', 'UC Berkeley', 
    'UCLA', 'UCSD', 'U Illinois', 'U Michigan', 'U Tokyo', 'Peking', 'Tsinghua'
]
student_enrollment = [31, 28, 30, 21, 22, 20, 19, 17, 16, 18, 29, 24, 40, 44, 38, 35, 46, 32, 34, 33]
average_tuition = [52000, 48500, 49800, 45000, 44000, 54000, 38000, 46000, 53000, 49000, 52000, 50000, 42000, 40000, 39000, 37000, 41000, 36000, 34000, 35000]
student_satisfaction = [9.3, 9.1, 9.2, 8.9, 8.8, 9.0, 8.7, 8.5, 9.0, 9.4, 9.2, 9.3, 8.6, 8.5, 8.4, 8.3, 8.7, 8.8, 8.6, 8.7]

# Create a figure with specified width and height
fig, ax = plt.subplots(figsize=(16, 12))

# Bubble sizes (scaled)
sizes = [enrollment * 10 for enrollment in student_enrollment]

# Bubble colors with specific hex color codes
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#FF8833', 
    '#33FFD5', '#FFD733', '#FF5733', '#33FF57', '#3357FF', '#FF33A6', 
    '#A633FF', '#FF8833', '#33FFD5', '#FFD733', '#FF5733', '#33FF57', 
    '#3357FF', '#FF33A6'
]

# Plot each data point
for (destination, enrollment, tuition, satisfaction, size, color) in zip(destinations, student_enrollment, average_tuition, student_satisfaction, sizes, colors):
    ax.scatter(enrollment, tuition, s=size, label=destination, alpha=0.6, edgecolors='w', color=color)

# Titles and labels
plt.title('Top Universities by Student Enrollment, Tuition, and Satisfaction')
plt.xlabel('Student Enrollment (thousands)')
plt.ylabel('Average Tuition (USD)')

# Legend
handles, labels = ax.get_legend_handles_labels()
hl = sorted(zip(handles, labels), key=lambda x: x[1])
handles2, labels2 = zip(*hl)
ax.legend(handles2, labels2, loc="upper left", title="Universities")

# Show plot
plt.show()