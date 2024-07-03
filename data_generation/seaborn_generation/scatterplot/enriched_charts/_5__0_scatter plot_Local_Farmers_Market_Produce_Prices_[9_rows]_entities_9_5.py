
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Data in a format suitable to be saved as .csv and then read using pandas
data = '''
Date,AverageCalories,NumberOfSteps
2024-01-01,2000,5000
2024-01-02,2100,5400
2024-01-03,1900,4800
2024-01-04,2200,6000
2024-01-05,2050,5500
2024-01-06,2300,6300
2024-01-07,2250,6200
2024-01-08,1950,5000
2024-01-09,2150,5700
2024-01-10,2200,5900
2024-01-11,2350,6500
2024-01-12,2000,5200
2024-01-13,2400,6700
2024-01-14,1850,4700
2024-01-15,2000,5100
2024-01-16,2500,6800
2024-01-17,2100,5400
2024-01-18,1950,5000
2024-01-19,2250,6100
2024-01-20,2050,5600
2024-01-21,2200,5900
2024-01-22,2300,6400
2024-01-23,2000,5200
2024-01-24,2400,6600
2024-01-25,1900,4900
2024-01-26,2100,5500
2024-01-27,2500,7000
2024-01-28,1800,4600
2024-01-29,2150,5800
2024-01-30,2250,6200
2024-01-31,2000,5000
'''

# Use StringIO to simulate a file handle
df = pd.read_csv(StringIO(data), parse_dates=['Date'])

# Setting the size of the plot
plt.figure(figsize=(16, 10))

# Create a scatterplot with a customized color scheme
sns.scatterplot(data=df, x='Date', y='AverageCalories', size='NumberOfSteps',
                sizes=(20, 200), hue='NumberOfSteps', palette=["#FF6347", "#FFD700", "#8A2BE2", "#00FA9A", "#4682B4", "#FF4500", "#DA70D6"])

# Customize the aesthetics
plt.title('Daily Health Tracker: Average Calories vs Number of Steps', fontsize=18, y=1.05)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Average Calories', fontsize=14)

# Show the plot
plt.show()