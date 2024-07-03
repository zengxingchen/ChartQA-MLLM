
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Solar_Energy_Output': [150, 180, 220, 260, 300, 340, 
                            320, 310, 280, 240, 200, 160]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(14, 9))

# Create the line chart
line_chart = sns.lineplot(x='Month', y='Solar_Energy_Output', data=df, 
                          marker='o', color='#1E90FF')

# Modify the color scheme using color codes
for line in line_chart.lines:
    line.set_color('#8A2BE2')

# Annotating the highest solar energy output point
highest_output = df['Solar_Energy_Output'].max()
highest_month = df[df['Solar_Energy_Output'] == highest_output]['Month'].values[0]
plt.annotate(f'Highest\n{highest_month}', xy=(highest_month, highest_output), 
             xytext=(highest_month, highest_output+30),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05),
             ha='center')

# Adjust the plot to make it more readable
plt.xticks(rotation=45)
plt.title('Monthly Average Solar Energy Output in 2023 (kWh)', pad=20)
plt.xlabel('Month')
plt.ylabel('Solar Energy Output (kWh)')

# Show the line chart
plt.tight_layout()
plt.show()