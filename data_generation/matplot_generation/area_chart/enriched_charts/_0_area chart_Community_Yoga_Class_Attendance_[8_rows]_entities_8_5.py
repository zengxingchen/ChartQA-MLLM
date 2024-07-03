
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature': [5, 6, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the area chart
plt.figure(figsize=(12, 6))  # Modify width and height
sns.set(style="whitegrid")  # Set style

# Define the color palette as a list
colors = ["#3498db"]  # Single color for the area chart

# Create the area plot with annotations
area_plot = sns.lineplot(data=df, x='Month', y='Temperature', color=colors[0])
area_plot.fill_between(df['Month'], df['Temperature'], alpha=0.3, color=colors[0])

# Annotate each data point on the plot
for index, row in df.iterrows():
    plt.text(row['Month'], row['Temperature'] + 0.5, round(row['Temperature'], 2), 
             color='black', ha="center")

# Set the title and labels
plt.title('Average Monthly Temperature in City XYZ', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')

# Show the plot.
plt.show()