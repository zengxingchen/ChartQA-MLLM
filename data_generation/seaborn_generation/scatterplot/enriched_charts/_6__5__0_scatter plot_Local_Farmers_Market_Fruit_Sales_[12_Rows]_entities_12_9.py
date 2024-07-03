
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'BooksSold': [10, 15, 12, 18, 14, 20, 22, 25, 21, 28, 30, 32, 35, 33, 36,
                  38, 40, 42, 45, 44, 47, 50, 52, 55, 54, 58, 60, 62, 65, 63],
    'Revenue': [100, 150, 120, 180, 140, 200, 220, 250, 210, 280, 300, 320, 350, 330, 360,
                380, 400, 420, 450, 440, 470, 500, 520, 550, 540, 580, 600, 620, 650, 630]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 9))
scatterplot = sns.scatterplot(x='BooksSold', y='Revenue', data=df, color='#1f77b4')

scatterplot.set_title('Relationship Between Books Sold and Revenue', fontsize=18)
scatterplot.set_xlabel('Number of Books Sold', fontsize=15)
scatterplot.set_ylabel('Revenue Generated ($)', fontsize=15)

plt.show()