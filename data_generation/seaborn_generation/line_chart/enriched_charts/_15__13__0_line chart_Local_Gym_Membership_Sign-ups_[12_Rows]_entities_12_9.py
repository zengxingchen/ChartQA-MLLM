
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature_Change': [2.3, 2.1, 1.8, 1.5, 1.2, 1.0, 1.1, 1.4, 1.6, 1.8, 2.0, 2.2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the order of the months
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August', 'September',
    'October', 'November', 'December'], ordered=True)

# Plot the data
plt.figure(figsize=(12, 6))
ax = sns.lineplot(x='Month', y='Temperature_Change', data=df, 
                  marker='o', color='#D55E00')

# Annotations and labels
for x, y in zip(df['Month'], df['Temperature_Change']):
    ax.text(x, y, f'{y}°C', color='black', ha='center', va='bottom')

# Customize appearance
ax.set_title('Monthly Temperature Change', fontsize=16, pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Temperature Change (°C)', fontsize=14)
sns.set_style('whitegrid')

plt.show()