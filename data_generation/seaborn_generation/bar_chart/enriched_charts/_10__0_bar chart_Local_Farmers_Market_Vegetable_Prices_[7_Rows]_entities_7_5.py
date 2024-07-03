
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte'],
    'average_sleep': [6.8, 7.2, 6.9, 7.1, 7.0, 6.7, 7.3, 7.4, 6.8, 7.1, 7.2, 6.9, 6.8, 7.0, 7.2]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 12))
barplot = sns.barplot(
    x='city',
    y='average_sleep',
    data=df,
    palette=['#FF5733', '#33FF57', '#3357FF', '#57FFF3', '#F3FF57', '#FF5733', '#33FF57', '#3357FF', '#57FFF3',
             '#F3FF57', '#FF5733', '#33FF57', '#3357FF', '#57FFF3', '#F3FF57'],
    orient='v'
)

for bar in barplot.patches:
    bar.set_width(0.6)

plt.title('Average Hours of Sleep per Night in Different Cities', fontsize=16, pad=20)
plt.xlabel('City', fontsize=14)
plt.ylabel('Average Sleep (hours)', fontsize=14)
plt.xticks(rotation=90)

plt.show()