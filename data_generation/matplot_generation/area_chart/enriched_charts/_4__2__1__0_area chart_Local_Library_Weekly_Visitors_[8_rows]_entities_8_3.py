
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': pd.date_range(start='2024-01-01', periods=24, freq='MS'),
    'Visitors': [150, 160, 180, 220, 300, 350, 400, 420, 380, 320, 280, 200, 
                 170, 180, 190, 230, 310, 360, 410, 430, 390, 330, 290, 210]
}
df = pd.DataFrame(data)

plt.figure(figsize=(16, 9))
plt.fill_between(df['Date'], df['Visitors'], color='#1E90FF', alpha=0.6)
plt.plot(df['Date'], df['Visitors'], color='#00008B', alpha=0.8)

plt.title('Monthly Visitor Statistics Over Two Years', fontsize=20, pad=30)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Number of Visitors', fontsize=16)

max_visitors = df['Visitors'].max()
max_date = df['Date'][df['Visitors'].idxmax()]
plt.annotate(f'Max Visitors: {max_visitors}', xy=(max_date, max_visitors), xytext=(max_date, max_visitors + 50),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.show()