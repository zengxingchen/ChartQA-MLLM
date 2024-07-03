
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Number_of_Tourists': [1200, 1500, 1800, 2000, 2200, 2500, 2700, 2600, 2300, 2100, 1600, 1300]
}
df = pd.DataFrame(data)

# Convert 'Month' to categorical type having an order because Seaborn sorts data by default
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Plotting
plt.figure(figsize=(12, 8))
tourist_plot = sns.lineplot(x='Month', y='Number_of_Tourists', data=df,
                            marker='o', color='#1f77b4', markersize=8)

# Annotations
for i in range(df.shape[0]):
    plt.text(df.Month[i], df.Number_of_Tourists[i] + 50, df.Number_of_Tourists[i],
             ha='center', va='bottom', fontsize=9)

# Customizations
tourist_plot.set_title("Monthly Tourist Visits in Fictional City", fontsize=16, pad=20)
tourist_plot.set_xlabel("Month", fontsize=14)
tourist_plot.set_ylabel("Number of Tourists", fontsize=14)
sns.despine()

# Show plot
plt.tight_layout()
plt.show()