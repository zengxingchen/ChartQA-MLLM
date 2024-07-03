
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': pd.date_range(start='2023-05-01', periods=61, freq='D'),
    'Stock_Price': [
        150, 158, 157, 165, 170, 175, 172, 180, 185, 190, 195, 205, 210, 200, 210,
        220, 230, 225, 235, 245, 255, 260, 265, 270, 280, 290, 300, 310, 305, 315,
        325, 335, 340, 345, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450,
        460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df['Date'], df['Stock_Price'], color='#1f77b4', alpha=0.6)
plt.plot(df['Date'], df['Stock_Price'], color='#ff7f0e', alpha=0.9)

plt.title('Stock Price Over Time', fontsize=20, pad=20)
plt.xlabel('Date')
plt.ylabel('Stock Price ($)')

plt.annotate('Peak Price', xy=(pd.Timestamp('2023-06-30'), 610), xytext=(pd.Timestamp('2023-06-20'), 540),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12, ha='center')

plt.tight_layout()
plt.show()