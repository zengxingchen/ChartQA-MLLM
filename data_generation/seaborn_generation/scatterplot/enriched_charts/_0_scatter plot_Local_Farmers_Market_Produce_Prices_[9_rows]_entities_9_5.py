
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data in a format suitable to be saved as .csv and then read using pandas
data = '''
Date,AverageBill,NumberOfCustomers
2023-01-01,5.20,95
2023-01-02,6.30,102
2023-01-03,4.80,88
2023-01-04,5.50,110
2023-01-05,5.60,107
2023-01-06,6.00,120
2023-01-07,5.85,115
2023-01-08,4.95,90
2023-01-09,5.75,108
2023-01-10,5.90,112
2023-01-11,6.10,130
2023-01-12,5.30,105
2023-01-13,6.50,123
2023-01-14,4.70,80
2023-01-15,5.20,99
2023-01-16,6.80,128
2023-01-17,5.40,104
2023-01-18,5.10,93
2023-01-19,5.95,118
2023-01-20,5.30,100
'''

# Use StringIO to simulate a file handle
from io import StringIO
df = pd.read_csv(StringIO(data), parse_dates=['Date'])

# Setting the size of the plot
plt.figure(figsize=(14, 8))

# Create a scatterplot with a customized color scheme
sns.scatterplot(data=df, x='Date', y='AverageBill', size='NumberOfCustomers',
                sizes=(20, 200), hue='NumberOfCustomers', palette="ch:r=-.5,l=.75")

# Customize the aesthetics
plt.title('Daily Coffee Shop Performance: Average Bill vs Number of Customers', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Average Bill ($)', fontsize=14)

# Show the plot
plt.show()