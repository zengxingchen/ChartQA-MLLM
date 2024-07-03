
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India',
                'United Kingdom', 'France', 'Brazil', 'Canada', 'Russia',
                'Australia', 'South Korea', 'Italy', 'Mexico', 'Spain'],
    'Book_Published': [300000, 220000, 150000, 80000, 200000, 70000, 60000, 50000, 40000, 70000, 30000, 35000, 30000, 45000, 40000],
    'Library_Count': [100000, 60000, 15000, 5000, 70000, 25000, 22000, 18000, 24000, 15000, 15000, 10000, 12000, 18000, 14000],
    'Population_Millions': [331, 1441, 126, 83, 1380, 68, 65, 213, 38, 146, 25, 52, 60, 129, 47]
})

data['Books_Per_Capita'] = data['Book_Published'] / data['Population_Millions']

sns.set(style='whitegrid')

plt.figure(figsize=(18, 14))
bubble = sns.scatterplot(data=data, x='Book_Published', y='Library_Count',
                         size='Books_Per_Capita', hue='Books_Per_Capita',
                         palette=['#2E8B57', '#8A2BE2', '#FF6347', '#4682B4'],
                         legend='brief', alpha=0.7, sizes=(100, 2000))

plt.xlabel('Books Published')
plt.ylabel('Library Count')
plt.title('Books Published vs. Library Count by Country', fontsize=16, pad=20)

plt.legend(title='Books Per Capita', loc='upper left', bbox_to_anchor=(1, 1))
plt.show()