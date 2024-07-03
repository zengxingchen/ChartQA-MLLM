
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'],
    'Apple': [20.15, 25.67, 30.70, 35.88, 40.55, 45.20, 50.25, 55.70, 60.90, 65.80, 70.95, 75.50],
    'Google': [30.45, 35.50, 38.55, 41.20, 45.30, 48.70, 52.10, 55.30, 58.60, 61.40, 65.10, 68.50],
    'Amazon': [40.50, 45.60, 50.75, 55.90, 60.80, 65.70, 70.85, 75.95, 80.05, 85.25, 90.45, 95.75]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

cumulative_revenue = df.cumsum(axis=1)

plt.figure(figsize=(14, 8))

plt.stackplot(df.index, cumulative_revenue['Apple'], cumulative_revenue['Google'], cumulative_revenue['Amazon'],
              labels=['Apple', 'Google', 'Amazon'],
              colors=['#FF5733', '#33FF57', '#3357FF'], alpha=0.8)

plt.legend(loc='upper left')

plt.annotate('Highest Market Share', xy=('Q4-2023', cumulative_revenue.loc['Q4-2023', 'Amazon']),
             xytext=(-50, -30), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

plt.title('Quarterly Market Share of Three Tech Companies')
plt.xlabel('Quarter')
plt.ylabel('Market Share (in billions)')

plt.tight_layout()
plt.show()