
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 'Jun-2021', 'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021', 
             'Nov-2021', 'Dec-2021', 'Jan-2022', 'Feb-2022', 'Mar-2022', 'Apr-2022', 'May-2022', 'Jun-2022', 'Jul-2022', 'Aug-2022', 
             'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022'],
    'Clothing': [4500, 4700, 4900, 5100, 5300, 5500, 5700, 5900, 6100, 6300, 
                 6500, 6700, 6900, 7100, 7300, 7500, 7700, 7900, 8100, 8300, 
                 8500, 8700, 8900, 9100],
    'Footwear': [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 
                 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 
                 5000, 5100, 5200, 5300],
    'Accessories': [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 
                    3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 
                    4000, 4100, 4200, 4300]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 10))
ax.stackplot(df['Date'], df['Clothing'], df['Footwear'], df['Accessories'],
             labels=['Clothing', 'Footwear', 'Accessories'],
             colors=['#FF6347', '#4682B4', '#32CD32'])

plt.title('Monthly Fashion Sales', pad=20)
plt.xlabel('Date')
plt.ylabel('Sales (in units)')
plt.legend(loc='upper left')

for i, (date, clothing, footwear, accessories) in enumerate(zip(df['Date'], df['Clothing'], df['Footwear'], df['Accessories'])):
    total_sales = clothing + footwear + accessories
    ax.annotate(f'Total: {total_sales}', (date, total_sales), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()