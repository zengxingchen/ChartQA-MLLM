
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'City': ['New York', 'Los Angeles', 'Tokyo', 'London', 'Paris', 'Beijing', 'Sydney', 'Cape Town', 'Mumbai', 'Mexico City', 'Rio de Janeiro', 'Cairo'],
    'Views': [5000, 3000, 8000, 6000, 7000, 2000, 9000, 1000, 7500, 8500, 5500, 6500],
    'Category': ['Tech', 'Health', 'Travel', 'Education', 'Food', 'Tech', 'Health', 'Travel', 'Education', 'Food', 'Tech', 'Health']
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))

ax = sns.barplot(
    data=df,
    x='Views',
    y='City',
    hue='Category',
    palette=['#FF5733', '#3366FF', '#FF33CC', '#33FF57', '#FFC300'],
    dodge=False,
    edgecolor='.2'
)

ax.bar_label(ax.containers[0], padding=3)
plt.xlabel('Views')
plt.ylabel('City')
plt.title('Views by Category for Various Cities', pad=20, loc='left')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()