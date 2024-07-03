
import matplotlib.pyplot as plt

# Data
countries = ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 
             'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 'Turkey', 'Iran', 'Germany', 'Thailand']
populations = [1444216107, 1393409038, 331883986, 273523621, 225199937, 213993437, 211400708, 166303498, 145912025, 130262221, 
               126050804, 114963583, 109581085, 104258327, 97338583, 89561403, 84339067, 83992953, 83240525, 69799978]

# Colors for each bar
colors = ['#FF0000', '#FF4000', '#FF8000', '#FFBF00', '#FFFF00', '#BFFF00', '#80FF00', '#40FF00', '#00FF00', '#00FF40', 
          '#00FF80', '#00FFBF', '#00FFFF', '#00BFFF', '#0080FF', '#0040FF', '#0000FF', '#4000FF', '#8000FF', '#BF00FF']

# Plotting the bar chart vertically
plt.figure(figsize=(14, 10))
plt.bar(countries, populations, color=colors, edgecolor='black', width=0.6)

# Chart title and labels
plt.title('Population of the Top 20 Most Populated Countries (2023)', fontsize=18)
plt.ylabel('Population', fontsize=14)

# Setting the ylim to truncate the y-axis
plt.ylim(60000000, max(populations) + 100000000)

# Rotating x-axis labels for better readability
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)

# Display the chart
plt.tight_layout()
plt.show()