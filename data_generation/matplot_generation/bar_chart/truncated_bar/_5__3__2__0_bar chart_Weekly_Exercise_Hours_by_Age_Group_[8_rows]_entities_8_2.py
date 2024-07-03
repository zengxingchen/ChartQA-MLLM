
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
stress_level = [50, 55, 60, 65, 70, 75, 80, 85, 90, 85, 80, 75]
exercise_hours = [15, 16, 17, 18, 19, 20, 21, 22, 23, 21, 20, 19]
quality_sleep_hours = [6, 5.5, 6, 5, 7, 6.5, 6, 7, 6, 6.5, 7, 6]

# Plot setup
fig, ax = plt.subplots(figsize=(10, 14))

# Create bar chart
bar_width = 0.3
bar_locations_stress = range(len(stress_level))
bar_locations_exercise = [x + bar_width for x in bar_locations_stress]
bar_locations_sleep = [x + bar_width for x in bar_locations_exercise]

bars1 = ax.bar(bar_locations_stress, stress_level, bar_width, label='Stress Level', color='#FF6347')
bars2 = ax.bar(bar_locations_exercise, exercise_hours, bar_width, label='Exercise Hours', color='#4682B4')
bars3 = ax.bar(bar_locations_sleep, quality_sleep_hours, bar_width, label='Quality Sleep Hours', color='#32CD32')

# Set the position of the x ticks
ax.set_xticks([r + bar_width for r in range(len(stress_level))])
ax.set_xticklabels(months)

# Setting limits
ax.set_ylim(4, 25)

# Adding labels and title
plt.ylabel('Measurements')
plt.title('Monthly Health Metrics')
ax.legend(loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()