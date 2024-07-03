
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Total_Units_Sold': [150, 180, 200, 240, 300, 350, 400, 380, 360, 320, 280, 220]
}

# Create DataFrame
df = pd.DataFrame(data)

# Adjusting the aesthetics
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(14, 7))
lineplot = sns.lineplot(x='Month', y='Total_Units_Sold', data=df, marker='o', linewidth=2.5,
                        color='#ff5733')

# Customize the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Units Sold', fontsize=14)
plt.title('Monthly Sales Performance in 2023', fontsize=18)

# Annotating the data points
for x, y in zip(df['Month'], df['Total_Units_Sold']):
    plt.text(x, y, y, ha='center', va='bottom', fontsize=10)

# Show the plot
plt.show()