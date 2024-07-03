
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue_kUSD': [10, 15, 18, 22, 30, 35, 40, 45, 48, 50, 55, 60]
}
df = pd.DataFrame(data)

# Convert 'Month' to categorical type having an order because Seaborn sorts data by default
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Plotting
plt.figure(figsize=(12, 8))
revenue_plot = sns.lineplot(x='Month', y='Revenue_kUSD', data=df,
                            marker='o', color='#1f77b4', markersize=8)

# Annotations
for i in range(df.shape[0]):
    plt.text(df.Month[i], df.Revenue_kUSD[i] + 0.5, df.Revenue_kUSD[i],
             ha='center', va='bottom', fontsize=9)

# Customizations
revenue_plot.set_title("Monthly Revenue of a Startup (kUSD)", fontsize=16)
revenue_plot.set_xlabel("Month", fontsize=12)
revenue_plot.set_ylabel("Revenue (kUSD)", fontsize=12)
sns.despine()

# Show plot
plt.tight_layout()
plt.show()