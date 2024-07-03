
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Unemployment_Rate': [6.1, 5.9, 5.7, 5.5, 5.3, 5.0, 5.2, 5.1, 4.9, 5.0, 5.2, 5.1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the order of the months
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August', 'September',
    'October', 'November', 'December'], ordered=True)

# Plot the data
plt.figure(figsize=(14, 8))
ax = sns.lineplot(x='Month', y='Unemployment_Rate', data=df, 
                  marker='o', color='#007ACC')

# Annotations and labels
for x, y in zip(df['Month'], df['Unemployment_Rate']):
    ax.text(x, y, f'{y}%', color='black', ha='center', va='bottom')

# Customize appearance
ax.set_title('Monthly Unemployment Rate Change', fontsize=16, pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Unemployment Rate (%)', fontsize=14)
sns.set_style('whitegrid')

plt.show()