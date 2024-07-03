
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Participants': [80, 75, 85, 90, 95, 100, 105, 110, 120, 125, 130, 135]
}
df = pd.DataFrame(data)

# Convert 'Month' to categorical type having an order because Seaborn sorts data by default
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Plotting
plt.figure(figsize=(16, 8))
participants_plot = sns.lineplot(x='Month', y='Participants', data=df,
                                 marker='o', color='#1f77b4', markersize=8)

# Annotations
for i in range(df.shape[0]):
    plt.text(df.Month[i], df.Participants[i] + 1, df.Participants[i],
             ha='center', va='bottom', fontsize=9)

# Customizations
participants_plot.set_title("Monthly Participants in Online Learning Course", fontsize=16, pad=20)
participants_plot.set_xlabel("Month", fontsize=12)
participants_plot.set_ylabel("Number of Participants", fontsize=12)
sns.despine()

# Show plot
plt.tight_layout()
plt.show()