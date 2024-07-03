
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Country': ['USA', 'China', 'Germany', 'India', 'UK',
                'USA', 'China', 'Germany', 'India', 'UK',
                'USA', 'China', 'Germany', 'India', 'UK',
                'USA', 'China', 'Germany', 'India', 'UK',
                'USA', 'China', 'Germany', 'India', 'UK'],
    'Year': [2019, 2019, 2019, 2019, 2019,
             2020, 2020, 2020, 2020, 2020,
             2021, 2021, 2021, 2021, 2021,
             2022, 2022, 2022, 2022, 2022,
             2023, 2023, 2023, 2023, 2023],
    'Popularity': [65, 80, 45, 60, 50,
                   70, 85, 55, 62, 48,
                   75, 90, 52, 68, 55,
                   80, 95, 50, 72, 58,
                   85, 98, 57, 75, 62],
    'Percentage Share': [25.3, 15.5, 4.5, 3.1, 3.3,
                         24.7, 17.8, 4.6, 3.0, 3.2,
                         24.1, 18.0, 4.4, 3.3, 3.4,
                         24.5, 17.8, 4.2, 3.4, 3.3,
                         24.2, 18.2, 4.3, 3.5, 3.4]
}

# Converting data to DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=df, x="Year", y="Popularity",
                               hue="Country", size="Percentage Share",
                               palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"],
                               sizes=(100, 2000), alpha=0.7)

# Adjust the legend and plot titles
plt.title('Music Popularity by Country (2019-2023)', fontsize=20, pad=30)
bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Country')
bubble_chart.set_xlabel('Year', fontsize=16)
bubble_chart.set_ylabel('Popularity Index', fontsize=16)

plt.tight_layout()
plt.show()