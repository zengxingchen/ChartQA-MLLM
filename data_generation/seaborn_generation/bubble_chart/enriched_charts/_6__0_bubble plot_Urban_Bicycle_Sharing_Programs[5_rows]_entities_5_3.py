
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Company': ['Amazon', 'Google', 'Microsoft', 'Facebook', 'Apple',
                'Amazon', 'Google', 'Microsoft', 'Facebook', 'Apple',
                'Amazon', 'Google', 'Microsoft', 'Facebook', 'Apple'],
    'Year': [2020, 2020, 2020, 2020, 2020,
             2021, 2021, 2021, 2021, 2021,
             2022, 2022, 2022, 2022, 2022],
    'Revenue': [386, 182, 143, 86, 274,
                469, 257, 168, 118, 365,
                514, 279, 198, 136, 394],
    'MarketShare': [40, 19, 15, 9, 30,
                    42, 23, 17, 11, 32,
                    44, 24, 19, 12, 34]
}

# Converting data to DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(16, 8))
bubble_chart = sns.scatterplot(data=df, x="Year", y="Revenue",
                               hue="Company", size="MarketShare",
                               palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FF8F33"],
                               sizes=(100, 2000), alpha=0.7)

# Adjust the legend and plot titles
plt.title('Company Revenues by Year', fontsize=18)
bubble_chart.legend(loc='upper right', bbox_to_anchor=(1.15, 1), title='Company')
bubble_chart.set_xlabel('Year', fontsize=14)
bubble_chart.set_ylabel('Revenue (in billions)', fontsize=14)

plt.tight_layout()
plt.show()