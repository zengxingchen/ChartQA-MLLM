
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Running': [120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340],
    'Swimming': [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420],
    'Cycling': [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))

plt.stackplot(df['Month'],
              df['Running'], df['Swimming'], df['Cycling'],
              labels=['Running', 'Swimming', 'Cycling'],
              colors=['#FFA07A', '#20B2AA', '#778899'])

plt.title('Monthly Exercise Activity Data', pad=40)
plt.xlabel('Month')
plt.ylabel('Activity (in hours)')

plt.legend(loc='upper left')

for i, (mon, run, swim, cycle) in enumerate(zip(df['Month'], df['Running'], df['Swimming'], df['Cycling'])):
    if mon == 'December':
        plt.text(i, run + swim + cycle, f'{run + swim + cycle}', ha='center', va='bottom')

plt.show()