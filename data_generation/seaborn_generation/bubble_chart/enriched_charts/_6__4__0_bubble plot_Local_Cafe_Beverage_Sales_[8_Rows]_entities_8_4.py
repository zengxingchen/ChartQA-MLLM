
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Country': ['USA', 'USA', 'USA', 'USA', 'USA',
                'China', 'China', 'China', 'China', 'China',
                'India', 'India', 'India', 'India', 'India',
                'Brazil', 'Brazil', 'Brazil', 'Brazil', 'Brazil',
                'France', 'France', 'France', 'France', 'France',
                'Germany', 'Germany', 'Germany', 'Germany', 'Germany'],
    'Year': [2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020],
    'Revenue': [1000, 1500, 2000, 2500, 3000,
                800, 1100, 1600, 2100, 2600,
                500, 700, 1000, 1300, 1700,
                600, 850, 1100, 1400, 1800,
                700, 950, 1300, 1600, 2000,
                900, 1200, 1600, 2000, 2400],
    'Budget': [500, 800, 1200, 1500, 1800,
               400, 600, 900, 1300, 1700,
               200, 350, 500, 700, 1000,
               300, 450, 600, 800, 1100,
               350, 500, 700, 900, 1200,
               450, 700, 900, 1200, 1500]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
bubble = sns.scatterplot(data=df, x="Year", y="Revenue", size="Budget", 
                         hue="Country", sizes=(50, 2000), 
                         palette=["#4c72b0","#55a868","#c44e52","#8172b3","#ccb974","#64b5cd"])

bubble.set_title('Revenue and Budget Over Years by Country', fontsize=20, y=1.05)
bubble.set_xlabel('Year', fontsize=14)
bubble.set_ylabel('Revenue (in millions)', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title='Country')
plt.grid(True)
plt.show()