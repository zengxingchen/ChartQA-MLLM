
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate a DataFrame from the given table data
data = {
    "Country": ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan", "Nigeria", "Bangladesh", "Russia", "Mexico", "Japan", "Ethiopia", "Philippines", "Egypt", "Vietnam"],
    "Year": [2021] * 15,
    "GDP Growth Rate": [8.1, 9.2, 5.7, 3.7, 4.6, 5.6, 3.4, 6.9, 4.8, 4.8, 2.3, 6.3, 5.6, 3.3, 2.6],
    "Unemployment Rate": [5.0, 7.0, 4.2, 6.5, 13.2, 8.5, 32.5, 5.3, 5.5, 3.8, 2.8, 19.6, 6.9, 7.4, 2.7],
    "Inflation Rate": [2.3, 5.5, 6.2, 1.6, 10.0, 9.7, 15.7, 5.6, 8.4, 7.4, 0.9, 21.1, 3.9, 4.5, 2.0],
    "Population": [1444216107, 1393409038, 331893745, 276361783, 213993437, 225199937, 211400708, 166303498, 145912025, 130262216, 125836021, 120812698, 111046913, 104258327, 98168829]
}

df = pd.DataFrame(data)

# Create a scatter plot with bubble sizes
plt.figure(figsize=(12, 8))
bubble_chart = sns.scatterplot(data=df, x="Unemployment Rate", y="GDP Growth Rate",
                               size="Population", sizes=(50, 1000), alpha=0.7,
                               hue="Inflation Rate", palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"])

# Adjust the legend for bubble size
bubble_chart.legend(loc='upper right', bbox_to_anchor=(1.25, 1), title='Population')

# Set title and labels
plt.title('Economic Indicators (2021)')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('GDP Growth Rate (%)')

# Show the plot
plt.show()