
import matplotlib.pyplot as plt

# Data
countries = [
    'United States', 'Germany', 'United Kingdom', 'France', 'Italy', 
    'Spain', 'Greece', 'Brazil', 'India', 'China', 'Japan', 
    'South Korea', 'Australia', 'Canada', 'Russia', 'Turkey'
]

average_daily_screen_time = [
    7.1, 6.8, 6.5, 6.4, 6.2, 6.1, 5.9, 5.8, 5.7, 5.5, 
    5.4, 5.3, 5.2, 5.1, 5.0, 4.9
]

# Modify the color scheme
colors = [
    '#FF6347', '#FF4500', '#FF8C00', '#FFD700', '#ADFF2F', 
    '#7FFF00', '#32CD32', '#00FF00', '#00FA9A', '#00CED1', 
    '#20B2AA', '#4682B4', '#1E90FF', '#4169E1', '#8A2BE2', '#9400D3'
]

# Set the figure size
plt.figure(figsize=(18, 12))

# Change the direction of the chart from vertical to horizontal
plt.barh(countries, average_daily_screen_time, color=colors, height=0.6)

# Set y-axis limits to truncate the chart
plt.xlim(4.5, 7.5)

# Rotate y-axis labels for better readability
plt.yticks(rotation=0, ha='right')

# Add labels and title to the chart
plt.xlabel('Average Daily Screen Time (hours)')
plt.title('Average Daily Screen Time by Country')

# Display the chart
plt.tight_layout()  # Adjust layout to fit all labels and title
plt.show()