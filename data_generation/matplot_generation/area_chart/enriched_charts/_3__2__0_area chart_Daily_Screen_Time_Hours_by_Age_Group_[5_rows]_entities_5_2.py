import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Day": list(range(1, 32)),
    "Book_Sales": [500, 700, 600, 800, 750, 900, 1100, 1000, 1300, 1200, 1400, 1600, 1800, 1700, 1900, 2100, 2300, 2200, 2400, 2600, 2500, 2700, 2900, 3100, 3000, 3200, 3400, 3600, 3500, 3700, 3900]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
area_chart = sns.lineplot(data=df, x='Day', y='Book_Sales', color="#1E90FF")
area_chart.fill_between(df['Day'], df['Book_Sales'], color="#1E90FF", alpha=0.4)

plt.annotate('Highest Sales',
             xy=(31, 3900),
             xytext=(25, 4200),
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             )

plt.title('Daily Book Sales in January')
plt.xlabel('Day of the Month')
plt.ylabel('Book Sales')

plt.show()