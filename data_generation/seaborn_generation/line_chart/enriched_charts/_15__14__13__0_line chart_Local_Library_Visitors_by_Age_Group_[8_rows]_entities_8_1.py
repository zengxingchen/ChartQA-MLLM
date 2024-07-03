
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Profit': [200, 180, 210, 220, 240, 260, 280, 270, 250, 230, 220, 210]
}

# Create DataFrame
df = pd.DataFrame(data)

# Adjusting the aesthetics
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(14, 7))
lineplot = sns.lineplot(x='Month', y='Profit', data=df, marker='o', linewidth=2.5,
                        color='#FF5733')

# Customize the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Profit (in $1000s)', fontsize=14)
plt.title('Monthly Profit in a Small Business (2023)', fontsize=20, pad=20)

# Annotating the data points
for x, y in zip(df['Month'], df['Profit']):
    plt.text(x, y, y, ha='center', va='bottom', fontsize=10)

# Show the plot
plt.show()