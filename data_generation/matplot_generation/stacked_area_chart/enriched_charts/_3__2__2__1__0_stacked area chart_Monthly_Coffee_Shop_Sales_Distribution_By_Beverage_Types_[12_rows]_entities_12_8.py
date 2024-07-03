
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Apples': [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
    'Oranges': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
    'Bananas': [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
}

df = pd.DataFrame(data)

plt.figure(figsize=(20, 12))

plt.stackplot(df['Month'],
              df['Apples'], df['Oranges'], df['Bananas'],
              labels=['Apples', 'Oranges', 'Bananas'],
              colors=['#FF4500', '#FFD700', '#8B4513'])

plt.title('Monthly Fruit Consumption', pad=40)
plt.xlabel('Month')
plt.ylabel('Number of Fruits')

plt.legend(loc='upper left')

for i, (mon, apples, oranges, bananas) in enumerate(zip(df['Month'], df['Apples'], df['Oranges'], df['Bananas'])):
    if mon == 'December':
        plt.text(i, apples + oranges + bananas, f'{apples + oranges + bananas}', ha='center', va='bottom')

plt.show()