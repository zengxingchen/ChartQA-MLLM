
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature_C': [-2, 0, 5, 10, 15, 20, 25, 23, 18, 12, 5, -1]
}
df = pd.DataFrame(data)

# Convert 'Month' to categorical type having an order because Seaborn sorts data by default
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Plotting
plt.figure(figsize=(10, 6))
temperature_plot = sns.lineplot(x='Month', y='Average_Temperature_C', data=df,
                                marker='o', color='#ff7f0e', markersize=8)

# Annotations
for i in range(df.shape[0]):
    plt.text(df.Month[i], df.Average_Temperature_C[i] + 0.5, df.Average_Temperature_C[i],
             ha='center', va='bottom', fontsize=9)

# Customizations
temperature_plot.set_title("Average Monthly Temperature in Fictional City", fontsize=14)
temperature_plot.set_xlabel("Month", fontsize=12)
temperature_plot.set_ylabel("Average Temperature (°C)", fontsize=12)
sns.despine()

# Show plot
plt.tight_layout()
plt.show()