
import matplotlib.pyplot as plt

# Data for the bar chart
countries = [
    'Canada', 'Russia', 'Germany', 'United Kingdom', 'France', 'Spain', 
    'Italy', 'Greece', 'Turkey', 'Australia', 'Brazil', 'India', 
    'China', 'Japan', 'South Korea', 'Mexico', 'South Africa', 
    'Argentina', 'Nigeria', 'Egypt'
]

average_streaming_hours = [
    35.4, 42.3, 40.1, 38.7, 37.8, 39.6, 41.2, 36.3, 45.1, 37.5, 48.3, 49.2, 
    44.6, 34.7, 50.8, 43.2, 46.5, 42.8, 33.4, 32.1
]

# Modify the color scheme
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', 
    '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', 
    '#dbdb8d', '#9edae5'
]

# Set the figure size for better clarity or visual appeal
plt.figure(figsize=(14, 10))

# Change the direction of the chart from vertical to horizontal
plt.barh(countries, average_streaming_hours, color=colors, height=0.6)

# Add labels and title to the chart
plt.xlabel('Average Monthly Streaming Hours')
plt.title('Average Monthly Streaming Hours by Country', pad=20)

# Display the chart
plt.show()