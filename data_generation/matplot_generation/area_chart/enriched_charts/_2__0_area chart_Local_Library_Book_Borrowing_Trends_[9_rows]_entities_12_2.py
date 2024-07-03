
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Steps': [3000, 3200, 5000, 6000, 8000, 12000, 15000, 14000, 10000, 7000, 5000, 4000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type and order it correctly
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)

# Plotting
plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(data=df, x='Month', y='Steps', color='#FF5733', lw=2)
ax.fill_between(df.Month, df.Steps, color='#FF5733', alpha=0.3)

# Adding annotation
for line in range(0, df.shape[0]):
     ax.text(df.Month[line], df.Steps[line], df.Steps[line], 
             horizontalalignment='center', size='small', color='black', weight='semibold')

# Customize the axes and title
ax.set_title('Monthly Average Steps Taken in 2023', fontsize=16, y=1.05)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Steps', fontsize=12)
ax.set(ylim=(0, None))

# Show final result
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()