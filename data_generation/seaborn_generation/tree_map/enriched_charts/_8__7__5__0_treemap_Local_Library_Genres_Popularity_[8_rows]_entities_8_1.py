
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify

# Creating a DataFrame from the provided dataset
data = {
    'Continent': ['Asia', 'Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe', 'Europe', 'Europe',
                  'Africa', 'Africa', 'Africa', 'Africa', 'Africa', 'Americas', 'Americas', 'Americas', 'Americas',
                  'Americas', 'Oceania', 'Oceania', 'Oceania', 'Oceania', 'Oceania'],
    'Country': ['China', 'India', 'Japan', 'South Korea', 'Indonesia', 'Germany', 'United Kingdom',
                'France', 'Italy', 'Russia', 'Nigeria', 'South Africa', 'Egypt', 'Algeria', 'Morocco',
                'United States', 'Brazil', 'Canada', 'Mexico', 'Argentina', 'Australia', 'New Zealand',
                'Papua New Guinea', 'Fiji', 'Samoa'],
    'Expenditure': [50000, 45000, 40000, 30000, 25000, 55000, 45000, 42000, 38000, 36000,
                    20000, 18000, 16000, 15000, 14000, 70000, 35000, 30000, 28000, 26000,
                    32000, 29000, 20000, 15000, 10000]
}

df = pd.DataFrame(data)

# Plotting the treemap
plt.figure(figsize=(28, 18))
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b",
          "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#1f77b4", "#ff7f0e",
          "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f",
          "#bcbd22", "#17becf", "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

# Using squarify to plot treemap
squarify.plot(sizes=df['Expenditure'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Food & Nutrition Expenditure by Country', fontsize=28, y=1.05)
plt.axis('off')
plt.show()