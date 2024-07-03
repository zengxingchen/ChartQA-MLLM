
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Stock_Price_USD': [150, 155, 160, 158, 162, 168, 170, 175, 172, 169, 165, 160]
}

# Create DataFrame
df = pd.DataFrame(data)

# Adjusting the aesthetics
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(14, 7))
lineplot = sns.lineplot(x='Month', y='Stock_Price_USD', data=df, marker='o', linewidth=2.5,
                        color='#ff6347')

# Customize the axes and title
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Stock Price (USD)', fontsize=14)
plt.title('Average Monthly Stock Prices', fontsize=18, pad=20)

# Annotating the data points
for x, y in zip(df['Month'], df['Stock_Price_USD']):
    plt.text(x, y, y, ha='center', va='bottom', fontsize=10)

# Show the plot
plt.show()