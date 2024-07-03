
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
                23, 24, 25, 26, 27, 28, 29, 30, 31],
        'Distance': [2.0, 2.1, 2.3, 2.5, 2.8, 3.0, 3.2, 3.5, 3.8, 4.0, 4.3, 4.5, 
                     4.7, 5.0, 5.2, 5.5, 5.3, 5.0, 4.8, 4.6, 4.3, 4.1, 3.8, 
                     3.6, 3.4, 3.1, 2.9, 2.7, 2.5, 2.3, 2.0]}

# Create DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 7))

# Create lineplot
sns.lineplot(x='Day', y='Distance', data=df, 
             color='#3498DB', marker='o', markersize=8, linewidth=2.5)

# Annotations could be added on specific important points
plt.annotate('Longest Distance', xy=(16, 5.5), xytext=(18, 5.2),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

plt.annotate('Start of Month', xy=(1, 2.0), xytext=(5, 2.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

# Adding title and labels
plt.title('Daily Running Distance in Kilometers for March', fontsize=16)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Distance (km)', fontsize=14)

# Display the plot
plt.show()