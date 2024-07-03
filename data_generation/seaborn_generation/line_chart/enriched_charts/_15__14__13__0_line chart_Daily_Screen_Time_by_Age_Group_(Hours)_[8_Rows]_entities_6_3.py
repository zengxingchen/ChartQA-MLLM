
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Day': [i for i in range(1, 32)],
    'Sales_Revenue': [
        200, 220, 210, 215, 230, 240, 235, 245, 250, 260,
        270, 280, 275, 285, 295, 290, 300, 310, 320, 315,
        325, 330, 340, 335, 345, 350, 355, 360, 365, 370, 375
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))

sns.lineplot(x='Day', y='Sales_Revenue', data=df, color='#FF6347')

for day, revenue in zip(data['Day'], data['Sales_Revenue']):
    if day == 20:  
        plt.text(day, revenue, f"${revenue}", fontsize=9, ha='center')

plt.title('Daily Sales Revenue Trend over a Month', fontsize=18, pad=15)
plt.xlabel('Day of the Month', fontsize=12)
plt.ylabel('Sales Revenue ($)', fontsize=12)

plt.show()