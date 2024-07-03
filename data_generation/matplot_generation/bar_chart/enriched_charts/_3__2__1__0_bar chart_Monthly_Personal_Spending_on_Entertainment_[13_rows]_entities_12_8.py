
import matplotlib.pyplot as plt

# Data points
countries = ['Japan', 'Switzerland', 'Australia', 'Spain', 'Italy', 'Iceland', 'Israel', 'France', 
             'Sweden', 'Canada', 'Norway', 'Netherlands', 'New Zealand', 'Austria', 'Ireland', 
             'Germany', 'United Kingdom', 'Belgium', 'Finland', 'Luxembourg', 'South Korea', 
             'Portugal', 'Denmark', 'Greece', 'United States', 'China', 'Brazil', 'Russia', 
             'India', 'South Africa']
life_expectancy = [84.6, 83.4, 83.3, 83.1, 83.0, 82.9, 82.8, 82.4, 82.3, 82.2, 82.1, 81.8, 81.6, 
                   81.5, 81.4, 81.2, 81.1, 81.0, 80.9, 80.8, 80.7, 80.5, 80.4, 80.3, 78.9, 76.9, 
                   75.7, 72.4, 69.7, 64.0]

# Colors for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
          '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', 
          '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5', '#2b83ba', '#abdda4', '#fdae61', '#d73027', 
          '#4575b4', '#91bfdb', '#fee08b', '#d73027', '#f46d43', '#e0f3f8']

# Create a vertical bar chart
plt.figure(figsize=(14, 10))
plt.bar(countries, life_expectancy, color=colors, width=0.5)

# Modify the ticks, labels, and title
plt.ylabel('Life Expectancy (Years)')
plt.title('Life Expectancy in Various Countries')
plt.ylim(60, 90)  # Assuming the life expectancy ranges between 60 and 90 years
plt.xticks(rotation=90)

# Display the plot
plt.tight_layout()
plt.show()