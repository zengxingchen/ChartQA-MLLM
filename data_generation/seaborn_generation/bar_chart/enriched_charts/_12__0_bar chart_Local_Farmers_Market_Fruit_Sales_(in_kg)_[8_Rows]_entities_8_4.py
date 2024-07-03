
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Prepare the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Steps": [5000, 7000, 8000, 10000, 12000, 15000, 17000, 16000, 14000, 11000, 9000, 6000]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a vertical bar chart
plt.figure(figsize=(10, 6))  # Change the size of the chart
sns.set_theme(style="whitegrid")
ax = sns.barplot(
    x="Month",
    y="Steps",
    data=df,
    palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b",
             "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#c5b0d5", "#9edae5"],
    orient="v")  # Vertical bar chart

# Set the width of the bars for better clarity
for bar in ax.patches:
    bar.set_width(0.5)  # Change the width of the bars

# Customizing chart
ax.set_ylabel("Average Daily Steps")  # Modify y-axis label
ax.set_title("Average Daily Steps per Month for a Health Study")  # Change headline
plt.xticks(rotation=45)  # Rotate month labels for better readability

plt.show()