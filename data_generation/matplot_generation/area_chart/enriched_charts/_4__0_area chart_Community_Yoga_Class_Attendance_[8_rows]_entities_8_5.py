
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Rainfall': [78, 68, 90, 105, 115, 130, 150, 145, 110, 95, 85, 70]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
sns.set(style="whitegrid")

colors = ["#1f77b4"]

area_plot = sns.lineplot(data=df, x='Month', y='Average_Rainfall', color=colors[0])
area_plot.fill_between(df['Month'], df['Average_Rainfall'], alpha=0.3, color=colors[0])

for index, row in df.iterrows():
    plt.text(row['Month'], row['Average_Rainfall'] + 3, round(row['Average_Rainfall'], 2), 
             color='black', ha="center")

plt.title('Average Monthly Rainfall in City XYZ', fontsize=18, y=1.05)
plt.xlabel('Month')
plt.ylabel('Average Rainfall (mm)')

plt.show()