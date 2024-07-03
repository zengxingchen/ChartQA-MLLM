
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40, 42],
    'Marketing': [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],
    'Development': [20, 25, 30, 28, 32, 35, 38, 40, 42, 45, 48, 50],
    'Support': [5, 8, 12, 10, 15, 18, 20, 22, 25, 28, 30, 32],
    'HR': [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
    'Finance': [12, 15, 18, 20, 22, 25, 27, 30, 32, 35, 38, 40]
}
df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

plt.figure(figsize=(18, 12))
plt.stackplot(df.index, df['Sales'], df['Marketing'], df['Development'], df['Support'], df['HR'], df['Finance'], 
              colors=['#FF5733', '#33FFBD', '#335BFF', '#FF33A8', '#33FF57', '#FFBD33'])

plt.xlabel('Month')
plt.ylabel('Hours')
plt.title('Company Department Monthly Hours Allocation', fontsize=18, pad=25)

for i, month in enumerate(df.index):
    plt.text(i, df.loc[month].sum() - 0.5, f"{df.loc[month].sum()}h", ha='center', fontsize=12)

plt.legend(['Sales', 'Marketing', 'Development', 'Support', 'HR', 'Finance'], loc='upper left')
plt.tight_layout()

plt.show()