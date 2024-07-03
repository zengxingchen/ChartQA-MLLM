
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from your provided data
data = [
    {'Year': 2008, 'Battery Capacity (mAh)': 900},
    {'Year': 2009, 'Battery Capacity (mAh)': 1000},
    {'Year': 2010, 'Battery Capacity (mAh)': 1200},
    {'Year': 2011, 'Battery Capacity (mAh)': 1500},
    {'Year': 2012, 'Battery Capacity (mAh)': 1800},
    {'Year': 2013, 'Battery Capacity (mAh)': 2100},
    {'Year': 2014, 'Battery Capacity (mAh)': 2400},
    {'Year': 2015, 'Battery Capacity (mAh)': 2700},
    {'Year': 2016, 'Battery Capacity (mAh)': 3000},
    {'Year': 2017, 'Battery Capacity (mAh)': 3300},
    {'Year': 2018, 'Battery Capacity (mAh)': 3600},
    {'Year': 2019, 'Battery Capacity (mAh)': 3900},
    {'Year': 2020, 'Battery Capacity (mAh)': 4200}
]
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Set up the matplotlib figure
plt.figure(figsize=(10, 6))

# Draw the lineplot showing the trend of battery capacities over years
sns.lineplot(x='Year', y='Battery Capacity (mAh)', data=df, marker='o', color='skyblue', lw=3)

# Fill the area under the line
plt.fill_between(x=df['Year'], y1=df['Battery Capacity (mAh)'], color='skyblue', alpha=0.3)

# Customizing the chart with a diversified visual encoding
plt.title("Trend of Battery Capacity over Years", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Battery Capacity (mAh)", fontsize=14)
plt.xticks(df['Year'], rotation=45)  # Rotate x-axis labels for better readability
plt.yticks(fontsize=12)
plt.tight_layout()

# Show the plot
plt.show()