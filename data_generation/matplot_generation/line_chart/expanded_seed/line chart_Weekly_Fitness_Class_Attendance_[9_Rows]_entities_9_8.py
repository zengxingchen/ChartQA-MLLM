
import matplotlib.pyplot as plt

# Data from the chart table
data = [
    {'Week': '2023-W10', 'Yoga': 24, 'Pilates': 19, 'Spinning': 30, 'Zumba': 22},
    {'Week': '2023-W11', 'Yoga': 20, 'Pilates': 22, 'Spinning': 35, 'Zumba': 25},
    {'Week': '2023-W12', 'Yoga': 26, 'Pilates': 18, 'Spinning': 33, 'Zumba': 28},
    {'Week': '2023-W13', 'Yoga': 28, 'Pilates': 21, 'Spinning': 37, 'Zumba': 30},
    {'Week': '2023-W14', 'Yoga': 30, 'Pilates': 25, 'Spinning': 40, 'Zumba': 32},
    {'Week': '2023-W15', 'Yoga': 32, 'Pilates': 20, 'Spinning': 42, 'Zumba': 34},
    {'Week': '2023-W16', 'Yoga': 34, 'Pilates': 23, 'Spinning': 45, 'Zumba': 36},
    {'Week': '2023-W17', 'Yoga': 29, 'Pilates': 26, 'Spinning': 43, 'Zumba': 38},
    {'Week': '2023-W18', 'Yoga': 35, 'Pilates': 24, 'Spinning': 47, 'Zumba': 40}
]

# Extracting the weeks and the attendance for each class
weeks = [entry['Week'] for entry in data]
yoga_attendances = [entry['Yoga'] for entry in data]
pilates_attendances = [entry['Pilates'] for entry in data]
spinning_attendances = [entry['Spinning'] for entry in data]
zumba_attendances = [entry['Zumba'] for entry in data]

# Plotting the line chart
plt.figure(figsize=(10, 6))

plt.plot(weeks, yoga_attendances, marker='o', linestyle='-', color='blue', label='Yoga')
plt.plot(weeks, pilates_attendances, marker='x', linestyle='--', color='green', label='Pilates')
plt.plot(weeks, spinning_attendances, marker='s', linestyle='-.', color='red', label='Spinning')
plt.plot(weeks, zumba_attendances, marker='^', linestyle=':', color='purple', label='Zumba')

# Adding chart details
plt.title('Class Attendance Over Weeks')
plt.xlabel('Week')
plt.ylabel('Attendance')
plt.xticks(rotation=45)    # Rotate the x-axis labels to prevent overlap
plt.legend()              # Shows the legend
plt.tight_layout()        # Adjusts plot to ensure everything fits without overlap

# Save the figure (Optional)
# plt.savefig('class_attendance_over_weeks.png')

plt.show()  # Display the plot