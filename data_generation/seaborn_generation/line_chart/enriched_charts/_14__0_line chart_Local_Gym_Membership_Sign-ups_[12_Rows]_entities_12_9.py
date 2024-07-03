
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Rainfall': [78, 85, 62, 55, 45, 40, 35, 48, 60, 72, 80, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the order of the months
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August', 'September',
    'October', 'November', 'December'], ordered=True)

# Plot the data
plt.figure(figsize=(14, 7))
ax = sns.lineplot(x='Month', y='Average_Rainfall', data=df, 
                  marker='o', color='#3498DB')

# Annotations and labels
for x, y in zip(df['Month'], df['Average_Rainfall']):
    ax.text(x, y, f'{y} mm', color='blue', ha='right', va='bottom')

# Customize appearance
ax.set_title('Monthly Average Rainfall', fontsize=16, pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Rainfall (mm)')
sns.set_style('whitegrid')

plt.show()