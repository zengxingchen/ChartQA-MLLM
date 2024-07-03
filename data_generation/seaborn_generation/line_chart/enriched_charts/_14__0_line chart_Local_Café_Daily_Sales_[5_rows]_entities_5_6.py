
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
                23, 24, 25, 26, 27, 28, 29, 30, 31],
        'Calories': [2300, 2250, 2200, 2150, 2100, 2050, 2000, 1950, 1900, 1850, 1800, 1750, 
                     1700, 1650, 1600, 1550, 1500, 1450, 1400, 1350, 1300, 1250, 1200, 
                     1150, 1100, 1050, 1000, 950, 900, 850, 800]}

# Create DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 7))

# Create lineplot
sns.lineplot(x='Day', y='Calories', data=df, 
             color='#3498DB', marker='o', markersize=8, linewidth=2.5)

# Annotations
plt.annotate('Lowest Calorie Intake', xy=(31, 800), xytext=(25, 900),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

plt.annotate('Start of Tracking', xy=(1, 2300), xytext=(5, 2200),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

# Adding title and labels
plt.title('Daily Calorie Intake Trend for April', fontsize=18, y=1.05)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Calories', fontsize=14)

# Display the plot
plt.show()