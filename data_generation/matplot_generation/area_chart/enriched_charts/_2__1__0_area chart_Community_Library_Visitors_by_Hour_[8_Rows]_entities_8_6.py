
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [2000, 2300, 2500, 2800, 3000, 3200, 3500, 3400, 3300, 3100, 2900, 2700]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
plt.fill_between(df['Month'], df['Revenue'], color='#FF5733', alpha=0.6)
plt.plot(df['Month'], df['Revenue'], color='#C70039')

plt.title('Monthly Revenue for 2024', fontsize=18, pad=25)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Revenue ($)', fontsize=15)

for i, revenue in enumerate(df['Revenue']):
    plt.text(i, revenue + 100, f'${revenue}', ha='center')

plt.grid(True)
plt.show()