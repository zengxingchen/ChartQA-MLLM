
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
    'Revenue Growth': [5.0, 7.5, 2.0, 8.0, 3.5,
                       -2.0, 5.5, 1.0, 6.5, 0.5,
                       6.0, 10.0, 3.5, 9.5, 4.0,
                       4.0, 7.0, 2.5, 8.5, 3.0],
    'Market Share': [35.0, 25.0, 15.0, 10.0, 15.0,
                     36.0, 26.0, 14.0, 11.0, 13.0,
                     34.0, 27.0, 16.0, 12.0, 11.0,
                     33.0, 28.0, 17.0, 13.0, 9.0]
}

# Converting data to DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(14, 8))
bubble_chart = sns.scatterplot(data=df, x="Year", y="Revenue Growth",
                               hue="Country", size="Market Share",
                               palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"],
                               sizes=(100, 2000), alpha=0.7)

# Adjust the legend and plot titles
plt.title('Revenue Growth by Country', fontsize=18, pad=20)
bubble_chart.legend(loc='upper right', bbox_to_anchor=(1.25, 1), title='Country')
bubble_chart.set_xlabel('Year', fontsize=14)
bubble_chart.set_ylabel('Revenue Growth (%)', fontsize=14)

plt.tight_layout()
plt.show()