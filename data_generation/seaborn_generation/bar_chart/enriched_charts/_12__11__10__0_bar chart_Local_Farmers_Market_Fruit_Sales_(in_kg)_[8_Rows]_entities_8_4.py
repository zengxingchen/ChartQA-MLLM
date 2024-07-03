
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Prepare the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Visitors": [2500, 1800, 3000, 3500, 2800, 4000, 4500, 4200, 3700, 3200, 2900, 3100]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a vertical bar chart
plt.figure(figsize=(10, 6))  # Change the size of the chart
sns.set_theme(style="whitegrid")
ax = sns.barplot(
    x="Month",
    y="Visitors",
    data=df,
    palette=["#ff6347", "#4682b4", "#32cd32", "#ffa07a", "#dc143c", "#ff8c00",
             "#9932cc", "#8a2be2", "#ff69b4", "#adff2f", "#ff1493", "#7fffd4"],
    dodge=False)  # Vertical bar chart

# Set the width of the bars for better clarity
for bar in ax.patches:
    bar.set_width(0.5)  # Change the width of the bars

# Customizing chart
ax.set_ylabel("Number of Visitors")  # Modify y-axis label
ax.set_title("Monthly Visitors to National Park X", pad=20)  # Change headline
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

plt.show()