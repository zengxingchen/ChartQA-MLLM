
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Temperature': [4, 5, 10, 14, 18, 22, 25, 24, 20, 15, 9, 5]
}
df = pd.DataFrame(data)

# Ensure that the Month column is treated as categorical with the correct order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the aesthetic style of the plots
sns.set_theme()

# Create the area chart
plt.figure(figsize=(12, 6))
area_chart = sns.lineplot(data=df, x='Month', y='Temperature', sort=False)
area_chart.fill_between(df['Month'], df['Temperature'], alpha=0.3, color='#1f77b4')

# Assign an annotation/text label on the chart for the highest average temperature
plt.text(x='July', y=25, s='Peak Temperature (25°C)', color='red', va='bottom', ha='center')

# Set chart title and labels
plt.title('Monthly Average Temperature Trend in a City')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')

# Finalize and show the plot
plt.tight_layout()
plt.show()