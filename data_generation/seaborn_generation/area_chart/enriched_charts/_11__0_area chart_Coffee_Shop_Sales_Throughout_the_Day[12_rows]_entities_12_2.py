
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Visitors': [1500, 1600, 2200, 2800, 3500, 4200, 4700, 4500, 4000, 3200, 2500, 1800]
}
df = pd.DataFrame(data)

# Ensure that the Month column is treated as categorical with the correct order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the aesthetic style of the plots
sns.set_theme()

# Create the area chart
plt.figure(figsize=(14, 7))
area_chart = sns.lineplot(data=df, x='Month', y='Visitors', sort=False, color='#2ca02c')
area_chart.fill_between(df['Month'], df['Visitors'], alpha=0.3, color='#2ca02c')

# Assign an annotation/text label on the chart for the highest number of visitors
plt.text(x='July', y=4700, s='Peak Visitors (4700)', color='blue', va='bottom', ha='center')

# Set chart title and labels
plt.title('Monthly Visitor Trend in a National Park')
plt.xlabel('Month')
plt.ylabel('Number of Visitors')

# Finalize and show the plot
plt.tight_layout()
plt.show()