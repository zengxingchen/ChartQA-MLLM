
import matplotlib.pyplot as plt

# Data
sports = [
    "Running", "Cycling", "Swimming", "Yoga", "Hiking",
    "Basketball", "Soccer", "Tennis", "Golf", "Baseball",
    "Surfing", "Gymnastics"
]
participants = [150, 120, 95, 200, 175, 80, 130, 85, 60, 70, 50, 90]

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(12, 8))

# Vertical bar chart
bars = ax.bar(sports, participants, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#9edae5', '#f7b6d2'], width=0.6)

# Set the title and labels
ax.set_title('Number of Participants in Various Sports', fontsize=15)
ax.set_xlabel('Sport', fontsize=12)
ax.set_ylabel('Participants', fontsize=12)
ax.set_ylim(40, 210)  # Set y-axis limits

# Remove the spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Set grid to be behind the bars
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)

# Show Values on Bars
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 5
    ax.text(bar.get_x() + bar.get_width() / 2, label_y_pos, f'{height}',
            ha='center', va='bottom')

# Set the layout to be tight
plt.tight_layout()

# Show the plot
plt.show()