
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Prepare the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Visitors": [1300, 1700, 1600, 2300, 3100, 3300, 4100, 3700, 3100, 2800, 1900, 1800]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a horizontal bar chart
plt.figure(figsize=(12, 8))  # Change the size of the chart
sns.set_theme(style="whitegrid")
ax = sns.barplot(
    y="Month",
    x="Visitors",
    data=df,
    palette=["#ff4c4c", "#1f78b4", "#33a02c", "#fb9a99", "#e31a1c", "#fdbf6f",
             "#ff7f00", "#cab2d6", "#6a3d9a", "#ffff99", "#b2df8a", "#a6cee3"],
    dodge=False)  # Horizontal bar chart

# Set the height of the bars for better clarity
for bar in ax.patches:
    bar.set_height(0.6)  # Change the height of the bars

# Customizing chart
ax.set_xlabel("Number of Visitors")  # Modify x-axis label
ax.set_title("Monthly Visitors to Art Gallery Z", pad=20)  # Change headline

plt.show()