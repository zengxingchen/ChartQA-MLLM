
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': pd.date_range(start='2023-06-01', periods=30, freq='D'),
    'Visitors': [150, 160, 158, 165, 170, 175, 180, 185, 190, 195, 200, 210, 220, 230, 240, 235, 245, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
plt.fill_between(df['Date'], df['Visitors'], color='#FF5733', alpha=0.5)
plt.plot(df['Date'], df['Visitors'], color='#C70039', alpha=0.8)

plt.title('Visitor Count Over June 2023', fontsize=18, pad=25)
plt.xlabel('Date')
plt.ylabel('Number of Visitors')

plt.annotate('Peak Visitor Count', xy=(pd.Timestamp('2023-06-30'), 370), xytext=(pd.Timestamp('2023-06-25'), 330),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, ha='center')

plt.tight_layout()
plt.show()