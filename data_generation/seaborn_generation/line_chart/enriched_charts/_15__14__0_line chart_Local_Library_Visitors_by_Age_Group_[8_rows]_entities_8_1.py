
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature_C': [5, 7, 12, 15, 20, 25, 28, 27, 22, 16, 10, 6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Adjusting the aesthetics
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(12, 6))
lineplot = sns.lineplot(x='Month', y='Average_Temperature_C', data=df, marker='o', linewidth=2.5,
                        color='#4682B4')

# Customize the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)
plt.title('Monthly Average Temperatures', fontsize=18, pad=20)

# Annotating the data points
for x, y in zip(df['Month'], df['Average_Temperature_C']):
    plt.text(x, y, y, ha='center', va='bottom', fontsize=10)

# Show the plot
plt.show()