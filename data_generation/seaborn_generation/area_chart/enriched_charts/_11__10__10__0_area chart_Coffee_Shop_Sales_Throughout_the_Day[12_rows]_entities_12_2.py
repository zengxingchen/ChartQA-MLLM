
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Visitors': [1000, 1100, 1200, 1500, 1800, 2000, 2200, 2100, 1900, 1600, 1400, 1200]
}
df = pd.DataFrame(data)

# Ensure that the Month column is treated as categorical with the correct order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the aesthetic style of the plots
sns.set_theme()

# Create the area chart
plt.figure(figsize=(14, 7))
area_chart = sns.lineplot(data=df, x='Month', y='Visitors', sort=False, color='#ff6347')
area_chart.fill_between(df['Month'], df['Visitors'], alpha=0.4, color='#ff6347')

# Assign an annotation/text label on the chart for the highest number of visitors
plt.text(x='July', y=2200, s='Peak Visitors (2200)', color='blue', va='bottom', ha='center')

# Set chart title and labels
plt.title('Monthly Visitor Numbers at the Museum', loc='center', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Visitors')

# Finalize and show the plot
plt.tight_layout()
plt.show()