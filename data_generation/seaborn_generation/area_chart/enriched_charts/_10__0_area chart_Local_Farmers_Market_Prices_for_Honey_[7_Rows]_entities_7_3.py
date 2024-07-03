
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'SleepHours': [7.5, 7.3, 7.0, 7.2, 7.8, 7.6, 8.0, 7.9, 7.7, 7.4, 7.2, 7.6]
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(12, 8))

# Create an area chart
sns.lineplot(data=df, x='Month', y='SleepHours', sort=False, lw=1)
plt.fill_between(df.Month, df.SleepHours, color="#FFB6C1")

# Assign annotation
plt.text(df.Month[df.SleepHours.idxmax()], df.SleepHours.max(), 'Highest\nSleep Hours', horizontalalignment='center', verticalalignment='bottom', fontsize=10, color='black')

# Customize the plot with title, labels, and limit
plt.title('Average Monthly Sleep Hours in City XYZ', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sleep Hours', fontsize=12)

# Customize x-axis
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()