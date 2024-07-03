import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Topic': ['Whole Grains', 'Leafy Greens', 'Lean Proteins', 'Dairy Alternatives', 'Fermented Foods', 'Nuts and Seeds', 'Berries', 
              'Citrus Fruits', 'Cruciferous Vegetables', 'Legumes', 'Healthy Fats', 'Spices and Herbs', 'Seafood', 'Eggs', 
              'Plant-based Proteins', 'Hydration', 'Organic Produce', 'Probiotics', 'Superfoods', 'Fiber-rich Foods'],
    'Popularity': [80, 90, 85, 75, 78, 82, 88, 81, 83, 77, 84, 79, 87, 76, 89, 92, 93, 91, 86, 95]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(14, 10))  
barplot = sns.barplot(y='Topic', x='Popularity', data=df, color="#4682B4", ci=None)  

barplot.set(xlim=(0, 100))  
sns.despine(left=True, bottom=True)

plt.title('Popular Healthy Foods Overview', fontsize=18, pad=20)
plt.xlabel('Popularity', fontsize=14)
plt.ylabel('Food Type', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.show()