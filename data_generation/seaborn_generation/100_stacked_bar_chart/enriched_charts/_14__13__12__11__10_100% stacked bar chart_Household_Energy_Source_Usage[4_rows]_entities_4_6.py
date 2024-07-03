
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2019, 'Research (%)': 20, 'Development (%)': 25, 'Marketing (%)': 30, 'Sales (%)': 15, 'Support (%)': 10},
    {'Year': 2020, 'Research (%)': 22, 'Development (%)': 20, 'Marketing (%)': 28, 'Sales (%)': 18, 'Support (%)': 12},
    {'Year': 2021, 'Research (%)': 25, 'Development (%)': 18, 'Marketing (%)': 30, 'Sales (%)': 17, 'Support (%)': 10},
    {'Year': 2022, 'Research (%)': 24, 'Development (%)': 22, 'Marketing (%)': 26, 'Sales (%)': 18, 'Support (%)': 10},
    {'Year': 2023, 'Research (%)': 23, 'Development (%)': 20, 'Marketing (%)': 27, 'Sales (%)': 20, 'Support (%)': 10}
]
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

df_percent = df.div(df.sum(axis=1), axis=0)

ax = df_percent.plot(kind='bar', stacked=True, color=['#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#9C27B0'], figsize=(12, 10), width=0.7)

plt.title('Company Resource Allocation Over Years (Percentage Stacked)', pad=20)
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

plt.legend(title='Departments', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()