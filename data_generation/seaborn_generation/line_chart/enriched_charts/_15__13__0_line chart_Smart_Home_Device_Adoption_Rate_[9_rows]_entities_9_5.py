
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Meditation Hours': [30, 35, 45, 50, 55, 65, 70, 
                         60, 75, 85, 90, 100]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to categorical type with order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Line chart
plt.figure(figsize=(14, 7))
sns.lineplot(x='Month', y='Meditation Hours', data=df, color="#4b8bbe", marker='o')

# Add annotation for the highest data point
max_value = df['Meditation Hours'].max()
max_month = df[df['Meditation Hours'] == max_value]['Month'].values[0]
plt.text(x = max_month, y = max_value,
         s = 'Highest Hours\nMonth: {}\nHours: {}'.format(max_month, max_value),
         fontdict = dict(color='#4b8bbe', size=12),
         bbox=dict(facecolor='none', edgecolor='#4b8bbe', boxstyle='round,pad=0.5'))

# Set chart title and labels
plt.title('Monthly Meditation Hours in 2023', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Meditation Hours', fontsize=14)

# Show the plot
plt.show()