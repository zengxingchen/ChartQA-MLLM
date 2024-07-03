
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Followers': [100, 150, 120, 180, 140, 200, 220, 250, 210, 280, 300, 320, 350, 330, 360,
                  380, 400, 420, 450, 440, 470, 500, 520, 550, 540, 580, 600, 620, 650, 630],
    'Engagement': [10, 15, 12, 18, 14, 20, 22, 25, 21, 28, 30, 32, 35, 33, 36,
                   38, 40, 42, 45, 44, 47, 50, 52, 55, 54, 58, 60, 62, 65, 63]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 8))
scatterplot = sns.scatterplot(x='Followers', y='Engagement', data=df, color='#ff5733')

scatterplot.set_title('Social Media Engagement vs. Followers Growth', fontsize=18, pad=20)
scatterplot.set_xlabel('Number of Followers', fontsize=15)
scatterplot.set_ylabel('Engagement Activities', fontsize=15)

plt.show()