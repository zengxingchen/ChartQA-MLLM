
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Topic': ['Artificial Intelligence', 'Quantum Computing', 'Blockchain Technology', 'Cybersecurity', 'Renewable Energy',
              'Biotechnology', 'Space Exploration', 'Autonomous Vehicles', 'Nanotechnology', 'Genomics',
              'Augmented Reality', 'Virtual Reality', 'Robotics', '5G Technology', 'Internet of Things',
              '3D Printing', 'Wearable Technology', 'Clean Water Technology', 'Green Architecture', 'Smart Grids'],
    'Funding': [85, 80, 90, 75, 95, 88, 82, 87, 78, 91, 84, 81, 83, 79, 86, 77, 76, 92, 93, 89]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(16, 12))  
barplot = sns.barplot(x='Funding', y='Topic', data=df, color="#2E8B57", ci=None, width=0.6)

barplot.set(xlim=(0, 100))  
sns.despine(left=True, bottom=True)

plt.title('Funding in Emerging Technologies', fontsize=20, pad=25)
plt.xlabel('Funding (in millions)', fontsize=16)
plt.ylabel('Technology', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.show()