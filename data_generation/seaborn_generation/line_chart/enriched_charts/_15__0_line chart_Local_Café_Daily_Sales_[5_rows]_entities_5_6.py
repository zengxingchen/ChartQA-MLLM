
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
                23, 24, 25, 26, 27, 28, 29, 30, 31],
        'Visitors': [50, 55, 60, 65, 62, 70, 75, 80, 85, 90, 95, 100, 
                     105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 
                     155, 160, 165, 170, 175, 180, 185, 190, 195]}

# Create DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 7))

# Create lineplot
sns.lineplot(x='Day', y='Visitors', data=df, 
             color='#2E86C1', marker='o', markersize=8, linewidth=2.5)

# Annotations
plt.annotate('Peak Visitors', xy=(31, 195), xytext=(28, 190),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

plt.annotate('Start of Month', xy=(1, 50), xytext=(5, 55),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

# Adding title and labels
plt.title('Daily Visitor Count in an Art Exhibition', fontsize=16)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Number of Visitors', fontsize=14)

# Display the plot
plt.show()