
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Total_Tourists': [800, 900, 950, 1000, 1200, 1500, 1800, 1600, 1400, 1300, 1100, 1000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Adjusting the aesthetics
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(16, 8))
lineplot = sns.lineplot(x='Month', y='Total_Tourists', data=df, marker='o', linewidth=2.5,
                        color='#1f77b4')

# Customize the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Tourists', fontsize=14)
plt.title('Monthly Tourist Visits in 2023', fontsize=18, loc='left')

# Annotating the data points
for x, y in zip(df['Month'], df['Total_Tourists']):
    plt.text(x, y, y, ha='center', va='bottom', fontsize=10)

# Show the plot
plt.show()