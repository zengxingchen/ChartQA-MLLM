
import matplotlib.pyplot as plt

# Generate data points
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
exercise_durations = [1.5, 1.6, 1.7, 1.8, 2.0, 2.1, 2.3, 2.4, 2.2, 2.1, 1.9, 1.8]

plt.figure(figsize=(14, 8))  # Change the width and height of the chart

# Create a horizontal bar chart with specified bar width and colors
plt.barh(months, exercise_durations, color=[
    '#2E8B57', '#3CB371', '#66CDAA', '#8FBC8F', '#20B2AA',
    '#48D1CC', '#40E0D0', '#00CED1', '#5F9EA0', '#4682B4',
    '#B0C4DE', '#B0E0E6'], height=0.6)

plt.xlabel('Average Exercise Duration (hours)', fontsize=14)
plt.title('Average Monthly Exercise Duration in 2023', fontsize=16)
plt.xlim(1, 2.5)  # Truncated to start from 1 for better visibility

plt.tight_layout()
plt.show()