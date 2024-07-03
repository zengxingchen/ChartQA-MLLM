
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
                'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'],
    'Artificial Intelligence': [10.5, 12.7, 14.3, 16.2, 18.5, 20.6, 23.1, 25.8, 28.2, 31.0, 33.4, 36.2],
    'Robotics': [12.3, 15.4, 18.0, 20.1, 22.7, 25.0, 27.8, 30.4, 33.1, 35.8, 38.5, 41.0],
    'Quantum Computing': [8.7, 10.9, 12.5, 14.2, 16.3, 18.4, 20.5, 22.7, 24.9, 27.2, 29.5, 31.8]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

cumulative_revenue = df.cumsum(axis=1)

plt.figure(figsize=(16, 10))

plt.stackplot(df.index, cumulative_revenue['Artificial Intelligence'],
              cumulative_revenue['Robotics'],
              cumulative_revenue['Quantum Computing'],
              labels=['Artificial Intelligence', 'Robotics', 'Quantum Computing'],
              colors=['#003f5c', '#58508d', '#bc5090'], alpha=0.8)

plt.legend(loc='upper left')

plt.annotate('Highest Robotics Revenue', xy=('Q4-2023', cumulative_revenue.loc['Q4-2023', 'Robotics']),
             xytext=(-150, 50), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

plt.title('Technology Quarterly Revenue (in billions)', fontsize=16)
plt.xlabel('Quarter')
plt.ylabel('Revenue')

plt.tight_layout()
plt.show()