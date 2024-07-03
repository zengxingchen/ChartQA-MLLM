
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data frame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature': [5, 6, 9, 12, 16, 20, 23, 23, 19, 14, 9, 6]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Define the plot size
plt.figure(figsize=(14, 6))

# Create the area chart
ax = sns.lineplot(x='Month', y='Average_Temperature', data=df)
plt.fill_between(df['Month'], df['Average_Temperature'], color='#1f77b4', alpha=0.3)

# Annotate a specific point with text
plt.text(5, 22, 'Peak Summer Temp', horizontalalignment='left', size='medium', color='black')

# Customizing the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.title('Monthly Average Temperature')

# Finalize and show the plot
plt.tight_layout()
plt.show()