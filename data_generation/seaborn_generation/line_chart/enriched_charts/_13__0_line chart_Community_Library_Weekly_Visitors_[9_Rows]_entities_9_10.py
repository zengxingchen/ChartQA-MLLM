
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Calorie_Intake': [2500, 2400, 2600, 2700, 2800, 2900, 
                       3000, 3100, 2900, 2800, 2700, 2600]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(12, 8))

# Create the line chart
line_chart = sns.lineplot(x='Month', y='Calorie_Intake', data=df, 
                          marker='o', color='#2E8B57')

# Modify the color scheme using color codes
for line in line_chart.lines:
    line.set_color('#FF4500')

# Annotating the highest calorie intake point
highest_intake = df['Calorie_Intake'].max()
highest_month = df[df['Calorie_Intake'] == highest_intake]['Month'].values[0]
plt.annotate(f'Highest\n{highest_month}', xy=(highest_month, highest_intake), 
             xytext=(highest_month, highest_intake+100),
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             ha='center')

# Adjust the plot to make it more readable
plt.xticks(rotation=45)
plt.title('Monthly Calorie Intake in 2023', pad=20)
plt.xlabel('Month')
plt.ylabel('Calorie Intake (kcal)')

# Show the line chart
plt.tight_layout()
plt.show()