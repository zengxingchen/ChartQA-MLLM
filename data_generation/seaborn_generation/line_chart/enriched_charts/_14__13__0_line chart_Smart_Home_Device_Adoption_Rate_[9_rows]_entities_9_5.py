
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Gym Membership Sign-Ups': [120, 150, 200, 250, 300, 350, 320, 
                                340, 360, 390, 420, 400]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to categorical type with order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Line chart
plt.figure(figsize=(14, 7))
sns.lineplot(x='Month', y='Gym Membership Sign-Ups', data=df, color="#FF5733", marker='o')

# Add annotation for the highest data point
max_value = df['Gym Membership Sign-Ups'].max()
max_month = df[df['Gym Membership Sign-Ups'] == max_value]['Month'].values[0]
plt.text(x=max_month, y=max_value,
         s='Highest Sign-Ups\nMonth: {}\nSign-Ups: {}'.format(max_month, max_value),
         fontdict=dict(color='#FF5733', size=12),
         bbox=dict(facecolor='none', edgecolor='#FF5733', boxstyle='round,pad=0.5'))

# Set chart title and labels
plt.title('Monthly Gym Membership Sign-Ups in 2023', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Gym Membership Sign-Ups', fontsize=14)

# Show the plot
plt.show()