
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2024-01-01', periods=36, freq='M').strftime('%Y-%m').tolist(),
    'Sales': [120, 130, 145, 160, 155, 165, 170, 175, 180, 190, 185, 195, 200, 210, 220, 230, 225, 235, 245, 255, 265, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(16, 8))

ax.fill_between(df['Date'], df['Sales'], color='#ff6347', alpha=0.6)

ax.set_title('Monthly Sales Performance Over Three Years', fontsize=18, pad=20)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Sales', fontsize=14)
ax.annotate('Highest Sales', xy=('2026-12', 400), xytext=('2026-06', 450),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

ax.spines['top'].set_color('#DDDDDD')
ax.spines['right'].set_color('#DDDDDD')
ax.spines['left'].set_color('#333333')
ax.spines['bottom'].set_color('#333333')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()