
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    "Year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "AveragePopularity": [25, 30, 28, 33, 35, 40, 45, 50, 47, 55, 60, 65, 70, 75]
}
df = pd.DataFrame(data)
df['Year'] = pd.Categorical(df['Year'], categories=data['Year'], ordered=True)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the area chart
plt.figure(figsize=(14, 8))
area_chart = sns.lineplot(data=df, x='Year', y='AveragePopularity', color="#1f77b4")

# Filling the area under the line
plt.fill_between(data['Year'], data['AveragePopularity'], color="#aec7e8")

# Customize the axes and title
area_chart.set_title('Popularity of Music Genres Over Years', fontsize=18)
area_chart.set_xlabel('Year', fontsize=12)
area_chart.set_ylabel('Average Popularity', fontsize=12)

# Adding annotations
for i, pop in enumerate(df['AveragePopularity']):
    plt.text(df['Year'][i], pop, str(pop), horizontalalignment='center')

# Show the plot
plt.tight_layout()
plt.show()