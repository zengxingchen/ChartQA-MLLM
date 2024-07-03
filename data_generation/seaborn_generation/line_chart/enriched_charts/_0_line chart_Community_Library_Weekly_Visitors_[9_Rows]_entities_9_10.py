
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [10000, 12000, 14000, 16000, 18000, 20000, 
                19000, 17000, 15000, 13000, 11000, 9000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(10, 6))

# Create the line chart
line_chart = sns.lineplot(x='Month', y='Revenue', data=df, 
                          marker='o', color='#1f77b4')

# Modify the color scheme using color codes
for line in line_chart.lines:
    line.set_color('#FF5733')

# Annotating the highest revenue point
highest_revenue = df['Revenue'].max()
highest_month = df[df['Revenue'] == highest_revenue]['Month'].values[0]
plt.annotate(f'Highest\n{highest_month}', xy=(highest_month, highest_revenue), 
             xytext=(highest_month, highest_revenue+1000),
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             ha='center')

# Adjust the plot to make it more readable
plt.xticks(rotation=45)
plt.title('Monthly Revenue in 2020')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')

# Show the line chart
plt.tight_layout()
plt.show()