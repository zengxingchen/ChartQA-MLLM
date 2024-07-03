
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Visitors': [1500, 1700, 1600, 1800, 2000, 2200, 2100, 2300, 2400, 2200, 2100, 2500]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
plt.fill_between(df['Month'], df['Visitors'], color='#4CAF50', alpha=0.7)
plt.plot(df['Month'], df['Visitors'], color='#388E3C')

plt.title('Monthly Visitors for 2024', fontsize=20, pad=30)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Number of Visitors', fontsize=15)

for i, visitors in enumerate(df['Visitors']):
    plt.text(i, visitors + 100, f'{visitors}', ha='center')

plt.grid(True)
plt.show()