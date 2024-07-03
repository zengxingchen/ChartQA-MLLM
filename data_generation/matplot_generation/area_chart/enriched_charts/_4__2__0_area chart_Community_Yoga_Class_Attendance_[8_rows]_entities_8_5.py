
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'Month': ['2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06', '2021-07', '2021-08', '2021-09', '2021-10', '2021-11', '2021-12', 
              '2022-01', '2022-02', '2022-03', '2022-04', '2022-05', '2022-06', '2022-07', '2022-08', '2022-09', '2022-10', '2022-11', '2022-12',
              '2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12'],
    'Energy Consumption': [320, 310, 350, 400, 380, 410, 450, 420, 430, 440, 460, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 
                           610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 8))
sns.set(style="whitegrid")

colors = ["#1f77b4"]

area_plot = sns.lineplot(data=df, x='Month', y='Energy Consumption', color=colors[0])
area_plot.fill_between(df['Month'], df['Energy Consumption'], alpha=0.4, color=colors[0])

for index, row in df.iterrows():
    plt.text(index, row['Energy Consumption'] + 5, round(row['Energy Consumption'], 2), 
             color='black', ha="center", fontsize=8)

plt.title('Monthly Energy Consumption in XYZ City (2021-2023)', fontsize=18, pad=30)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Energy Consumption (in GWh)', fontsize=14)
plt.xticks(rotation=45)

plt.show()