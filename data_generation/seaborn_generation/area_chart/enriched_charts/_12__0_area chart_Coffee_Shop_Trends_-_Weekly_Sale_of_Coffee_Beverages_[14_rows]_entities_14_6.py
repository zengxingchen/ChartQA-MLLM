
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the above data
data = pd.DataFrame({
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Sales_Revenue": [15000, 18000, 22000, 27000, 35000, 40000, 45000, 43000, 38000, 31000, 25000, 20000]
})

# Set the figure size for better clarity
plt.figure(figsize=(14, 8))

# Create an area plot
sns.set_theme(style="whitegrid")
ax = sns.lineplot(
    x="Month",
    y="Sales_Revenue",
    data=data,
    color="#007ACC",
    linewidth=2
)
ax.fill_between(data["Month"], data["Sales_Revenue"], color="#66C2FF")

# Add annotation
for i in range(data.shape[0]):
    plt.text(data["Month"][i], data["Sales_Revenue"][i] + 500, str(data["Sales_Revenue"][i]) + ' USD', 
             horizontalalignment='center', size='small', color='black', weight='semibold')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Set chart title and labels
ax.set_title('Monthly Sales Revenue', fontsize=18, pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Sales Revenue (USD)', fontsize=14)

# Show the plot
plt.tight_layout()
plt.show()