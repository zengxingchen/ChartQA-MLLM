
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Book_Sales': [50, 60, 45, 70, 80, 95, 85, 90, 65, 75, 55, 60]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(12, 8))

# Create the line chart
line_chart = sns.lineplot(x='Month', y='Book_Sales', data=df, 
                          marker='o', color='#FF5733')

# Modify the color scheme using color codes
for line in line_chart.lines:
    line.set_color('#FF4500')

# Annotating the highest book sales point
highest_sales = df['Book_Sales'].max()
highest_month = df[df['Book_Sales'] == highest_sales]['Month'].values[0]
plt.annotate(f'Highest\n{highest_month}', xy=(highest_month, highest_sales), 
             xytext=(highest_month, highest_sales+10),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05),
             ha='center')

# Adjust the plot to make it more readable
plt.xticks(rotation=45)
plt.title('Monthly Book Sales in 2023 (Units)', pad=20)
plt.xlabel('Month')
plt.ylabel('Book Sales (Units)')

# Show the line chart
plt.tight_layout()
plt.show()