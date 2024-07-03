import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus'],
    'Visitors': [500000, 450000, 300000, 350000, 250000, 270000, 220000, 280000, 330000, 210000, 240000, 200000, 230000, 260000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))

bar_plot = sns.barplot(
    y='City',
    x='Visitors',
    data=df,
    palette=['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8F33', '#33FFB5', '#FF3333', '#339BFF', '#FF57E3', '#33FFD5', '#FFBD33', '#33FF8F', '#FF3357', '#33FF9F'],
    linewidth=1.2,
    edgecolor='black'
)

for bar in bar_plot.patches:
    bar.set_height(0.5)

plt.ylabel('City')
plt.xlabel('Number of Visitors')
plt.title('Number of Tourists Visiting Various Cities in a Year')
plt.yticks(rotation=0)

plt.show()