
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range(start='2024-01-01', periods=48, freq='MS'),
    'Participants': [150, 152, 148, 153, 157, 160, 162, 161, 165, 170, 167, 172,
                     175, 178, 180, 183, 185, 190, 192, 195, 198, 200, 202, 205,
                     208, 210, 212, 215, 217, 220, 222, 225, 227, 230, 232, 235,
                     238, 240, 242, 245, 247, 250, 252, 255, 257, 260, 262, 265]
}
df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))
plt.fill_between(df['Date'], df['Participants'], color='#FF6347', alpha=0.6)
plt.plot(df['Date'], df['Participants'], color='#FF4500', alpha=0.9)

plt.title('Conference Participants Over Time', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Participants', fontsize=14)

max_value = df['Participants'].max()
max_date = df['Date'][df['Participants'].idxmax()]
plt.annotate(f'Max: {max_value}', xy=(max_date, max_value), xytext=(max_date, max_value+10),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.show()