
import matplotlib.pyplot as plt

# Data
countries = ['Japan', 'Switzerland', 'Spain', 'Singapore', 'France', 'Australia', 'Canada', 'Italy', 'South Korea', 'Norway', 'Sweden', 'New Zealand', 'Germany', 'United Kingdom', 'United States', 'China', 'Brazil', 'India', 'South Africa', 'Nigeria']
carbon_emissions = [9.3, 4.1, 5.8, 34.6, 4.6, 16.5, 15.6, 5.7, 11.5, 8.7, 4.5, 7.3, 9.7, 5.6, 15.3, 7.1, 2.3, 1.9, 8.9, 0.7]

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 14))

bars = ax.barh(countries, carbon_emissions, height=0.5, color=['#1E90FF', '#FF6347', '#32CD32', '#FFD700', '#8A2BE2', '#FF4500', '#5F9EA0', '#A52A2A', '#DC143C', '#D2691E', '#008B8B', '#B8860B', '#00CED1', '#4682B4', '#DAA520', '#6A5ACD', '#7FFF00', '#8B0000', '#4B0082', '#FF69B4'])

# Customizing the plot
ax.set_title('Carbon Emissions by Country (Metric Tons per Capita)', fontsize=20, pad=20)
ax.set_xlabel('Carbon Emissions (Metric Tons per Capita)', fontsize=16)
ax.set_ylabel('Country', fontsize=16)
ax.set_yticklabels(countries, rotation=0, ha='right')

# Set y-axis limits to truncate the bar chart
ax.set_xlim(0, 36)

# Set bar labels to show the carbon emissions values
for bar in bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height()/2, f'{width}', ha='left', va='center')

# Show the plot
plt.tight_layout()
plt.show()