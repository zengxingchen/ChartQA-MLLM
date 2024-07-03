
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
                23, 24, 25, 26, 27, 28, 29, 30],
        'Calories': [1800, 1850, 1900, 1920, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 
                     2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 
                     2900, 2950, 3000, 3050, 3100, 3150, 3200]}

# Create DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(12, 6))

# Create lineplot
sns.lineplot(x='Day', y='Calories', data=df, 
             color='#FF5733', marker='s', markersize=8, linewidth=2.5)

# Annotations
plt.annotate('Highest Calorie Intake', xy=(30, 3200), xytext=(25, 3100),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

plt.annotate('Start of Month', xy=(1, 1800), xytext=(5, 1900),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

# Adding title and labels
plt.title('Daily Calorie Intake in June', fontsize=16, pad=20)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Calories', fontsize=14)

# Display the plot
plt.show()