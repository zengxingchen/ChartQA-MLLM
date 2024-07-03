
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

data = '''
Date,Steps,CaloriesBurned
2023-01-01,8000,250
2023-01-02,7500,230
2023-01-03,10000,300
2023-01-04,12000,350
2023-01-05,8500,260
2023-01-06,9000,280
2023-01-07,9500,290
2023-01-08,11000,320
2023-01-09,9800,305
2023-01-10,8700,270
2023-01-11,11500,340
2023-01-12,8000,250
2023-01-13,10500,310
2023-01-14,7000,220
2023-01-15,8500,260
2023-01-16,13000,380
2023-01-17,8200,245
2023-01-18,7600,235
2023-01-19,9200,275
2023-01-20,8900,265
'''

df = pd.read_csv(StringIO(data), parse_dates=['Date'])

plt.figure(figsize=(16, 10))

sns.scatterplot(data=df, x='Date', y='Steps', size='CaloriesBurned',
                sizes=(20, 200), hue='CaloriesBurned', palette=['#FF5733', '#33FF57', '#3357FF', '#F5B041', '#AF7AC5'])

plt.title('Daily Fitness Performance: Steps vs Calories Burned', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Steps', fontsize=16)

plt.show()