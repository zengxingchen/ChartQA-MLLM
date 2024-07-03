
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2019, 'Math (%)': 30, 'Science (%)': 25, 'History (%)': 20, 'Art (%)': 25},
    {'Year': 2020, 'Math (%)': 28, 'Science (%)': 22, 'History (%)': 25, 'Art (%)': 25},
    {'Year': 2021, 'Math (%)': 27, 'Science (%)': 23, 'History (%)': 25, 'Art (%)': 25},
    {'Year': 2022, 'Math (%)': 26, 'Science (%)': 24, 'History (%)': 25, 'Art (%)': 25}
]
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_percent = df.div(df.sum(axis=1), axis=0)

fig, ax = plt.subplots(figsize=(8, 12))
df_percent.plot(kind='bar', stacked=True, color=['#FF5733', '#33FF57', '#3357FF', '#F1C40F'], ax=ax, width=0.5)

plt.title('Subject Popularity in School Over Years (Percentage Stacked)', pad=20)
plt.xlabel('Year')
plt.ylabel('Percentage %')

for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy() 
    if height > 0:
        ax.text(x + width / 2, 
                y + height / 2, 
                '{:.0%}'.format(height), 
                horizontalalignment='center', 
                verticalalignment='center')

plt.legend(title='Subjects', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()