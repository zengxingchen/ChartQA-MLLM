
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
                'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'],
    'Revenue from Fiction Books': [15.6, 16.2, 16.8, 17.5, 18.2, 18.8, 19.4, 20.0, 20.7, 21.3, 21.9, 22.5],
    'Revenue from Non-Fiction Books': [22.8, 23.4, 24.0, 24.6, 25.3, 26.0, 26.6, 27.3, 28.0, 28.7, 29.4, 30.0],
    'Revenue from E-books': [10.5, 11.0, 11.5, 12.0, 12.6, 13.1, 13.7, 14.3, 14.9, 15.4, 16.0, 16.5]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

cumulative_revenue = df.cumsum(axis=1)

plt.figure(figsize=(14, 8))

plt.stackplot(df.index, cumulative_revenue['Revenue from Fiction Books'],
              cumulative_revenue['Revenue from Non-Fiction Books'],
              cumulative_revenue['Revenue from E-books'],
              labels=['Fiction Books', 'Non-Fiction Books', 'E-books'],
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.85)

plt.legend(loc='upper left')
plt.annotate('Peak Fiction Book Revenue', xy=('Q4-2023', cumulative_revenue.loc['Q4-2023', 'Revenue from Fiction Books']),
             xytext=(-100, 30), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

plt.title('Quarterly Revenue from Book Sales (in millions)', fontsize=16, y=1.05)
plt.xlabel('Quarter')
plt.ylabel('Revenue (in millions)')

plt.tight_layout()
plt.show()