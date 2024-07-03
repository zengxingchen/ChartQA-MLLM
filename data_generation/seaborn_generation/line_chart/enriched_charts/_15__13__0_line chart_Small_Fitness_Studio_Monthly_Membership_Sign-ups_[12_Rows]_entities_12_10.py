
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Sunspots': [15, 12, 18, 20, 22, 25, 30, 35, 40, 38, 32, 28]
}
df = pd.DataFrame(data)

# Convert 'Month' to categorical type having an order because Seaborn sorts data by default
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Plotting
plt.figure(figsize=(14, 10))
sunspot_plot = sns.lineplot(x='Month', y='Sunspots', data=df,
                            marker='o', color='#ff6347', markersize=8)

# Annotations
for i in range(df.shape[0]):
    plt.text(df.Month[i], df.Sunspots[i] + 0.5, df.Sunspots[i],
             ha='center', va='bottom', fontsize=9)

# Customizations
sunspot_plot.set_title("Monthly Sunspot Counts in 2023", fontsize=16)
sunspot_plot.set_xlabel("Month", fontsize=12)
sunspot_plot.set_ylabel("Number of Sunspots", fontsize=12)
sns.despine()

# Show plot
plt.tight_layout()
plt.show()