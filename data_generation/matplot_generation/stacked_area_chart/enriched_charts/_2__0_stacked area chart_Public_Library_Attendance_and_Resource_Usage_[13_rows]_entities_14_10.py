
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date': ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 'Jun-2021', 'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021', 
             'Nov-2021', 'Dec-2021', 'Jan-2022', 'Feb-2022', 'Mar-2022', 'Apr-2022', 'May-2022', 'Jun-2022', 'Jul-2022', 'Aug-2022', 
             'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022'],
    'Fruits': [5000, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 
               10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 
               15500, 16000, 16500, 17000],
    'Vegetables': [7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 
                   12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500, 
                   17000, 17500, 18000, 18500],
    'Dairy': [3000, 3200, 3500, 4000, 4200, 4500, 4800, 5000, 5200, 5500, 
              5800, 6000, 6200, 6500, 6800, 7000, 7300, 7500, 7800, 8000, 
              8300, 8500, 8800, 9000]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(df['Date'], df['Fruits'], df['Vegetables'], df['Dairy'],
             labels=['Fruits', 'Vegetables', 'Dairy'],
             colors=['#FF5733', '#33FF57', '#3357FF'])

plt.title('Monthly Food Consumption', pad=20)
plt.xlabel('Date')
plt.ylabel('Consumption (in kg)')
plt.legend(loc='upper right')

for i, (date, fruits, vegetables, dairy) in enumerate(zip(df['Date'], df['Fruits'], df['Vegetables'], df['Dairy'])):
    total_consumption = fruits + vegetables + dairy
    ax.annotate(f'Total: {total_consumption}', (date, total_consumption), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()