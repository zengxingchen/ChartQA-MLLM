
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'Day': 'Monday', 'Visitors': 300},
    {'Day': 'Tuesday', 'Visitors': 250},
    {'Day': 'Wednesday', 'Visitors': 270},
    {'Day': 'Thursday', 'Visitors': 320},
    {'Day': 'Friday', 'Visitors': 230},
    {'Day': 'Saturday', 'Visitors': 380},
    {'Day': 'Sunday', 'Visitors': 410}
]

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Set the context to "talk" for larger elements, suitable for presentations
sns.set_context("talk")

# Create a color palette
palette = sns.color_palette("husl", len(df))

# Create the bar plot
plt.figure(figsize=(10, 6)) # Adjust the size of the figure
bar_plot = sns.barplot(x='Day', y='Visitors', data=df, palette=palette)

# Add labels to the plot
plt.title('Visitors by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Visitors')

# Optional: rotate x-axis labels if they are too long or for better readability
plt.xticks(rotation=45)

# Show the plot
plt.show()