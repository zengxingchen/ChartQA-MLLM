
import matplotlib.pyplot as plt

# Data to plot
countries = ['China', 'India', 'USA', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 
             'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 'Turkey', 'Iran', 'Germany', 'Thailand']
populations = [1400, 1360, 331, 273, 225, 213, 206, 166, 146, 128, 126, 114, 109, 102, 97, 89, 85, 83, 83, 70]

# Plot a horizontal bar chart
plt.figure(figsize=(14, 10))  # Width and height of the chart
plt.barh(y=countries, width=populations, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', 
    '#A633FF', '#33FFF0', '#FFBD33', '#FF3333', 
    '#57FF33', '#33A6FF', '#A6FF33', '#5733FF', 
    '#33FFBD', '#FFA633', '#F033FF', '#33FF8E', 
    '#FF5733', '#33A6FF', '#FFBD33', '#33FF57'], 
    height=0.6)  # Band height of the bars

# Set the title and labels
plt.title('Top 20 Most Populated Countries in the World', fontsize=18)
plt.xlabel('Population (in millions)', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.xlim(50, 1500)  # Truncated y-axis

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()