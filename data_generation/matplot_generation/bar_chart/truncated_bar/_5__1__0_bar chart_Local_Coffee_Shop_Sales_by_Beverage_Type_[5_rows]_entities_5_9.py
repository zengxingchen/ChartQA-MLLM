
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
words_written = [1200, 1500, 1700, 2000, 1800, 1600, 1300]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 8))  # Changed figure size

# Plotting the bar chart horizontally
ax.barh(days, words_written, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2'], height=0.6)  # Changed colors and bar height

# Customizing the plot (labels, title, etc.)
ax.set_xlabel('Words Written')
ax.set_title('Weekly Writing Progress')
ax.set_xlim([1000, 2100])  # Truncated to start from 1000

# Display the plot
plt.tight_layout()
plt.show()