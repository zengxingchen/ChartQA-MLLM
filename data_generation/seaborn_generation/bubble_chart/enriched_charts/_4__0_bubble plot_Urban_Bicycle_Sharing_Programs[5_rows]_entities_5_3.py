
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
    'GDP Growth': [2.3, 6.1, 0.6, 4.2, 1.3,
                   -3.4, 2.3, -4.6, -7.3, -9.7,
                   5.7, 8.1, 2.9, 9.2, 7.4,
                   2.1, 3.0, 1.8, 6.9, 4.0],
    'Global GDP Share': [24.3, 15.5, 4.5, 3.1, 3.3,
                         24.7, 17.8, 4.6, 3.0, 3.2,
                         24.1, 18.0, 4.4, 3.3, 3.4,
                         24.5, 17.8, 4.2, 3.4, 3.3]
}

# Converting data to DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(16, 9))
bubble_chart = sns.scatterplot(data=df, x="Year", y="GDP Growth",
                               hue="Country", size="Global GDP Share",
                               palette=["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f"],
                               sizes=(100, 2000), alpha=0.7)

# Adjust the legend and plot titles
plt.title('GDP Growth by Country', fontsize=18, pad=20)
bubble_chart.legend(loc='upper right', bbox_to_anchor=(1.15, 1), title='Country')
bubble_chart.set_xlabel('Year', fontsize=14)
bubble_chart.set_ylabel('GDP Growth (%)', fontsize=14)

plt.tight_layout()
plt.show()