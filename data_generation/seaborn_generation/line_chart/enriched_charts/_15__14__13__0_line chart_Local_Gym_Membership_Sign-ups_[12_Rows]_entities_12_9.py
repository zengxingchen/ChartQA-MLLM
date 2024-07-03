
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Heart_Rate': [75, 77, 76, 78, 80, 79, 81, 83, 82, 81, 80, 78]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the order of the months
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August', 'September',
    'October', 'November', 'December'], ordered=True)

# Plot the data
plt.figure(figsize=(10, 5))
ax = sns.lineplot(x='Month', y='Heart_Rate', data=df, 
                  marker='o', color='#1E90FF')

# Annotations and labels
for x, y in zip(df['Month'], df['Heart_Rate']):
    ax.text(x, y, f'{y} bpm', color='black', ha='center', va='bottom')

# Customize appearance
ax.set_title('Monthly Average Heart Rate', fontsize=16, pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Heart Rate (bpm)', fontsize=14)
sns.set_style('whitegrid')

plt.show()