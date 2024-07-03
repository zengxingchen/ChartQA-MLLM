
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
                23, 24, 25, 26, 27, 28, 29, 30, 31],
        'Sunspots': [45, 48, 50, 52, 55, 53, 51, 50, 48, 47, 49, 50, 
                     52, 53, 55, 57, 59, 60, 58, 56, 55, 54, 53, 
                     51, 49, 47, 45, 43, 42, 40, 38]}

# Create DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(12, 6))

# Create lineplot
sns.lineplot(x='Day', y='Sunspots', data=df, 
             color='#FF6347', marker='D', markersize=8, linewidth=2.5)

# Annotations
plt.annotate('Peak Sunspot Activity', xy=(18, 60), xytext=(15, 62),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

plt.annotate('Start of Observation', xy=(1, 45), xytext=(4, 48),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

# Adding title and labels
plt.title('Daily Average Sunspots Observed in May', fontsize=18, y=1.05)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Number of Sunspots', fontsize=14)

# Display the plot
plt.show()