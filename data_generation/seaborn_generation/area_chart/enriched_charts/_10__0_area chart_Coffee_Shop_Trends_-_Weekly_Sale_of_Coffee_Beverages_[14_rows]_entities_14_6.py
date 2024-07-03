
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the above data
data = pd.DataFrame({
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Visitors": [500, 800, 1200, 1800, 2300, 3000, 3500, 3200, 2800, 2000, 1200, 700]
})

# Set the figure size for better clarity
plt.figure(figsize=(14, 7))

# Create an area plot
sns.set_theme(style="whitegrid")
ax = sns.lineplot(
    x="Month",
    y="Visitors",
    data=data,
    color="#1f77b4",
    linewidth=2
)
ax.fill_between(data["Month"], data["Visitors"], color="#aec7e8")

# Add annotation
for i in range(data.shape[0]):
    plt.text(data["Month"][i], data["Visitors"][i] + 50, str(data["Visitors"][i]), 
             horizontalalignment='center', size='small', color='black', weight='semibold')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Set chart title and labels
ax.set_title('Monthly Visitors to a National Park', fontsize=16)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Number of Visitors', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()