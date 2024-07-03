
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Country': ['Canada', 'United States', 'Mexico', 'Brazil', 'United Kingdom', 'Germany', 
                'France', 'Italy', 'Russia', 'China', 'India', 'Australia', 'Japan', 
                'South Korea', 'Nigeria', 'Egypt'],
    'Population_Density': [4, 36, 66, 25, 277, 233, 122, 206, 9, 153, 464, 3, 347, 527, 226, 104]
}

df = pd.DataFrame(data)

sns.set_style('whitegrid')

plt.figure(figsize=(14, 8))
ax = sns.barplot(y='Country', x='Population_Density', data=df, palette=['#4c72b0', '#55a868', '#c44e52', 
                                                                        '#8172b3', '#ccb974', '#64b5cd',
                                                                        '#8c564b', '#e377c2', '#7f7f7f',
                                                                        '#bcbd22', '#17becf', '#1f77b4',
                                                                        '#ff7f0e', '#2ca02c', '#d62728',
                                                                        '#9467bd'])

for bar in ax.patches:
    bar.set_height(0.7)

ax.set_title('Population Density by Country (people per sq km)', fontsize=16, pad=20)

plt.show()