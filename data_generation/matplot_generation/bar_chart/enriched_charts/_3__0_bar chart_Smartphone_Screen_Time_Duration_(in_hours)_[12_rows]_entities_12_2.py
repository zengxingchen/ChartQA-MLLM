
import matplotlib.pyplot as plt

# Data to plot
countries = ['China', 'India', 'USA', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 
             'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam', 'DR Congo', 'Turkey', 'Iran', 'Germany', 'Thailand']
populations = [1400, 1360, 331, 273, 225, 213, 206, 166, 146, 128, 126, 114, 109, 102, 97, 89, 85, 83, 83, 70]

# Plot a vertical bar chart
plt.figure(figsize=(12, 8))  # Width and height of the chart
plt.bar(x=countries, height=populations, color=[
    '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', 
    '#92A8D1', '#955251', '#B565A7', '#009B77', 
    '#DD4124', '#D65076', '#45B8AC', '#EFC050', 
    '#5B5EA6', '#9B2335', '#DFCFBE', '#55B4B0', 
    '#E15D44', '#7FCDCD', '#BC243C', '#C3447A'], 
    width=0.7)  # Band width of the bars

# Set the title and labels
plt.title('Top 20 Most Populated Countries in the World', fontsize=16)
plt.ylabel('Population (in millions)', fontsize=12)
plt.xlabel('Country', fontsize=12)
plt.xticks(rotation=90)

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()