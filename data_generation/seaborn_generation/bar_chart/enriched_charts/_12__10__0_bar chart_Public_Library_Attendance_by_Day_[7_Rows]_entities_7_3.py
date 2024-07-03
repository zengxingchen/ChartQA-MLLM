
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data inspired by average monthly humidity of a city
data = {
    'Month': ['April', 'May', 'June', 'July', 'August', 'September', 
              'October', 'March', 'November', 'December', 'February', 'January'],
    'Average_Humidity_Percentage': [62, 55, 50, 45, 48, 53, 60, 68, 70, 75, 75, 78]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort data by humidity for better visualization
df = df.sort_values('Average_Humidity_Percentage')

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(14, 8))

# Plot the data; since we want a horizontal bar chart, use 'barh' instead of 'bar'
sns.barplot(
    x="Average_Humidity_Percentage", 
    y="Month", 
    data=df,
    palette=['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc948', '#b07aa1', '#ff9da7', '#9c755f', '#bab0ab', '#d4a6c8', '#86bc86'],
    edgecolor=".2",
    linewidth=1.2
)

# Set the bar width; in the case of 'barh', the bar height is actually controlled by 'height'
sns.set_context("poster", font_scale=0.9)
ax.bar_label(ax.containers[0], label_type='edge')

# Change the axes to set a more suitable limit and labels
ax.set_xlim(40, 80)
ax.set_xlabel('Average Humidity (%)')
ax.set_ylabel('Month')
ax.set_title('Average Monthly Humidity of a City', pad=20)

# Show the plot
plt.tight_layout()
plt.show()