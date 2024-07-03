import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
steps = [7000, 8500, 6500, 9000, 12000, 11000, 8000]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 8))  # Changed figure size

# Plotting the bar chart
ax.barh(days, steps, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2'], height=0.4)  # Changed colors and bar height

# Customizing the plot (labels, title, etc.)
ax.set_xlabel('Steps Taken')
ax.set_title('Weekly Step Count Data', pad=20)  # Changed title and added padding

# Adjusting the limit to better fit the data
ax.set_xlim([0, 13000])  # Adjusted to accommodate the maximum data point

# Display the plot
plt.tight_layout()
plt.show()