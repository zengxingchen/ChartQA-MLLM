
import matplotlib.pyplot as plt

# Data provided in the chart table
data = [
    {'Week': 1, 'Attendance': 12},
    {'Week': 2, 'Attendance': 15},
    {'Week': 3, 'Attendance': 14},
    {'Week': 4, 'Attendance': 17},
    {'Week': 5, 'Attendance': 19},
    {'Week': 6, 'Attendance': 18},
    {'Week': 7, 'Attendance': 22},
    {'Week': 8, 'Attendance': 21},
    {'Week': 9, 'Attendance': 25},
    {'Week': 10, 'Attendance': 23},
    {'Week': 11, 'Attendance': 30},
    {'Week': 12, 'Attendance': 27}
]

# Extracting weeks and attendance values for plotting
weeks = [week_data['Week'] for week_data in data]
attendance = [week_data['Attendance'] for week_data in data]

# Create an area chart
plt.fill_between(weeks, attendance, color="skyblue", alpha=0.4)
plt.plot(weeks, attendance, color="Slateblue", alpha=0.6, linewidth=2)

# Add titles and labels
plt.title("Weekly Attendance Over 12 Weeks")
plt.xlabel("Week")
plt.ylabel("Attendance")

# Customize ticks
plt.xticks(range(1, len(weeks) + 1), labels=[f"Week {i}" for i in weeks])
plt.yticks(range(min(attendance), max(attendance) + 1, 2))

# Add gridlines for better readability
plt.grid(color='grey', linestyle='--', linewidth=0.5)

# Annotate the data points
for i, txt in enumerate(attendance):
    plt.annotate(txt, (weeks[i], attendance[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Show the figure with a tight layout
plt.tight_layout()
plt.show()