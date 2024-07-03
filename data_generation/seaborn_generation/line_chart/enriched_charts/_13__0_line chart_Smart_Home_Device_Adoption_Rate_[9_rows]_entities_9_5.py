
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Books Sold': [300, 450, 500, 600, 700, 850, 900, 
                   750, 800, 950, 1100, 1200]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to categorical type with order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Line chart
plt.figure(figsize=(16, 8))
sns.lineplot(x='Month', y='Books Sold', data=df, color="#1f77b4", marker='o')

# Add annotation for the highest data point
max_value = df['Books Sold'].max()
max_month = df[df['Books Sold'] == max_value]['Month'].values[0]
plt.text(x = max_month, y = max_value,
         s = 'Highest Sales\nMonth: {}\nBooks Sold: {}'.format(max_month, max_value),
         fontdict = dict(color='#1f77b4', size=12),
         bbox=dict(facecolor='none', edgecolor='#1f77b4', boxstyle='round,pad=0.5'))

# Set chart title and labels
plt.title('Monthly Book Sales in 2023', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Books Sold', fontsize=14)

# Show the plot
plt.show()