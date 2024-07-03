
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = {
    "Year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "BooksPublished": [50, 55, 53, 60, 58, 65, 70, 75, 72, 80, 85, 90, 95, 100]
}
df = pd.DataFrame(data)
df['Year'] = pd.Categorical(df['Year'], categories=data['Year'], ordered=True)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the area chart
plt.figure(figsize=(12, 7))
area_chart = sns.lineplot(data=df, x='Year', y='BooksPublished', color="#ff7f0e")

# Filling the area under the line
plt.fill_between(data['Year'], data['BooksPublished'], color="#ffbb78")

# Customize the axes and title
area_chart.set_title('Number of Books Published Over Years', fontsize=18, pad=20)
area_chart.set_xlabel('Year', fontsize=12)
area_chart.set_ylabel('Books Published', fontsize=12)

# Adding annotations
for i, books in enumerate(df['BooksPublished']):
    plt.text(df['Year'][i], books, str(books), horizontalalignment='center')

# Show the plot
plt.tight_layout()
plt.show()