
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Step Count': [
        7000, 8000, 12000, 9000, 10000, 11000, 13000, 5000, 6000, 7000, 
        10000, 14000, 15000, 9500, 10500, 9800, 12000, 11200, 9300, 8500, 
        7600, 8000, 8200, 11000, 11500, 10900, 11300, 10800, 10700, 13000, 
        12500
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
sns.histplot(df['Step Count'], bins=20, kde=False, color='#1E90FF', binwidth=1000, orientation='horizontal')
plt.title('Histogram of Daily Step Counts Over a Year', pad=20)
plt.xlabel('Frequency')
plt.ylabel('Step Count')
plt.show()