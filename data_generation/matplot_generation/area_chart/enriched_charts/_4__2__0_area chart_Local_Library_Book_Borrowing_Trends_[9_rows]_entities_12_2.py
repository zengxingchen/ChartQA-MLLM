
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Average Daily Rainfall (mm)': [5.0, 6.2, 10.0, 12.5, 14.8, 20.3, 25.7, 22.5, 18.9, 15.6, 8.4, 6.8]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type and order it correctly
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)

# Plotting
plt.figure(figsize=(16, 9))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(data=df, x='Month', y='Average Daily Rainfall (mm)', color='#3498DB', lw=2)
ax.fill_between(df.Month, df['Average Daily Rainfall (mm)'], color='#3498DB', alpha=0.4)

# Adding annotation
for line in range(0, df.shape[0]):
    ax.text(df.Month[line], df['Average Daily Rainfall (mm)'][line], 
            df['Average Daily Rainfall (mm)'][line], 
            horizontalalignment='center', size='small', color='black', weight='semibold')

# Customize the axes and title
ax.set_title('Average Daily Rainfall (mm) in 2023', fontsize=18, y=1.05)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Average Daily Rainfall (mm)', fontsize=14)
ax.set(ylim=(0, None))

# Show final result
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()