
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the above data
data = pd.DataFrame({
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Visitors": [1200, 1800, 2500, 3100, 4200, 5300, 4100]
})

# Set the figure size for better clarity
plt.figure(figsize=(12, 6))

# Create an area plot
sns.set_theme(style="whitegrid")
ax = sns.lineplot(
    x="Day",
    y="Visitors",
    data=data,
    color="#2ca02c",
    linewidth=2
)
ax.fill_between(data["Day"], data["Visitors"], color="#98df8a")

# Add annotation
for i in range(data.shape[0]):
    plt.text(data["Day"][i], data["Visitors"][i] + 50, str(data["Visitors"][i]), 
             horizontalalignment='center', size='small', color='black', weight='semibold')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=0)

# Set chart title and labels
ax.set_title('Weekly Visitors to the Local Zoo', fontsize=16, pad=20)
ax.set_xlabel('Day of the Week', fontsize=12)
ax.set_ylabel('Number of Visitors', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()