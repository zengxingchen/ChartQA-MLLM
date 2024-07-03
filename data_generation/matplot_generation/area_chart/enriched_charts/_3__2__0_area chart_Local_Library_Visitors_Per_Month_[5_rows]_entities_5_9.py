
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Calories': [
        2000, 2200, 2500, 2400, 2700, 2300, 2100, 2600, 2500, 2700, 2800, 2900, 3100, 3200, 3300, 3400, 3500,
        3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))

sns.lineplot(data=df, x='Date', y='Calories', color="#FF6347")
plt.fill_between(df.Date, df.Calories, color="#FF6347", alpha=0.3)

for index, value in df.iterrows():
    if index % 5 == 0:
        plt.text(value['Date'], value['Calories'] + 100, f"{value['Calories']} cal", ha='center')

plt.title('Daily Caloric Intake in January 2023', fontsize=18, pad=30)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Calories', fontsize=14)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()