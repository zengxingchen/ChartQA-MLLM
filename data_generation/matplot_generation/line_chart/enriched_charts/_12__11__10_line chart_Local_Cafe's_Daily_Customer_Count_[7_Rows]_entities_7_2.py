
import matplotlib.pyplot as plt

# Data for the new chart
data = [
    {'Day': 'Monday', 'Caloric Intake': 2000},
    {'Day': 'Tuesday', 'Caloric Intake': 2500},
    {'Day': 'Wednesday', 'Caloric Intake': 2200},
    {'Day': 'Thursday', 'Caloric Intake': 2800},
    {'Day': 'Friday', 'Caloric Intake': 2300},
    {'Day': 'Saturday', 'Caloric Intake': 2400},
    {'Day': 'Sunday', 'Caloric Intake': 2600}
]

# Extracting the days and caloric intake into separate lists
days = [entry['Day'] for entry in data]
caloric_intake = [entry['Caloric Intake'] for entry in data]

# Creating the line chart
plt.figure(figsize=(16, 8))  # Set the size of the figure

# Plot the data
plt.plot(days, caloric_intake, color='#1f77b4', linestyle='-', marker='o', linewidth=2, markersize=8, label="Caloric Intake per Day")

# Add titles and labels
plt.title('Daily Caloric Intake Over a Week', fontsize=20, loc='center')
plt.xlabel('Day of the Week', fontsize=16)
plt.ylabel('Caloric Intake', fontsize=16)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Include grid lines
plt.grid(True, linestyle='--', linewidth=0.5, color='grey')

# Add text annotations for the data points
for i, intake in enumerate(caloric_intake):
    plt.text(days[i], intake + 50, str(intake), ha='center', color='black')

# Highlight the max and min caloric intake
max_intake = max(caloric_intake)
min_intake = min(caloric_intake)
plt.axhline(max_intake, color='#2ca02c', linestyle='--', linewidth=1)
plt.axhline(min_intake, color='#d62728', linestyle='--', linewidth=1)

# Add a legend
plt.legend(loc='upper left')

# Show the plot
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping
plt.show()