
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Country': ['Afghanistan', 'Afghanistan', 'Afghanistan', 'Afghanistan', 'Afghanistan',
                'Brazil', 'Brazil', 'Brazil', 'Brazil', 'Brazil',
                'China', 'China', 'China', 'China', 'China',
                'France', 'France', 'France', 'France', 'France',
                'India', 'India', 'India', 'India', 'India',
                'USA', 'USA', 'USA', 'USA', 'USA'],
    'Year': [2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020],
    'Life_Expectancy': [45.6, 48.1, 50.5, 52.9, 54.8,
                        69.3, 70.5, 71.6, 72.8, 74.0,
                        71.4, 72.9, 74.2, 75.7, 77.1,
                        78.8, 79.4, 80.1, 81.2, 82.4,
                        62.2, 63.5, 65.1, 66.8, 68.7,
                        76.8, 77.5, 78.3, 78.9, 79.8],
    'Happiness_Score': [3.5, 3.6, 3.7, 3.9, 4.0,
                        6.7, 6.9, 7.1, 7.2, 7.3,
                        5.8, 6.0, 6.3, 6.5, 6.7,
                        7.8, 7.9, 8.0, 8.1, 8.2,
                        4.3, 4.5, 4.8, 5.0, 5.2,
                        7.2, 7.4, 7.6, 7.7, 7.9]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
bubble = sns.scatterplot(data=df, x="Year", y="Life_Expectancy", size="Happiness_Score", 
                         hue="Country", sizes=(50, 2000), 
                         palette=["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b"])

bubble.set_title('Life Expectancy and Happiness Over Years by Country', fontsize=16)
bubble.set_xlabel('Year', fontsize=14)
bubble.set_ylabel('Life Expectancy', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title='Country')
plt.grid(True)
plt.show()