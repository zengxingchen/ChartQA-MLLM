
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Monthly visitors data for a fictional travel website.
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Visitors': [15000, 18000, 22000, 21000, 25000, 27000, 30000, 32000, 29000, 26000, 24000, 28000]
}
# Create a DataFrame.
df = pd.DataFrame(data)
# Convert 'Month' to categorical type with ordered categories.
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the color palette with specific color codes.
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#1f77b4", "#ff7f0e"]

# Initialize the matplotlib figure.
plt.figure(figsize=(14, 8))

# Plot the data.
sns.lineplot(data=df, x='Month', y='Visitors', palette=colors, marker='o', linewidth=2.5)

# Adding annotations for selected months.
plt.text(0, df['Visitors'][0], f"{df['Visitors'][0]:,}", color='black', ha="center")
plt.text(6, df['Visitors'][6], f"{df['Visitors'][6]:,}", color='black', ha="center")
plt.text(11, df['Visitors'][11], f"{df['Visitors'][11]:,}", color='black', ha="center")

# Customizing the axes and title.
plt.title('Monthly Visitors for Fictional Travel Website in 2023', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Visitors', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot.
plt.show()