
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Exercise_Duration': [45, 50, 60, 70, 75, 80, 
                          85, 90, 85, 80, 75, 70]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(14, 10))

# Create the line chart
line_chart = sns.lineplot(x='Month', y='Exercise_Duration', data=df, 
                          marker='o', color='#1E90FF')

# Modify the color scheme using color codes
for line in line_chart.lines:
    line.set_color('#FF1493')

# Annotating the highest exercise duration point
highest_duration = df['Exercise_Duration'].max()
highest_month = df[df['Exercise_Duration'] == highest_duration]['Month'].values[0]
plt.annotate(f'Highest\n{highest_month}', xy=(highest_month, highest_duration), 
             xytext=(highest_month, highest_duration+5),
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             ha='center')

# Adjust the plot to make it more readable
plt.xticks(rotation=45)
plt.title('Monthly Exercise Duration in 2023', pad=20)
plt.xlabel('Month')
plt.ylabel('Exercise Duration (minutes)')

# Show the line chart
plt.tight_layout()
plt.show()