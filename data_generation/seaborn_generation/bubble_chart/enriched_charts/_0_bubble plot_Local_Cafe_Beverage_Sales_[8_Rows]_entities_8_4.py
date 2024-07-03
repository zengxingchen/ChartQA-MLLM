
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# We'll create a DataFrame using the copied data
data = {
    'Country': ['Afghanistan', 'Afghanistan', 'Afghanistan', 'Afghanistan', 'Afghanistan',
                'Brazil', 'Brazil', 'Brazil', 'Brazil', 'Brazil',
                'China', 'China', 'China', 'China', 'China',
                'France', 'France', 'France', 'France', 'France',
                'India', 'India', 'India', 'India', 'India',
                'USA', 'USA', 'USA', 'USA', 'USA'],
    'Year': [2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2008, 2012, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020,
             2000, 2005, 2010, 2015, 2020],
    'Population': [20040000, 25000000, 29120000, 32527000, 38928000,
                   174800000, 186110000, 190010000, 194500000, 211050000,
                   1262645000, 1303720000, 1338300000, 1371220000, 1439324000,
                   59278000, 60980000, 62844000, 64338000, 65273000,
                   1006300000, 1107800000, 1234280000, 1310152000, 1380004000,
                   282160000, 295515000, 309321000, 321368000, 331002000],
    'Economy_Score': [300, 350, 400, 420, 410,
                      2000, 2600, 3000, 3200, 3300,
                      1200, 2400, 4000, 8000, 10000,
                      2900, 3400, 3600, 3800, 3900,
                      450, 790, 1350, 1600, 1900,
                      5200, 7900, 8500, 18000, 21000]
}

df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(10, 6))
bubble = sns.scatterplot(data=df, x="Year", y="Population", size="Economy_Score", 
                         hue="Country", sizes=(20, 2000), 
                         palette=["#3498db","#e74c3c","#2ecc71","#f1c40f","#9b59b6","#34495e"])

# Customizing the plot
bubble.set_title('Economic Score and Population Over Years by Country')
bubble.set_xlabel('Year')
bubble.set_ylabel('Population')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid(True)
plt.show()