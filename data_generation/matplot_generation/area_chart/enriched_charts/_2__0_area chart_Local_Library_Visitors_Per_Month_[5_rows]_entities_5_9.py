
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Steps': [
        3000, 5000, 4500, 7000, 8500, 6000, 6200, 7000, 7500, 8000, 9000, 9500, 10000, 10500, 11000,
        11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))

sns.lineplot(data=df, x='Date', y='Steps', color="#1F77B4")
plt.fill_between(df.Date, df.Steps, color="#1F77B4", alpha=0.3)

for index, value in df.iterrows():
    if index % 5 == 0:
        plt.text(value['Date'], value['Steps'] + 500, f"{value['Steps']} steps", ha='center')

plt.title('Daily Step Count in January 2023', fontsize=16, pad=20)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Steps', fontsize=12)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()