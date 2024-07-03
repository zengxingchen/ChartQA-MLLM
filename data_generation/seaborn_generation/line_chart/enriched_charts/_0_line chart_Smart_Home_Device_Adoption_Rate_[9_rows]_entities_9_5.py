
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Subscribers': [1000, 1500, 1400, 1450, 1600, 1550, 1620, 
                   1700, 1800, 1750, 1900, 2000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to categorical type with order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Line chart
plt.figure(figsize=(14, 6))
sns.lineplot(x='Month', y='Subscribers', data=df, color="#FF5733", marker='o')

# Add annotation for the last data point
plt.text(x = df.Month.iloc[-1], y = df.Subscribers.iloc[-1],
         s = 'End of Year\nSubscribers: {}'.format(df.Subscribers.iloc[-1]),
         fontdict = dict(color='#FF5733', size=12),
         bbox=dict(facecolor='none', edgecolor='#FF5733', boxstyle='round,pad=0.5'))

# Set chart title and labels
plt.title('Monthly Subscribers Growth in 2023', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Subscribers', fontsize=14)

# Show the plot
plt.show()