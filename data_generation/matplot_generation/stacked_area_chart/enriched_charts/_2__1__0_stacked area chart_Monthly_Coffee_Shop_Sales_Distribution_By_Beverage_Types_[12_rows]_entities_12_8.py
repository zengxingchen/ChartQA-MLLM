
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Domestic Trips': [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320],
    'International Trips': [150, 160, 170, 180, 200, 220, 240, 260, 280, 300, 320, 340],
    'Business Trips': [80, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))

plt.stackplot(df['Month'],
              df['Domestic Trips'], df['International Trips'], df['Business Trips'],
              labels=['Domestic Trips', 'International Trips', 'Business Trips'],
              colors=['#FF4500', '#1E90FF', '#32CD32'])

plt.title('Monthly Travel Data of Different Trip Types', pad=30)
plt.xlabel('Month')
plt.ylabel('Number of Trips')

plt.legend(loc='upper left')

for i, (mon, dt, it, bt) in enumerate(zip(df['Month'], df['Domestic Trips'], df['International Trips'], df['Business Trips'])):
    if mon == 'December':
        plt.text(i, dt+it+bt, f'{dt+it+bt}', ha='center', va='bottom')

plt.show()