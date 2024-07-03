
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': pd.date_range(start='2024-01-01', periods=24, freq='MS'),
    'Sales': [5000, 6000, 7500, 8200, 9100, 10000, 9400, 8900, 9500, 10200, 9800, 10400,
              10800, 11500, 12000, 12500, 13200, 13800, 13400, 13000, 14000, 14500, 15000, 16000]
}
df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
plt.fill_between(df['Date'], df['Sales'], color='#4682B4', alpha=0.6)
plt.plot(df['Date'], df['Sales'], color='#1E90FF', alpha=0.8)

plt.title('Monthly Sales Over Two Years', fontsize=20, pad=25)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Sales (in USD)', fontsize=16)

max_sales = df['Sales'].max()
max_date = df['Date'][df['Sales'].idxmax()]
plt.annotate(f'Max Sales: ${max_sales}', xy=(max_date, max_sales), xytext=(max_date, max_sales + 2000),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.show()