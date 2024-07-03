
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'Week': '2023-02-01', 'Running Club Members': 45, 'Aerobics Classes Attendance': 30, 'Yoga Studio Visits': 25, 'Swimming Pool Laps': 15},
    {'Week': '2023-02-08', 'Running Club Members': 50, 'Aerobics Classes Attendance': 34, 'Yoga Studio Visits': 20, 'Swimming Pool Laps': 18},
    # ... (other data points here) ...
    {'Week': '2023-04-12', 'Running Club Members': 70, 'Aerobics Classes Attendance': 54, 'Yoga Studio Visits': 47, 'Swimming Pool Laps': 35},
    {'Week': '2023-04-19', 'Running Club Members': 72, 'Aerobics Classes Attendance': 55, 'Yoga Studio Visits': 50, 'Swimming Pool Laps': 37}
]

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'Week' column to datetime for proper plotting
df['Week'] = pd.to_datetime(df['Week'])

# Reshape the DataFrame for Seaborn
df_melted = df.melt(id_vars='Week', var_name='Activity', value_name='Count')

# Start plotting
sns.set_style("whitegrid")
plt.figure(figsize=(14, 8))

# Plot each activity with a loop to add diversification in styles
activities = df_melted['Activity'].unique()
palette = sns.color_palette("tab10", len(activities))
line_styles = ["-", "--", "-.", ":"]
markers = ["o", "s", "^", "P"]

for i, activity in enumerate(activities):
    sns.lineplot(
        x='Week',
        y='Count',
        data=df_melted[df_melted['Activity'] == activity],
        label=activity,
        linewidth=2.5,
        linestyle=line_styles[i % len(line_styles)],
        marker=markers[i % len(markers)],
        markersize=8,
        color=palette[i]
    )

# Customize the ticks and labels
plt.xticks(rotation=45)
plt.xlabel('Week', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.title('Weekly Activity Overview', fontsize=16)

# Place the legend outside the plot
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Tighten the layout and show the plot
plt.tight_layout()
plt.show()