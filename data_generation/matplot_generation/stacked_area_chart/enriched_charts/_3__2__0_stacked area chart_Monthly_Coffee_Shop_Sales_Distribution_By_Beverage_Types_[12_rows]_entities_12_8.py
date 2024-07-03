
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Beach Vacations': [120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230],
    'Hiking Trips': [200, 220, 210, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'Cultural Tours': [180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))

plt.stackplot(df['Month'],
              df['Beach Vacations'], df['Hiking Trips'], df['Cultural Tours'],
              labels=['Beach Vacations', 'Hiking Trips', 'Cultural Tours'],
              colors=['#3366CC', '#DC3912', '#FF9900'])

plt.title('Monthly Participation in Travel Activities', pad=30, fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Participants (in thousands)', fontsize=14)
plt.legend(loc='upper right')

for i, (mon, a, b, c) in enumerate(zip(df['Month'], df['Beach Vacations'], df['Hiking Trips'], df['Cultural Tours'])):
    if mon == 'December':
        plt.text(i, a+b+c, f'{a+b+c}', ha='center', va='bottom', fontsize=12)

plt.show()