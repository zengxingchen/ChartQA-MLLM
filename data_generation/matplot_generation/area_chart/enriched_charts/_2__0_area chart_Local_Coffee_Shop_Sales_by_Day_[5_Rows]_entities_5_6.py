
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'AvgCalorieIntake': [2000, 2200, 2300, 2100, 2400, 2500, 2600, 2550, 2450, 2350, 2250, 2150]
}
df = pd.DataFrame(data)

# Convert 'Month' to categorical type with proper order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Create the area chart
plt.figure(figsize=(14, 9))
sns.set_theme(style="whitegrid")
area_chart = sns.lineplot(data=df, x='Month', y='AvgCalorieIntake', sort=False, lw=2, color='#FF5733')

# Filling the area under the line
plt.fill_between(x=df['Month'], y1=df['AvgCalorieIntake'], color='#FFC300', alpha=0.6)

# Annotate the chart with text labels
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['AvgCalorieIntake'][i]+20, str(df['AvgCalorieIntake'][i])+' kcal', horizontalalignment='center')

# Customize the axes
area_chart.set_xlabel('Month')
area_chart.set_ylabel('Average Calorie Intake (kcal)')
area_chart.set_title('Average Monthly Calorie Intake', pad=20)

# Show the final plot
plt.show()