
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'distance': [2, 4, 5, 5, 7, 8, 10, 11, 12, 12, 14, 15, 16, 17, 19, 21, 22, 23, 
                 24, 26, 27, 28, 30, 32, 34, 36, 37, 38, 40, 42, 44, 45, 48]
}
df = pd.DataFrame(data)

# Seaborn Histogram
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(df['distance'], color="#3498db", binwidth=3, orientation='vertical')

plt.title('Distribution of Weekly Running Distance', fontsize=14, pad=15)
plt.xlabel('Distance (km)')
plt.ylabel('Frequency')

# Show plot
plt.show()