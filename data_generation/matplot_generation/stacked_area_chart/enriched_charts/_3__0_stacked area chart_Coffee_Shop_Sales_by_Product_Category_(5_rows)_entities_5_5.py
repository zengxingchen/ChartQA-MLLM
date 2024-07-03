
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Calories Burned': [1200, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800],
    'Active Minutes': [700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920],
    'Distance Covered': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],
}

df = pd.DataFrame(data)

x = df['Month']

plt.figure(figsize=(14, 8))
plt.stackplot(x, df['Calories Burned'], df['Active Minutes'], df['Distance Covered'], 
              colors=['#3498db', '#2ecc71', '#e74c3c'])

plt.title('Monthly Fitness Activity Over A Year', y=1.05)
plt.xlabel('Month')
plt.ylabel('Activity Metrics')

plt.legend(['Calories Burned', 'Active Minutes', 'Distance Covered'], loc='upper left')

plt.annotate('Start of Year', xy=(0, df['Calories Burned'][0] + df['Active Minutes'][0]), 
             xytext=(0, 3000), arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.annotate('End of Year', xy=(11, df['Calories Burned'][11] + df['Active Minutes'][11] + df['Distance Covered'][11]), 
             xytext=(11, 3500), arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.show()