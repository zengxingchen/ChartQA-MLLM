
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Prepare the data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "Visitors": [1200, 1500, 1800, 2400, 3000, 3500, 4000, 3800, 3200, 2700, 2000, 1600]
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
    palette=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6",
             "#c4e17f", "#76d7c4", "#ff6f61", "#6b5b95", "#88b04b", "#f7cac9"],
    dodge=False)  # Vertical bar chart

# Set the width of the bars for better clarity
for bar in ax.patches:
    bar.set_width(0.5)  # Change the width of the bars (which is effectively the height in a vertical bar chart)

# Customizing chart
ax.set_ylabel("Number of Visitors")  # Modify y-axis label
ax.set_title("Monthly Visitors to Museum Y")  # Change headline

plt.show()