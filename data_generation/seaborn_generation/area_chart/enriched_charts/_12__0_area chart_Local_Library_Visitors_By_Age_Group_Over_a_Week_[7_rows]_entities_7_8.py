
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data frame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Hours_of_Study': [20, 25, 30, 35, 40, 45, 50, 55, 50, 45, 30, 25]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Define the plot size
plt.figure(figsize=(16, 8))

# Create the area chart
ax = sns.lineplot(x='Month', y='Average_Hours_of_Study', data=df, color='#FF5733')
plt.fill_between(df['Month'], df['Average_Hours_of_Study'], color='#FFBD33', alpha=0.3)

# Annotate a specific point with text
plt.text(7, 55, 'Peak Study Hours', horizontalalignment='left', size='medium', color='black')

# Customizing the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Average Hours of Study')
plt.title('Monthly Average Study Hours')

# Finalize and show the plot
plt.tight_layout()
plt.show()