
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
                23, 24, 25, 26, 27, 28, 29, 30, 31],
        'Flare_Count': [5, 6, 7, 9, 12, 15, 18, 21, 24, 26, 28, 30, 
                        32, 34, 36, 38, 37, 35, 32, 30, 28, 26, 23, 
                        20, 18, 16, 14, 12, 10, 8, 6]}

# Create DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(16, 8))

# Create lineplot
sns.lineplot(x='Day', y='Flare_Count', data=df, 
             color='#FF5733', marker='o', markersize=8, linewidth=2.5)

# Annotations
plt.annotate('Peak Activity', xy=(16, 38), xytext=(18, 36),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

plt.annotate('Start of Month', xy=(1, 5), xytext=(5, 10),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

# Adding title and labels
plt.title('Daily Solar Flare Activity in March', fontsize=16)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Number of Solar Flares', fontsize=14)

# Display the plot
plt.show()