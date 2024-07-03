
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Visitors': [
        100, 120, 140, 130, 160, 180, 150, 200, 220, 210, 230, 250, 240, 260, 270, 290, 310, 300, 320, 340, 330, 350, 370, 360, 380, 400, 390, 410, 430, 450, 470
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))

plt.plot(df['Date'], df['Visitors'], color="#FF5733")
plt.fill_between(df['Date'], df['Visitors'], color="#FF5733", alpha=0.4)

for index, value in df.iterrows():
    plt.text(value['Date'], value['Visitors'] + 10, f"{value['Visitors']}", ha='center')

plt.title('Daily Foot Traffic to Fashion Boutique in January 2023', fontsize=18, pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Visitors', fontsize=14)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()