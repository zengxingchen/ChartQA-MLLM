
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 
             2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'Number_of_Species': [85, 90, 95, 100, 110, 120, 125, 130, 135, 140, 
                          150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]
}

df = pd.DataFrame(data)

# Define the color palette as an array of hex color codes
colors = ["#4682B4"]

# Plotting the area chart
plt.figure(figsize=(14, 8))
ax = sns.lineplot(x='Year', y='Number_of_Species', data=df, color=colors[0])
ax.fill_between(df['Year'], df['Number_of_Species'], color=colors[0], alpha=0.3)

# Annotations
for i, point in df.iterrows():
    ax.text(point['Year'], point['Number_of_Species'], str(point['Number_of_Species']), 
            ha='center', va='bottom')

# Customizing with a title and labels
ax.set_title('Biodiversity Increase Over Time', fontsize=18, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Species', fontsize=14)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()