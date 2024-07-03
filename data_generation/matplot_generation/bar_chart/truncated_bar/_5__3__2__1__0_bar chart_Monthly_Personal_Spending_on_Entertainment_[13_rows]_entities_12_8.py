
import matplotlib.pyplot as plt

# Data points
countries = ['Japan', 'Switzerland', 'Australia', 'Spain', 'Italy', 'Iceland', 'Israel', 'France', 
             'Sweden', 'Canada', 'Norway', 'Netherlands', 'New Zealand', 'Austria', 'Ireland', 
             'Germany', 'United Kingdom', 'Belgium', 'Finland', 'Luxembourg', 'South Korea', 
             'Portugal', 'Denmark', 'Greece', 'United States', 'China', 'Brazil', 'Russia', 
             'India', 'South Africa']
avg_monthly_temp = [16.5, 10.2, 21.8, 19.3, 16.4, 6.0, 22.2, 12.8, 7.4, 5.7, 6.3, 11.1, 14.8, 
                    9.8, 9.4, 9.6, 10.3, 10.9, 4.4, 10.6, 13.4, 16.8, 8.3, 18.5, 13.2, 11.8, 
                    24.9, 5.0, 24.3, 17.1]

# Colors for each bar
colors = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c', '#f781bf', '#a65628', '#999999', 
          '#dede00', '#007f7f', '#bf5b17', '#cab2d6', '#6a3d9a', '#b2df8a', '#fb9a99', '#1f78b4', 
          '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a', '#b2df8a', '#cab2d6', '#ffff99', '#a6cee3', 
          '#1f78b4', '#33a02c', '#fb9a99', '#e31a1c', '#ff7f00', '#6a3d9a']

# Create a horizontal bar chart
plt.figure(figsize=(12, 8))
plt.barh(countries, avg_monthly_temp, color=colors, height=0.6)

# Modify the ticks, labels, and title
plt.xlabel('Average Monthly Temperature (°C)')
plt.title('Average Monthly Temperature in Various Countries', pad=20)
plt.xlim(4, 26)  # Truncated x-axis limits

# Display the plot
plt.tight_layout()
plt.show()