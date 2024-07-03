
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data inspired by average monthly humidity of a city
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Humidity_Percentage': [78, 75, 68, 62, 55, 50, 45, 48, 53, 60, 70, 75]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort data by humidity for better visualization
df = df.sort_values('Average_Humidity_Percentage')

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 6))

# Plot the data; since we want a vertical bar chart, use 'bar' instead of 'barh'
sns.barplot(
    x="Month", 
    y="Average_Humidity_Percentage", 
    data=df,
    palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ff9896', '#c5b0d5'],
    edgecolor=".2",
    linewidth=1.5
)

# Set the bar width; in the case of 'bar', the bar width is actually controlled by 'width'
sns.set_context("poster", font_scale=0.8)
ax.bar_label(ax.containers[0], label_type='edge')

# Change the axes to set a more suitable limit and labels
ax.set_ylim(40, 80)
ax.set_ylabel('Average Humidity (%)')
ax.set_xlabel('Month')
ax.set_title('Average Monthly Humidity of a City', pad=20)

# Show the plot
plt.tight_layout()
plt.show()