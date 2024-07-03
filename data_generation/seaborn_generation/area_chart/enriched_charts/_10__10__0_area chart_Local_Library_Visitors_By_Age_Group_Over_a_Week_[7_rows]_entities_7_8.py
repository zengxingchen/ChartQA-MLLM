
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data frame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Miles': [50, 60, 75, 90, 110, 130, 150, 140, 120, 100, 80, 55]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Define the plot size
plt.figure(figsize=(14, 7))

# Create the area chart
ax = sns.lineplot(x='Month', y='Miles', data=df, color='#4682B4')
plt.fill_between(df['Month'], df['Miles'], color='#87CEEB', alpha=0.6)

# Annotate a specific point with text
plt.text(6, 155, 'Peak Miles', horizontalalignment='left', size='medium', color='black')

# Customizing the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Miles Run')
plt.title('Monthly Running Miles Logged by Runner')

# Finalize and show the plot
plt.tight_layout()
plt.show()