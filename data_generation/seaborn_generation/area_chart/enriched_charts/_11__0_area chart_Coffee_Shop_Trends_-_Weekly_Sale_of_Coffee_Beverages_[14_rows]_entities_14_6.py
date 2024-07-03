
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the above data
data = pd.DataFrame({
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Caloric_Intake": [2200, 2100, 2300, 2150, 2250, 2400, 2350]
})

# Set the figure size for better clarity
plt.figure(figsize=(14, 7))

# Create an area plot
sns.set_theme(style="whitegrid")
ax = sns.lineplot(
    x="Day",
    y="Caloric_Intake",
    data=data,
    color="#1f77b4",
    linewidth=2
)
ax.fill_between(data["Day"], data["Caloric_Intake"], color="#aec7e8")

# Add annotation
for i in range(data.shape[0]):
    plt.text(data["Day"][i], data["Caloric_Intake"][i] + 50, str(data["Caloric_Intake"][i]) + ' kcal', 
             horizontalalignment='center', size='small', color='black', weight='semibold')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=0)

# Set chart title and labels
ax.set_title('Daily Caloric Intake Over a Week', fontsize=18)
ax.set_xlabel('Day', fontsize=14)
ax.set_ylabel('Caloric Intake (kcal)', fontsize=14)

# Show the plot
plt.tight_layout()
plt.show()