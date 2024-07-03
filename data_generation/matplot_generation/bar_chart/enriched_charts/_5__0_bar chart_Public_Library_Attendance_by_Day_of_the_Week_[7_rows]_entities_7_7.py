
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
heart_rates = [72, 74, 76, 78, 80, 82, 85, 88, 84, 81, 77, 73]
colors = ['#D32F2F', '#C2185B', '#7B1FA2', '#512DA8', '#303F9F', '#1976D2',
          '#0288D1', '#0097A7', '#00796B', '#388E3C', '#689F38', '#AFB42B']

# Create a vertical bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(months, heart_rates, color=colors, edgecolor='black', width=0.5)

# Customizing the plot
plt.ylabel('Average Heart Rate (bpm)')
plt.title('Average Monthly Heart Rate in Adults')
plt.ylim(70, 90)
plt.tight_layout()

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()