
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Data in a format suitable to be saved as .csv and then read using pandas
data = '''
Date,BooksSold,RevenueGenerated
2024-01-01,50,1000
2024-01-02,45,950
2024-01-03,60,1200
2024-01-04,55,1100
2024-01-05,65,1300
2024-01-06,70,1400
2024-01-07,75,1500
2024-01-08,40,800
2024-01-09,85,1700
2024-01-10,90,1800
2024-01-11,95,1900
2024-01-12,50,1000
2024-01-13,100,2000
2024-01-14,45,900
2024-01-15,55,1100
2024-01-16,105,2100
2024-01-17,60,1200
2024-01-18,50,1000
2024-01-19,80,1600
2024-01-20,65,1300
2024-01-21,70,1400
2024-01-22,90,1800
2024-01-23,55,1100
2024-01-24,100,2000
2024-01-25,50,1000
2024-01-26,75,1500
2024-01-27,105,2100
2024-01-28,35,700
2024-01-29,85,1700
2024-01-30,95,1900
2024-01-31,50,1000
'''

# Use StringIO to simulate a file handle
df = pd.read_csv(StringIO(data), parse_dates=['Date'])

# Setting the size of the plot
plt.figure(figsize=(18, 12))

# Create a scatterplot with a customized color scheme
sns.scatterplot(data=df, x='Date', y='RevenueGenerated', size='BooksSold',
                sizes=(20, 200), hue='BooksSold', palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF", "#33FFF7", "#F7FF33"])

# Customize the aesthetics
plt.title('Books Sales and Revenue Over Time', fontsize=18, y=1.05)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Revenue Generated ($)', fontsize=14)

# Show the plot
plt.show()