
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data inspired by average time spent on different physical activities per week
data = {
    'Activity': ['Running', 'Swimming', 'Cycling', 'Yoga', 'Weightlifting', 'Basketball', 
                 'Hiking', 'Dancing', 'Tennis', 'Soccer', 'Pilates', 'Boxing'],
    'Average_Time_Hours': [3.5, 2.0, 4.0, 1.5, 2.5, 3.0, 2.0, 2.5, 1.0, 2.0, 1.5, 1.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort data by time for better visualization
df = df.sort_values('Average_Time_Hours')

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 6))

# Plot the data
sns.barplot(
    y="Average_Time_Hours", 
    x="Activity", 
    data=df,
    palette=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#FFD433', '#33FFF2', '#FF8F33', '#75FF33', '#FF3333', '#33D4FF', '#3338FF'],
    edgecolor=".2",
    linewidth=1.2
)

# Set the bar height
sns.set_context("poster", font_scale=0.7)
ax.bar_label(ax.containers[0], label_type='edge')

# Change the axes to set a more suitable limit and labels
ax.set_ylim(0, 5)
ax.set_xlabel('Activity')
ax.set_ylabel('Average Time (Hours)')
ax.set_title('Average Time Spent on Different Physical Activities per Week')

# Show the plot
plt.tight_layout()
plt.show()