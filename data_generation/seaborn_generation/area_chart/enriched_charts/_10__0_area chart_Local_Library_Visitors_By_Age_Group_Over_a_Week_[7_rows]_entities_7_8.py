
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data frame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Running_Distance': [50, 55, 60, 70, 80, 85, 90, 95, 85, 70, 60, 50]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Define the plot size
plt.figure(figsize=(16, 8))

# Create the area chart
ax = sns.lineplot(x='Month', y='Average_Running_Distance', data=df, color='#2ca02c')
plt.fill_between(df['Month'], df['Average_Running_Distance'], color='#2ca02c', alpha=0.3)

# Annotate a specific point with text
plt.text(7, 95, 'Peak Running Distance', horizontalalignment='left', size='medium', color='black')

# Customizing the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Average Running Distance (km)')
plt.title('Monthly Average Running Distance')

# Finalize and show the plot
plt.tight_layout()
plt.show()