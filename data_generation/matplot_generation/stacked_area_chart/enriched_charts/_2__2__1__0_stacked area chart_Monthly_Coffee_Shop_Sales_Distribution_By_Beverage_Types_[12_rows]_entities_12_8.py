
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Domestic Trips': [5, 6, 8, 10, 12, 15, 18, 20, 22, 24, 26, 30],
    'International Trips': [3, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20],
    'Adventure Trips': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 10))

plt.stackplot(df['Month'],
              df['Domestic Trips'], df['International Trips'], df['Adventure Trips'],
              labels=['Domestic Trips', 'International Trips', 'Adventure Trips'],
              colors=['#FF6347', '#4682B4', '#32CD32'])

plt.title('Monthly Trips Overview', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Trips')

plt.legend(loc='upper right')

for i, (mon, domestic, international, adventure) in enumerate(zip(df['Month'], df['Domestic Trips'], df['International Trips'], df['Adventure Trips'])):
    if mon == 'December':
        plt.text(i, domestic+international+adventure, f'{domestic+international+adventure}', ha='center', va='bottom')

plt.show()