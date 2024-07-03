
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate a DataFrame from the given table data
data = {
    "Country": ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan", "Nigeria", "Bangladesh", "Russia", "Mexico", "Japan", "Ethiopia", "Philippines", "Egypt", "Vietnam", "Germany", "South Korea", "France"],
    "Year": [2015] * 18,
    "Population": [1376048943, 1311050527, 321773631, 258705000, 207847528, 188924874, 181562056, 160995642, 146544710, 121736809, 127298000, 99465819, 100699395, 91779522, 91713800, 82000000, 51000000, 67000000],
    "Life Expectancy": [76.25, 68.3, 79.1, 69.1, 75.0, 66.4, 53.1, 71.8, 70.5, 76.7, 83.7, 64.8, 68.5, 71.3, 75.4, 81.0, 82.0, 82.5],
    "GDP per Capita": [8069.21, 1606.02, 55805.2, 3336.29, 8538.08, 1275.29, 2885.13, 1211.73, 9329.29, 9005.18, 34567.78, 632.91, 2950.95, 3308.66, 2102.67, 45000.0, 36500.0, 40000.0]
}

df = pd.DataFrame(data)

# Create a scatter plot with bubble sizes
plt.figure(figsize=(12, 8))
bubble_chart = sns.scatterplot(data=df, x="Life Expectancy", y="GDP per Capita",
                               size="Population", sizes=(50, 1500), alpha=0.7,
                               hue="Population", palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#1f78b4", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f", "#cab2d6", "#6a3d9a", "#b2df8a"])

# Adjust the legend for bubble size
bubble_chart.legend(loc='upper right', bbox_to_anchor=(1.15, 1), title='Population')

# Set title and labels
plt.title('Economic and Demographic Indicators (2015)', y=1.03)
plt.xlabel('Life Expectancy (years)')
plt.ylabel('GDP per Capita (USD)')

# Show the plot
plt.show()