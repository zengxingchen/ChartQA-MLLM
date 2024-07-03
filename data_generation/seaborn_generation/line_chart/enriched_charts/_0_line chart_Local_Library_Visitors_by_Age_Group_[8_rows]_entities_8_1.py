
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature_Celsius': [5, 6, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Adjusting the aesthetics
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(16, 8))
lineplot = sns.lineplot(x='Month', y='Average_Temperature_Celsius', data=df, marker='o', linewidth=2.5,
                        color='#1f77b4')

# Customize the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)
plt.title('Average Monthly Temperature', fontsize=18)

# Annotating the data points
for x, y in zip(df['Month'], df['Average_Temperature_Celsius']):
    plt.text(x, y, y, ha='center', va='bottom', fontsize=10)

# Show the plot
plt.show()