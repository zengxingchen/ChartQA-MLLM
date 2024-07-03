
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data points generated according to the above table
data = {
    'Day': [day for day in range(1, 31)], 
    'Steps': [4500, 5200, 6100, 5700, 6300, 7100, 8600, 7900, 6500, 8700, 
              9200, 5400, 6800, 7300, 8800, 9600, 10200, 11300, 10700, 9900, 
              9450, 8000, 7600, 8100, 8400, 9000, 8700, 9100, 8500, 8300]
}

# Transform data into a Pandas DataFrame
df = pd.DataFrame(data)

# Create a Seaborn histogram, adjust visual elements and figure size
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='Steps', bins=20, color="#336699", kde=False, edgecolor='black', linewidth=1.3, orientation='horizontal')

plt.title('Histogram of Daily Steps Taken (n=30)', fontsize=16)
plt.xlabel('Frequency', fontsize=14)
plt.ylabel('Number of Steps', fontsize=14)
plt.show()