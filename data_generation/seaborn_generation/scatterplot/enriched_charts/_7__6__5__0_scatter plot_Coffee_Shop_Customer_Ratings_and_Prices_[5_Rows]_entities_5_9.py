
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Age': [15, 15, 15, 15, 18, 18, 18, 18, 21, 21, 21, 21, 24, 24, 24, 24, 27, 27, 27, 27, 30, 30, 30, 30, 33, 33, 33, 33, 36, 36, 36, 36, 39, 39, 39, 39],
    'Average_Income': [2000, 2200, 2100, 2300, 2500, 2700, 2600, 2800, 3000, 3200, 3100, 3300, 3500, 3700, 3600, 3800, 4000, 4200, 4100, 4300, 4500, 4700, 4600, 4800, 5000, 5200, 5100, 5300, 5500, 5700, 5600, 5800, 6000, 6200, 6100, 6300],
    'Social_Media_Usage': [30, 35, 40, 38, 45, 50, 48, 52, 55, 60, 58, 62, 65, 70, 68, 72, 75, 80, 78, 82, 85, 90, 88, 92, 95, 100, 98, 102, 105, 110, 108, 112, 115, 120, 118, 122],
    'Hours_Spent': [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
scatter_plot = sns.scatterplot(x='Social_Media_Usage', y='Average_Income', hue='Age', palette=['#E74C3C', '#3498DB', '#2ECC71', '#9B59B6', '#F39C12'], data=df)

scatter_plot.set_title('Correlation Between Social Media Usage and Income by Age', fontsize=20, pad=30)
scatter_plot.set_xlabel('Average Social Media Usage (hours/week)', fontsize=14)
scatter_plot.set_ylabel('Average Monthly Income (USD)', fontsize=14)

plt.legend(title='Age Group', loc='upper right', bbox_to_anchor=(1.3, 1))
plt.show()