
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load data into a pandas DataFrame
data_values = [
    1500, 1700, 1600, 1750, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500,
    2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700,
    3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900,
    5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100,
    6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300,
    7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500,
    8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700,
    9800, 9900, 10000
]

# Create the dataframe
df = pd.DataFrame(data_values, columns=['Value'])

# Set up the matplotlib figure
sns.set(style="whitegrid")
plt.figure(figsize=(8, 10))

# Plot a vertical histogram with specified bin width and color
sns.histplot(df['Value'], color='#2ecc71', binwidth=500, kde=False, orientation='vertical')

# Customize the plot with title, labels, and limits
plt.title('Distribution of Monthly Expenditures', fontsize=16)
plt.xlabel('Monthly Expenditure (in $)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Show the plot
plt.show()