
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Subscribers': [300, 350, 400, 370, 420, 380, 390, 450, 470, 430, 480, 500]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to categorical type with order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Line chart
plt.figure(figsize=(12, 8))
sns.lineplot(x='Month', y='Subscribers', data=df, color="#3498db", marker='o')

# Add annotation for the last data point
plt.text(x=df.Month.iloc[-1], y=df.Subscribers.iloc[-1],
         s='End of Year\nSubscribers: {}'.format(df.Subscribers.iloc[-1]),
         fontdict=dict(color='#3498db', size=12),
         bbox=dict(facecolor='none', edgecolor='#3498db', boxstyle='round,pad=0.5'))

# Set chart title and labels
plt.title('Monthly Fitness Subscribers Growth in 2023', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Subscribers', fontsize=14)

# Add annotations for specific points
for i in range(len(df)):
    plt.text(x=df.Month.iloc[i], y=df.Subscribers.iloc[i] + 5,
             s=str(df.Subscribers.iloc[i]), 
             fontdict=dict(color='#2c3e50', size=10))

# Show the plot
plt.show()