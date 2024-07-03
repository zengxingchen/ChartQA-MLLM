
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Domestic Trips': [110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330],
    'International Trips': [140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360],
    'Business Trips': [90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18, 10))

plt.stackplot(df['Month'],
              df['Domestic Trips'], df['International Trips'], df['Business Trips'],
              labels=['Domestic Trips', 'International Trips', 'Business Trips'],
              colors=['#FF5733', '#3498DB', '#2ECC71'])

plt.title('Monthly Business Travel Trends', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Trips')

plt.legend(loc='upper right')

for i, (mon, dt, it, bt) in enumerate(zip(df['Month'], df['Domestic Trips'], df['International Trips'], df['Business Trips'])):
    if mon == 'December':
        plt.text(i, dt+it+bt, f'{dt+it+bt}', ha='center', va='bottom')

plt.show()