
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperature = [5, 6, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(10, 6))  # Adjusted figure size

# Plotting the vertical bar chart
ax.bar(months, temperature, color=['#ff5733', '#33ff57', '#3357ff', '#ff33a1', '#a133ff', '#33ffa1', '#a1ff33', '#ff5733', '#33ff57', '#3357ff', '#ff33a1', '#a133ff'], width=0.6)  # Changed colors and bar width

# Customizing the plot (labels, title, etc.)
ax.set_ylabel('Temperature (°C)')
ax.set_title('Average Monthly Temperature')
ax.set_ylim([0, 30])  # Adjusted y-axis limit to start from 0 and go up to 30

# Display the plot
plt.tight_layout()
plt.show()