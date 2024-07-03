
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data inspired by average monthly temperatures of a city
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature_Celsius': [-2.8, -1.0, 3.2, 9.8, 15.6, 19.1, 22.0, 21.3, 16.7, 10.4, 4.1, -0.6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort data by temperature for better visualization
df = df.sort_values('Average_Temperature_Celsius')

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 8))

# Plot the data; since we want a horizontal bar chart, use 'barh' instead of 'bar'
sns.barplot(
    x="Average_Temperature_Celsius", 
    y="Month", 
    data=df,
    palette=['#FF6347', '#FF4500', '#FFD700', '#ADFF2F', '#7FFF00', '#32CD32', '#20B2AA', '#1E90FF', '#0000FF', '#8A2BE2', '#FF69B4', '#C71585'],
    edgecolor=".2",
    linewidth=1.5,
    orient='h'
)

# Set the bar width; in the case of 'barh', the bar width is actually controlled by 'height'
sns.set_context("poster", font_scale=0.8)
ax.bar_label(ax.containers[0], label_type='edge')

# Change the axes to set a more suitable limit and labels
ax.set_xlim(-5, 25)
ax.set_xlabel('Average Temperature (°C)')
ax.set_ylabel('Month')
ax.set_title('Average Monthly Temperatures of a City')

# Show the plot
plt.tight_layout()
plt.show()