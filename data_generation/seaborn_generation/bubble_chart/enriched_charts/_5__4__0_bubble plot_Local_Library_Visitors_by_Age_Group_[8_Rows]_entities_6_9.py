
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India',
                'United Kingdom', 'France', 'Brazil', 'Canada', 'Russia',
                'Australia', 'South Korea', 'Italy', 'Mexico', 'Spain'],
    'GDP_Billion': [21430, 14340, 5080, 3860, 2870, 2830, 2720, 1840, 1730, 1700, 1390, 1630, 2000, 1220, 1390],
    'Innovation_Index': [85, 75, 80, 83, 65, 82, 78, 60, 79, 68, 81, 84, 77, 59, 76],
    'Technology_Adoption': [80, 70, 85, 90, 60, 88, 82, 55, 84, 63, 85, 87, 80, 58, 78],
    'Population_Millions': [331, 1441, 126, 83, 1380, 68, 65, 213, 38, 146, 25, 52, 60, 129, 47],
    'Research_Expenditure_Per_Capita': [1500, 1000, 1200, 1400, 500, 1300, 1250, 400, 1350, 800, 1450, 1300, 1100, 350, 1150]
})

data['Technology_Ratio'] = data['Research_Expenditure_Per_Capita'] / data['Technology_Adoption']

sns.set(style='whitegrid')

plt.figure(figsize=(14, 10))
bubble = sns.scatterplot(data=data, x='GDP_Billion', y='Innovation_Index',
                         size='Technology_Ratio', hue='Technology_Ratio',
                         palette=['#FF0000', '#00FF00', '#0000FF', '#FFA500', '#800080'],
                         legend='brief', alpha=0.7, sizes=(100, 2500))

plt.xlabel('GDP in Billions of USD')
plt.ylabel('Innovation Index')
plt.title('Innovation and Technology Adoption in Major Economies')
plt.legend(loc='upper left', title='Technology Ratio')

plt.show()