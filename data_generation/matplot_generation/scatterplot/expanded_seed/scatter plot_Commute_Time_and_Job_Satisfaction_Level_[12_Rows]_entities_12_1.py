
import matplotlib.pyplot as plt

# Input data
data = [
    {'Employee ID': 1, ' Commute Time (minutes)': 30, ' Job Satisfaction (1-10)': 7},
    {'Employee ID': 2, ' Commute Time (minutes)': 45, ' Job Satisfaction (1-10)': 6},
    {'Employee ID': 3, ' Commute Time (minutes)': 60, ' Job Satisfaction (1-10)': 4},
    {'Employee ID': 4, ' Commute Time (minutes)': 20, ' Job Satisfaction (1-10)': 8},
    {'Employee ID': 5, ' Commute Time (minutes)': 10, ' Job Satisfaction (1-10)': 9},
    {'Employee ID': 6, ' Commute Time (minutes)': 50, ' Job Satisfaction (1-10)': 6},
    {'Employee ID': 7, ' Commute Time (minutes)': 25, ' Job Satisfaction (1-10)': 8},
    {'Employee ID': 8, ' Commute Time (minutes)': 35, ' Job Satisfaction (1-10)': 7},
    {'Employee ID': 9, ' Commute Time (minutes)': 70, ' Job Satisfaction (1-10)': 3},
    {'Employee ID': 10, ' Commute Time (minutes)': 15, ' Job Satisfaction (1-10)': 9},
    {'Employee ID': 11, ' Commute Time (minutes)': 40, ' Job Satisfaction (1-10)': 7},
    {'Employee ID': 12, ' Commute Time (minutes)': 55, ' Job Satisfaction (1-10)': 5}
]

# Extracting the commute times and job satisfactions into separate lists
commute_times = [employee[' Commute Time (minutes)'] for employee in data]
job_satisfactions = [employee[' Job Satisfaction (1-10)'] for employee in data]
employee_ids = [employee['Employee ID'] for employee in data]

# Create a new figure for plotting
plt.figure(figsize=(10, 6))

# Plotting the scatter plot
scatter = plt.scatter(
    commute_times,
    job_satisfactions,
    s=[i*20 for i in job_satisfactions],  # Sizes based on job satisfaction (giving it more weight)
    cmap='viridis',                        # Color map for variations based on commute time
    c=commute_times,                      # Colors based on commute time
    alpha=0.6,                             # Transparency of the points
    edgecolors='w',                        # Edge color of the points
)

# Adding labels and title to the plot
plt.xlabel('Commute Time (minutes)')
plt.ylabel('Job Satisfaction (1-10)')
plt.title('Scatterplot of Employee Commute Times vs. Job Satisfaction')

# Adding a color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Commute Time (minutes)')

# Annotating each point with the corresponding Employee ID
for i, employee_id in enumerate(employee_ids):
    plt.annotate(employee_id, (commute_times[i], job_satisfactions[i]), textcoords="offset points", xytext=(0,5), ha='center')

# Show grid
plt.grid(True)

# Show plot
plt.show()