
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data frame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Return': [2.5, 3.1, 4.0, 5.2, 6.1, 7.3, 8.0, 7.5, 6.7, 5.5, 4.2, 3.0]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Define the plot size
plt.figure(figsize=(16, 8))

# Create the area chart
ax = sns.lineplot(x='Month', y='Return', data=df, color='#FF6347')
plt.fill_between(df['Month'], df['Return'], color='#FFD700', alpha=0.6)

# Annotate a specific point with text
plt.text(6, 8.5, 'Highest Return', horizontalalignment='left', size='medium', color='black')

# Customizing the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Investment Return (%)')
plt.title('Monthly Investment Returns in 2023')

# Finalize and show the plot
plt.tight_layout()
plt.show()