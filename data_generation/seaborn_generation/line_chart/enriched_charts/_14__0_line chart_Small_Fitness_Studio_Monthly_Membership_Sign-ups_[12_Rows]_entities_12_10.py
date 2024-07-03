
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Running_Distance_km': [5, 7, 10, 12, 15, 18, 20, 17, 14, 10, 8, 6]
}
df = pd.DataFrame(data)

# Convert 'Month' to categorical type having an order because Seaborn sorts data by default
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Plotting
plt.figure(figsize=(12, 8))
running_distance_plot = sns.lineplot(x='Month', y='Average_Running_Distance_km', data=df,
                                     marker='o', color='#1f77b4', markersize=8)

# Annotations
for i in range(df.shape[0]):
    plt.text(df.Month[i], df.Average_Running_Distance_km[i] + 0.5, df.Average_Running_Distance_km[i],
             ha='center', va='bottom', fontsize=9)

# Customizations
running_distance_plot.set_title("Average Monthly Running Distance in Fitness Club", fontsize=14, pad=20)
running_distance_plot.set_xlabel("Month", fontsize=12)
running_distance_plot.set_ylabel("Average Running Distance (km)", fontsize=12)
sns.despine()

# Show plot
plt.tight_layout()
plt.show()