
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Physical Books': [150, 170, 180, 190, 210, 220, 230, 250, 260, 270, 280, 300],
    'E-Books': [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420],
    'Audio Books': [100, 110, 130, 140, 160, 170, 180, 200, 210, 220, 240, 250]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))

plt.stackplot(df['Month'],
              df['Physical Books'], df['E-Books'], df['Audio Books'],
              labels=['Physical Books', 'E-Books', 'Audio Books'],
              colors=['#FF6347', '#4682B4', '#32CD32'])

plt.title('Monthly Sales Data of Book Formats', pad=20)
plt.xlabel('Month')
plt.ylabel('Sales (in units)')

plt.legend(loc='upper right')

for i, (mon, pb, eb, ab) in enumerate(zip(df['Month'], df['Physical Books'], df['E-Books'], df['Audio Books'])):
    if mon == 'December':
        plt.text(i, pb+eb+ab, f'{pb+eb+ab}', ha='center', va='bottom')

plt.show()