
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': ['Japan', 'Switzerland', 'Spain', 'Australia', 'Italy', 'Canada', 'South Korea', 'Netherlands', 'New Zealand', 'Sweden', 'United Kingdom', 'Germany', 'France', 'Singapore', 'Norway'],
    'Life_Expectancy': [84.6, 83.4, 83.2, 82.8, 82.7, 82.3, 82.1, 81.7, 81.6, 81.5, 81.3, 81.0, 82.4, 83.1, 82.5]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 12))

bar_plot = sns.barplot(
    x='Country',
    y='Life_Expectancy',
    data=df,
    palette=['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF', '#AEC7E8', '#FFBB78', '#98DF8A', '#FF9896', '#C5B0D5'],
    linewidth=1.2,
    edgecolor='black'
)

for bar in bar_plot.patches:
    bar.set_width(0.6)

plt.xlabel('Country')
plt.ylabel('Life Expectancy (Years)')
plt.title('Life Expectancy in Various Countries')
plt.xticks(rotation=90)

plt.show()