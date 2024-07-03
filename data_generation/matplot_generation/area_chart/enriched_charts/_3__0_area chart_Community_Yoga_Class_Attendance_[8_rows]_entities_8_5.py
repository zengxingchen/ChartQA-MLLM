
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [3000, 3200, 3500, 3800, 4200, 4500, 4700, 4900, 4600, 4300, 4000, 3700]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the area chart
plt.figure(figsize=(14, 8))  # Modify width and height
sns.set(style="whitegrid")  # Set style

# Define the color palette as a list
colors = ["#2ecc71"]  # Single color for the area chart

# Create the area plot with annotations
area_plot = sns.lineplot(data=df, x='Month', y='Revenue', color=colors[0])
area_plot.fill_between(df['Month'], df['Revenue'], alpha=0.3, color=colors[0])

# Annotate each data point on the plot
for index, row in df.iterrows():
    plt.text(row['Month'], row['Revenue'] + 100, round(row['Revenue'], 2), 
             color='black', ha="center")

# Set the title and labels
plt.title('Monthly Revenue in 2024', fontsize=16, pad=20)
plt.xlabel('Month')
plt.ylabel('Revenue ($)')

# Show the plot
plt.show()