
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Monthly revenue data for a fictional retail store.
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [50000, 52000, 48000, 47000, 56000, 58000, 53000, 54000, 49000, 61000, 63000, 60000]
}
# Create a DataFrame.
df = pd.DataFrame(data)
# Convert 'Month' to categorical type with ordered categories.
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the color palette with specific color codes.
colors = ["#FF5733", "#33FF57", "#3357FF", "#57FFF3", "#F357FF", "#FF5733", "#33FF57", "#3357FF", "#57FFF3", "#F357FF", "#FF5733", "#33FF57"]

# Initialize the matplotlib figure.
plt.figure(figsize=(12, 6))

# Plot the data. Every point has a different color specified from the colors list.
sns.lineplot(data=df, x='Month', y='Revenue', palette=colors, marker='o', linewidth=2.5)

# Adding annotations for the beginning, middle, and end of the year.
plt.text(0, df['Revenue'][0], f"${df['Revenue'][0]:,}", color='black', ha="center")
plt.text(5, df['Revenue'][5], f"${df['Revenue'][5]:,}", color='black', ha="center")
plt.text(11, df['Revenue'][11], f"${df['Revenue'][11]:,}", color='black', ha="center")

# Customizing the axes and title.
plt.title('Monthly Revenue for Fictional Retail Store in 2023', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot.
plt.show()