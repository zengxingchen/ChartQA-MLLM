
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Stock Prices': [150, 160, 155, 165, 170, 175, 
                     160, 180, 185, 175, 190, 195]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(14, 8))

# Create the line chart
line_chart = sns.lineplot(x='Month', y='Stock Prices', data=df, 
                          marker='o', color='#1F77B4')

# Modify the color scheme using color codes
for line in line_chart.lines:
    line.set_color('#FF7F0E')

# Annotating the highest stock price
highest_price = df['Stock Prices'].max()
highest_month = df[df['Stock Prices'] == highest_price]['Month'].values[0]
plt.annotate(f'Highest\n{highest_month}', xy=(highest_month, highest_price), 
             xytext=(highest_month, highest_price+10),
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             ha='center')

# Adjust the plot to make it more readable
plt.xticks(rotation=45)
plt.title('Monthly Stock Prices in 2020', pad=20)
plt.xlabel('Month')
plt.ylabel('Stock Prices')

# Show the line chart
plt.tight_layout()
plt.show()