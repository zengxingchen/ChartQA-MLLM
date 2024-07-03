
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
                'France', 'Brazil', 'Italy', 'Canada', 'Russia', 'South Korea', 
                'Spain', 'Australia', 'Mexico', 'Indonesia', 'Netherlands', 
                'Saudi Arabia', 'Turkey', 'Switzerland', 'Norway', 'Sweden', 'Denmark'],
    'Protein Intake (g/day)': [91, 85, 89, 92, 55, 88,
                               90, 72, 89, 91, 77, 88, 
                               87, 91, 78, 60, 92, 75, 
                               80, 91, 93, 92, 91],
    'Caloric Intake (kcal/day)': [3682, 2990, 2800, 3500, 2230, 3450,
                                  3460, 3010, 3370, 3550, 3100, 3000, 
                                  3300, 3450, 2800, 2600, 3400, 3200, 
                                  2950, 3500, 3600, 3400, 3350],
    'Population (Millions)': [331, 1438, 126, 83, 1367, 66,
                              65, 213, 60, 38, 145, 51,
                              47, 25, 128, 273, 17,
                              34, 84, 8, 5, 10, 6]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 14))
bubble_chart = sns.scatterplot(data=df,
                               x='Caloric Intake (kcal/day)',
                               y='Protein Intake (g/day)',
                               size='Population (Millions)',
                               hue='Caloric Intake (kcal/day)',
                               palette=['#377eb8', '#ff7f00', '#4daf4a', '#e41a1c', '#984ea3', '#ffff33'],
                               sizes=(50, 1000),
                               alpha=0.8)

plt.title('Nutritional Metrics of Various Countries', pad=20)
plt.xlabel('Caloric Intake (kcal/day)')
plt.ylabel('Protein Intake (g/day)')
plt.legend(loc='upper left', title='Population (Millions)')

plt.show()