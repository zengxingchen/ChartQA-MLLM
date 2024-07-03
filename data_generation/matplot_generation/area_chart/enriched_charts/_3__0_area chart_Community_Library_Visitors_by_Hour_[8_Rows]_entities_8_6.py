
import matplotlib.pyplot as plt

# Data
months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
observation_hours = [
    50, 65, 80, 90, 85, 75,
    80, 85, 90, 95, 100, 130
]

# Plot
fig, ax = plt.subplots(figsize=(14, 7))  # Modify width (14) and height (7) of the chart
ax.fill_between(months, observation_hours, color='#FF5733', alpha=0.6)  # Fill with a specific color code

# Style
ax.set_title('Monthly Observation Hours in 2023', fontsize=20, pad=20)  # Changing the title
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Observation Hours', fontsize=14)
ax.set_ylim(0, max(observation_hours) + 20)  # Set the y-axis limit to give some space at the top
ax.margins(x=0)  # Remove the white space on the x-axis edges
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Annotation
peak_hours = max(observation_hours)
peak_month = months[observation_hours.index(peak_hours)]
ax.annotate(f'Peak Hours: {peak_hours}', xy=(peak_month, peak_hours), xytext=(5, 20),
            textcoords='offset points', arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))

plt.show()