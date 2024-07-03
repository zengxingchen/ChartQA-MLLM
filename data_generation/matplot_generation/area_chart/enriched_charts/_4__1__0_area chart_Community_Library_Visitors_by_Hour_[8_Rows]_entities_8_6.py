
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Happiness_Index': [70, 73, 75, 78, 80, 85, 90, 88, 82, 77, 72, 68]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 9))
plt.fill_between(df['Month'], df['Happiness_Index'], color='#ff7f0e', alpha=0.6)
plt.plot(df['Month'], df['Happiness_Index'], color='#ff7f0e')

plt.title('Monthly Happiness Index', fontsize=18, pad=25)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Happiness Index', fontsize=15)

for i, value in enumerate(df['Happiness_Index']):
    plt.text(i, value + 0.5, f'{value}', ha='center')

plt.grid(True)
plt.show()