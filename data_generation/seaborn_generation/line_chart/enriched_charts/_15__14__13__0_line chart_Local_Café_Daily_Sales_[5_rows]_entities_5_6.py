
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
                23, 24, 25, 26, 27, 28, 29, 30],
        'Books Sold': [120, 125, 110, 140, 145, 150, 160, 155, 170, 175, 165, 180, 
                       190, 185, 200, 205, 210, 220, 230, 235, 240, 245, 250, 
                       255, 260, 265, 270, 275, 280, 290]}

# Create DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 8))

# Create lineplot
sns.lineplot(x='Day', y='Books Sold', data=df, 
             color='#3366CC', marker='o', markersize=8, linewidth=2.5)

# Annotations
plt.annotate('Highest Books Sold', xy=(30, 290), xytext=(25, 280),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

plt.annotate('Start of Month', xy=(1, 120), xytext=(5, 130),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

# Adding title and labels
plt.title('Daily Books Sold in June', fontsize=18, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Books Sold', fontsize=14)

# Display the plot
plt.show()