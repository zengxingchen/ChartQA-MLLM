
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the above data
data = pd.DataFrame({
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Average_Temp": [5, 6, 10, 13, 17, 20, 22, 21, 19, 14, 9, 6]
})

# Set the figure size for better clarity
plt.figure(figsize=(12, 6))

# Create an area plot
sns.set_theme(style="whitegrid")
ax = sns.lineplot(
    x="Month",
    y="Average_Temp",
    data=data,
    color="#FF5733",
    linewidth=2
)
ax.fill_between(data["Month"], data["Average_Temp"], color="#FFC300")

# Add annotation
for i in range(data.shape[0]):
    plt.text(data["Month"][i], data["Average_Temp"][i] + 0.5, str(data["Average_Temp"][i]) + '°C', 
             horizontalalignment='center', size='small', color='black', weight='semibold')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Set chart title and labels
ax.set_title('Average Daily Temperature by Month', fontsize=16)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Average Temperature (°C)', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()