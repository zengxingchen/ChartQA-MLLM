
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
             "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
             "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
             "Indianapolis", "Seattle", "Denver", "Boston", "El Paso",
             "Detroit", "Nashville", "Memphis", "Portland", "Las Vegas", 
             "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson"],
    "LifeExpectancy": [81.2, 80.3, 77.5, 78.1, 79.0, 
                       77.9, 80.1, 81.0, 78.5, 82.2, 
                       79.7, 76.9, 78.8, 77.3, 78.4, 
                       76.5, 82.0, 80.5, 82.5, 79.1, 
                       75.9, 77.0, 75.5, 81.7, 78.0, 
                       76.7, 76.8, 76.2, 79.2, 79.8],
    "AnnualHealthExpenditure": [6500, 6100, 5900, 6200, 5700, 
                                6300, 5500, 6800, 6000, 6900, 
                                5400, 5200, 5800, 5600, 6000, 
                                5300, 7200, 7000, 7300, 5100, 
                                4900, 5700, 5000, 6600, 5900, 
                                5200, 5600, 5400, 5800, 5500]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 7))

scatter_plot = sns.scatterplot(x="LifeExpectancy", y="AnnualHealthExpenditure", data=df, s=100,
                               palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
                                        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"],
                               hue="City", legend=False)

scatter_plot.set_title("Life Expectancy and Annual Health Expenditure by City")
scatter_plot.set_xlabel("Life Expectancy (years)")
scatter_plot.set_ylabel("Annual Health Expenditure (USD)")

plt.show()