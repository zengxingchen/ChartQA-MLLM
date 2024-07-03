
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Attendance': [800, 1200, 1600, 2000, 2500, 3000, 3800, 3600, 3200, 2800, 2200, 1800]
}
df = pd.DataFrame(data)

# Ensure that the Month column is treated as categorical with the correct order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the aesthetic style of the plots
sns.set_theme()

# Create the area chart
plt.figure(figsize=(16, 8))
area_chart = sns.lineplot(data=df, x='Month', y='Attendance', sort=False, color='#1f77b4')
area_chart.fill_between(df['Month'], df['Attendance'], alpha=0.3, color='#1f77b4')

# Assign an annotation/text label on the chart for the highest number of visitors
plt.text(x='July', y=3800, s='Peak Attendance (3800)', color='red', va='bottom', ha='center')

# Set chart title and labels
plt.title('Monthly Gym Attendance Trend')
plt.xlabel('Month')
plt.ylabel('Number of Attendees')

# Finalize and show the plot
plt.tight_layout()
plt.show()