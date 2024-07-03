
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Prepare the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Temperature": [-5, -3, 2, 10, 16, 20, 22, 21, 17, 11, 4, -2]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a horizontal bar chart
plt.figure(figsize=(12, 8))  # Change the size of the chart
sns.set_theme(style="whitegrid")
ax = sns.barplot(
    x="Temperature",
    y="Month",
    data=df,
    palette=["#334455", "#556677", "#778899", "#99aabb", "#aabccc", "#bbcddd",
             "#ccddee", "#ddeeff", "#eff0f1", "#f0f1f2", "#f1f2f3", "#f2f3f4"],
    orient="h",
    dodge=False)  # Horizontal bar chart

# Set the width of the bars for better clarity
for bar in ax.patches:
    bar.set_height(0.5)  # Change the height of the bars (which is effectively the width in a horizontal bar chart)

# Customizing chart
ax.set_xlabel("Average Monthly Temperature (°C)")  # Modify x-axis label
ax.set_title("Average Monthly Temperatures for Region X")  # Change headline

plt.show()