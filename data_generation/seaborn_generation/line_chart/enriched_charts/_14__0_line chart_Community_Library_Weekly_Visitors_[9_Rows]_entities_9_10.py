
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Signups': [200, 220, 250, 270, 300, 280, 
                310, 330, 290, 320, 340, 360]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(12, 7))

# Create the line chart
line_chart = sns.lineplot(x='Month', y='Signups', data=df, 
                          marker='o', color='#3498db')

# Modify the color scheme using color codes
for line in line_chart.lines:
    line.set_color('#E74C3C')

# Annotating the highest signup point
highest_signups = df['Signups'].max()
highest_month = df[df['Signups'] == highest_signups]['Month'].values[0]
plt.annotate(f'Highest\n{highest_month}', xy=(highest_month, highest_signups), 
             xytext=(highest_month, highest_signups+20),
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             ha='center')

# Adjust the plot to make it more readable
plt.xticks(rotation=45)
plt.title('Monthly Gym Membership Signups in 2020', pad=20)
plt.xlabel('Month')
plt.ylabel('Signups')

# Show the line chart
plt.tight_layout()
plt.show()