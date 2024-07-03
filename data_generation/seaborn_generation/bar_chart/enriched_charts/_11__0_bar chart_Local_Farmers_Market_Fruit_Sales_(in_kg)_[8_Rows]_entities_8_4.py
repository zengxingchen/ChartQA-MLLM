
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Prepare the data
data = {
    "Age Group": ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"],
    "Average Stress Level": [7.5, 6.8, 6.3, 5.9, 5.2, 4.7]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a vertical bar chart
plt.figure(figsize=(10, 6))  # Change the size of the chart
sns.set_theme(style="whitegrid")
ax = sns.barplot(
    x="Age Group",
    y="Average Stress Level",
    data=df,
    palette=["#FF5733", "#33FF57", "#3357FF", "#57FF33", "#FF33A5", "#A533FF"],
    dodge=False)  # Vertical bar chart

# Set the width of the bars for better clarity
for bar in ax.patches:
    bar.set_width(0.5)  # Change the width of the bars

# Customizing chart
ax.set_ylabel("Average Stress Level")  # Modify y-axis label
ax.set_title("Average Stress Levels by Age Group")  # Change headline

plt.show()