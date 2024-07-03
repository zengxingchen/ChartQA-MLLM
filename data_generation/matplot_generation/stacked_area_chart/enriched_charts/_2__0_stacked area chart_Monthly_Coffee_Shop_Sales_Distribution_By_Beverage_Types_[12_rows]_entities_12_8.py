
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Classic Novels': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210],
    'Modern Novels': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'Non-fiction': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))

plt.stackplot(df['Month'],
              df['Classic Novels'], df['Modern Novels'], df['Non-fiction'],
              labels=['Classic Novels', 'Modern Novels', 'Non-fiction'],
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

plt.title('Monthly Book Sales Data of Different Genres', pad=20)
plt.xlabel('Month')
plt.ylabel('Sales (in units)')
plt.legend(loc='upper left')

for i, (mon, a, b, c) in enumerate(zip(df['Month'], df['Classic Novels'], df['Modern Novels'], df['Non-fiction'])):
    if mon == 'December':
        plt.text(i, a+b+c, f'{a+b+c}', ha='center', va='bottom')

plt.show()