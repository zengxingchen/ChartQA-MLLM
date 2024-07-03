
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Topic': ['Renewable Energy', 'Climate Change Awareness', 'Recycling Programs', 'Carbon Emissions', 'Electric Vehicles',
              'Sustainable Agriculture', 'Air Quality', 'Water Conservation', 'Biodiversity', 'Deforestation',
              'Ocean Pollution', 'Green Building', 'Waste Management', 'Clean Energy Investments', 'Wildlife Protection',
              'Sustainable Fisheries', 'Urban Green Spaces', 'Renewable Resources', 'Environmental Education', 'Eco-friendly Products'],
    'Importance': [85, 95, 78, 88, 92, 80, 76, 82, 90, 84, 87, 89, 77, 91, 86, 79, 81, 93, 83, 75]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 14))  
barplot = sns.barplot(x='Topic', y='Importance', data=df, color="#FF6347")  

barplot.set(ylim=(0, 100))  
sns.despine(left=True, bottom=True)

plt.title('Environmental Importance Overview', fontsize=18)
plt.xlabel('Topic', fontsize=14)
plt.ylabel('Importance', fontsize=14)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)

plt.show()