
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Country': ['USA', 'China', 'Germany', 'India', 'UK',
                'USA', 'China', 'Germany', 'India', 'UK',
                'USA', 'China', 'Germany', 'India', 'UK',
                'USA', 'China', 'Germany', 'India', 'UK'],
    'Year': [2019, 2019, 2019, 2019, 2019,
             2020, 2020, 2020, 2020, 2020,
             2021, 2021, 2021, 2021, 2021,
             2022, 2022, 2022, 2022, 2022],
    'Participation Rate': [35.0, 30.0, 25.0, 20.0, 22.0,
                           36.0, 31.0, 24.0, 21.0, 23.0,
                           34.0, 32.0, 26.0, 22.0, 21.0,
                           33.0, 30.0, 27.0, 23.0, 20.0],
    'Average Duration': [120.0, 90.0, 100.0, 80.0, 70.0,
                         130.0, 85.0, 95.0, 75.0, 72.0,
                         140.0, 95.0, 105.0, 78.0, 74.0,
                         150.0, 100.0, 110.0, 82.0, 76.0]
}

# Converting data to DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(16, 10))
bubble_chart = sns.scatterplot(data=df, x="Year", y="Participation Rate",
                               hue="Country", size="Average Duration",
                               palette=["#4c72b0", "#dd8452", "#55a868", "#c44e52", "#8172b3"],
                               sizes=(100, 2000), alpha=0.7)

# Adjust the legend and plot titles
plt.title('Participation Rate in Music Events by Country', fontsize=18, pad=20)
bubble_chart.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Country')
bubble_chart.set_xlabel('Year', fontsize=14)
bubble_chart.set_ylabel('Participation Rate (%)', fontsize=14)

plt.tight_layout()
plt.show()