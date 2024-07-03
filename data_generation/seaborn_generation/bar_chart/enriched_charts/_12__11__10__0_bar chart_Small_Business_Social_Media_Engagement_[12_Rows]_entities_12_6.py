
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Country': ['Canada', 'United States', 'Mexico', 'Brazil', 'United Kingdom', 'Germany', 
                'France', 'Italy', 'Russia', 'China', 'India', 'Australia', 'Japan', 
                'South Korea', 'Nigeria', 'Egypt', 'Turkey', 'South Africa', 'Saudi Arabia', 'Argentina'],
    'Population_Density': [4, 36, 66, 25, 277, 233, 122, 206, 9, 153, 464, 3, 347, 527, 226, 104, 107, 45, 15, 16]
}

df = pd.DataFrame(data)

sns.set_style('whitegrid')

plt.figure(figsize=(16, 10))
ax = sns.barplot(x='Country', y='Population_Density', data=df, palette=['#FF5733', '#33FF57', '#3357FF', 
                                                                        '#FF33A1', '#33FFF6', '#F3FF33',
                                                                        '#7F33FF', '#FF8C33', '#33FF8C',
                                                                        '#8CFF33', '#FF3357', '#33A1FF',
                                                                        '#5733FF', '#A1FF33', '#FF3333',
                                                                        '#33FF33', '#FFB533', '#337FFF',
                                                                        '#FF33B5', '#33FFBD'])

for bar in ax.patches:
    bar.set_width(0.5)

ax.set_title('Population Density by Country (people per sq km)', fontsize=16, pad=20)

plt.xticks(rotation=90)

plt.show()