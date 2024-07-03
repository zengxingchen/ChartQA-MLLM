
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Exercise_Hours': [20, 25, 18, 22, 27, 30, 35, 33, 31, 28, 26, 30]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to categorical type with order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Line chart
plt.figure(figsize=(16, 8))
sns.lineplot(x='Month', y='Exercise_Hours', data=df, color="#1E90FF", marker='o')

# Add annotation for the last data point
plt.text(x = df.Month.iloc[-1], y = df.Exercise_Hours.iloc[-1],
         s = 'End of Year\nExercise Hours: {}'.format(df.Exercise_Hours.iloc[-1]),
         fontdict = dict(color='#1E90FF', size=12),
         bbox=dict(facecolor='none', edgecolor='#1E90FF', boxstyle='round,pad=0.5'))

# Set chart title and labels
plt.title('Monthly Exercise Hours in 2023', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Exercise Hours', fontsize=14)

# Show the plot
plt.show()