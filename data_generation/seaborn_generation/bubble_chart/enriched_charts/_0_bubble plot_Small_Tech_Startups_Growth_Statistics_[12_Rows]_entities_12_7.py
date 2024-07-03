
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate a DataFrame from the given table data
data = {
    "Country": ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan", "Nigeria", "Bangladesh", "Russia", "Mexico", "Japan", "Ethiopia", "Philippines", "Egypt", "Vietnam"],
    "Year": [2015] * 15,
    "Population": [1376048943, 1311050527, 321773631, 258705000, 207847528, 188924874, 181562056, 160995642, 146544710, 121736809, 127298000, 99465819, 100699395, 91779522, 91713800],
    "Life Expectancy": [76.25, 68.3, 79.1, 69.1, 75.0, 66.4, 53.1, 71.8, 70.5, 76.7, 83.7, 64.8, 68.5, 71.3, 75.4],
    "GDP per Capita": [8069.21, 1606.02, 55805.2, 3336.29, 8538.08, 1275.29, 2885.13, 1211.73, 9329.29, 9005.18, 34567.78, 632.91, 2950.95, 3308.66, 2102.67]
}

df = pd.DataFrame(data)

# Create a scatter plot with bubble sizes
plt.figure(figsize=(10, 6))
bubble_chart = sns.scatterplot(data=df, x="Life Expectancy", y="GDP per Capita",
                               size="Population", sizes=(50, 1000), alpha=0.7,
                               hue="Population", palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A6"])

# Adjust the legend for bubble size
bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Population')

# Set title and labels
plt.title('Global Health and Wealth Indicators (2015)')
plt.xlabel('Life Expectancy (years)')
plt.ylabel('GDP per Capita (USD)')

# Show the plot
plt.show()