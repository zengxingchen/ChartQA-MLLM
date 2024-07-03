
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Travelers': [1800, 1600, 2000, 2400, 3000, 3500, 3800, 3600, 3400, 3100, 2800, 2500]
}
df = pd.DataFrame(data)

# Ensure that the Month column is treated as categorical with the correct order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the aesthetic style of the plots
sns.set_theme()

# Create the area chart
plt.figure(figsize=(14, 7))
area_chart = sns.lineplot(data=df, x='Month', y='Travelers', sort=False, color='#FF6347')
area_chart.fill_between(df['Month'], df['Travelers'], alpha=0.4, color='#FFD700')

# Assign an annotation/text label on the chart for the highest number of travelers
plt.text(x='July', y=3800, s='Peak Travelers (3800)', color='red', va='bottom', ha='center')

# Set chart title and labels
plt.title('Monthly Travel Statistics', fontsize=18)
plt.xlabel('Month')
plt.ylabel('Number of Travelers')

# Finalize and show the plot
plt.tight_layout()
plt.show()