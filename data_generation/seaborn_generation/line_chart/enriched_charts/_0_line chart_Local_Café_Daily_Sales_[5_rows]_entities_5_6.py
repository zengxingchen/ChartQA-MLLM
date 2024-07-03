
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
                23, 24, 25, 26, 27, 28, 29, 30, 31],
        'Temperature': [12, 12.5, 13, 13.5, 14, 14.2, 14.5, 14.8, 15, 15.5, 16, 16.3, 
                        16.5, 17, 17.5, 17.6, 17.8, 18, 18.5, 19, 19.5, 19.7, 19.9, 
                        20, 19.8, 19.6, 19.3, 19, 18.8, 18.5, 18.2]}

# Create DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(12, 6))

# Create lineplot
sns.lineplot(x='Day', y='Temperature', data=df, 
             color='#E74C3C', marker='o', markersize=8, linewidth=2.5)

# Annotations could be added on specific important points, like highest and lowest temperature
plt.annotate('Highest Temp', xy=(24, 20), xytext=(25, 19),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

plt.annotate('Start of Month', xy=(1, 12), xytext=(5, 13),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right', verticalalignment='top')

# Adding title and labels
plt.title('Daily Average Temperature Trend for March', fontsize=16)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)

# Display the plot
plt.show()