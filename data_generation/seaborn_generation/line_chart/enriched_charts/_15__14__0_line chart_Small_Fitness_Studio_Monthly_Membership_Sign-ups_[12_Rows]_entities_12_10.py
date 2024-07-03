
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Daily_Exercise_Time_minutes': [30, 35, 40, 45, 50, 55, 60, 58, 52, 48, 42, 38]
}
df = pd.DataFrame(data)

# Convert 'Month' to categorical type having an order because Seaborn sorts data by default
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Plotting
plt.figure(figsize=(14, 9))
exercise_time_plot = sns.lineplot(x='Month', y='Average_Daily_Exercise_Time_minutes', data=df,
                                  marker='o', color='#ff6347', markersize=8)

# Annotations
for i in range(df.shape[0]):
    plt.text(df.Month[i], df.Average_Daily_Exercise_Time_minutes[i] + 0.5, df.Average_Daily_Exercise_Time_minutes[i],
             ha='center', va='bottom', fontsize=9)

# Customizations
exercise_time_plot.set_title("Average Daily Exercise Time in Health Club", fontsize=16, pad=20)
exercise_time_plot.set_xlabel("Month", fontsize=12)
exercise_time_plot.set_ylabel("Average Daily Exercise Time (minutes)", fontsize=12)
sns.despine()

# Show plot
plt.tight_layout()
plt.show()