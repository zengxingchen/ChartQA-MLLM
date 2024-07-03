
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'City': ['Paris', 'London', 'New York', 'Tokyo', 'Sydney', 'Berlin', 
             'Los Angeles', 'Rome', 'Dubai', 'Singapore', 'Hong Kong', 
             'Amsterdam', 'Toronto', 'Seoul'],
    'Revenue (in Millions)': [500, 450, 475, 430, 420, 410, 440, 435, 455, 
                              460, 470, 425, 415, 450]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
sns.barplot(x='City', y='Revenue (in Millions)', data=df,
            palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
                     '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
                     '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', 
                     '#2ca02c', '#d62728'],
            width=0.6)

plt.xlabel('City')
plt.ylabel('Revenue (in Millions)')
plt.title('Annual Revenue of Major Cities in 2023', pad=20)
sns.despine(left=True, bottom=True)

plt.show()