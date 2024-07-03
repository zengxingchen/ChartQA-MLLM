
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate a DataFrame from the given table data
data = {
    "Country": ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan", "Nigeria", "Bangladesh", "Russia", "Mexico", "Japan", "Ethiopia", "Philippines", "Egypt", "Vietnam", "South Korea", "Turkey", "France", "United Kingdom", "Italy", "Spain"],
    "Year": [2023] * 21,
    "Population": [1427647786, 1393409038, 331002651, 273523615, 212559417, 225199937, 206139589, 169575884, 145912025, 128932753, 125836021, 114963588, 109581078, 104258327, 97338579, 51780579, 85157650, 65426179, 67886011, 60367477, 47351567],
    "Life Expectancy": [77.3, 69.5, 79.5, 71.2, 75.9, 67.5, 54.3, 73.5, 72.6, 76.2, 84.5, 66.2, 70.2, 71.7, 76.3, 83.3, 75.4, 82.5, 81.3, 83.4, 83.1],
    "GDP per Capita": [10510.21, 2256.39, 63179.48, 4349.12, 8920.53, 1556.7, 2366.1, 1879.36, 10279.29, 9780.12, 40258.47, 925.32, 3641.42, 3312.56, 3054.22, 32085.48, 8916.52, 40258.69, 42302.94, 35546.22, 29514.19]
}

df = pd.DataFrame(data)

# Create a scatter plot with bubble sizes
plt.figure(figsize=(12, 8))
bubble_chart = sns.scatterplot(data=df, x="Life Expectancy", y="GDP per Capita",
                               size="Population", sizes=(100, 1500), alpha=0.7,
                               hue="Population", palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"])

# Adjust the legend for bubble size
bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Population')

# Set title and labels
plt.title('Economic and Health Indicators of Selected Countries (2023)')
plt.xlabel('Life Expectancy (years)')
plt.ylabel('GDP per Capita (USD)')

# Show the plot
plt.show()