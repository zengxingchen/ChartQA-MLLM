
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
data = [
    {'Day of the Week': 'Monday', 'Number of Visitors': 80},
    {'Day of the Week': 'Tuesday', 'Number of Visitors': 105},
    {'Day of the Week': 'Wednesday', 'Number of Visitors': 95},
    {'Day of the Week': 'Thursday', 'Number of Visitors': 120},
    {'Day of the Week': 'Friday', 'Number of Visitors': 110},
    {'Day of the Week': 'Saturday', 'Number of Visitors': 130},
    {'Day of the Week': 'Sunday', 'Number of Visitors': 70}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Create the area plot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
ax = sns.lineplot(x='Day of the Week', y='Number of Visitors', data=df, marker='o', sort=False)

# Setting x-axis labels to show every day of the week
ax.set_xticks(df['Day of the Week'])
ax.set_xticklabels(df['Day of the Week'], rotation=45) # Rotate x labels for better readability

# Fill the area under the plot
plt.fill_between(df['Day of the Week'], df['Number of Visitors'], alpha=0.3)

# Add a title and labels
plt.title('Number of Visitors by Day of the Week', fontsize=16)
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Number of Visitors', fontsize=14)

# Remove the right and top spines
sns.despine()

# Show the plot
plt.show()