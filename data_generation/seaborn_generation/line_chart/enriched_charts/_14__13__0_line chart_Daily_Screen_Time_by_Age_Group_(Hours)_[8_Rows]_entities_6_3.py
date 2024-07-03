
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Day': [i for i in range(1, 32)],
    'Steps_Taken': [
        3000, 3100, 2900, 3050, 3200, 3100, 3300, 3400, 3500, 3450,
        3550, 3600, 3700, 3650, 3750, 3800, 3850, 3750, 3900, 3950,
        4000, 4050, 4100, 4200, 4150, 4250, 4300, 4350, 4400, 4450, 4500
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))

sns.lineplot(x='Day', y='Steps_Taken', data=df, color='#1E90FF')

for day, steps in zip(data['Day'], data['Steps_Taken']):
    if day == 15:  
        plt.text(day, steps, f"{steps} steps", fontsize=9, ha='center')

plt.title('Daily Steps Taken Trend over a Month', fontsize=20, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Steps Taken', fontsize=14)

plt.show()