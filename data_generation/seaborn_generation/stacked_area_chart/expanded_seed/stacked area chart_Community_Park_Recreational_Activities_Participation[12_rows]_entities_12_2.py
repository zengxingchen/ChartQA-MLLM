
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Provided data
data = [
    {'Month': 'January', 'Jogging': 230, 'Cycling': 150, 'Yoga Classes': 60, 'Soccer': 250, 'Basketball': 200, 'Tennis': 180, 'Outdoor Gym': 110, 'Picnics': 300, 'Fishing': 80, 'Bird Watching': 120},
    {'Month': 'February', 'Jogging': 240, 'Cycling': 160, 'Yoga Classes': 65, 'Soccer': 260, 'Basketball': 210, 'Tennis': 190, 'Outdoor Gym': 120, 'Picnics': 310, 'Fishing': 85, 'Bird Watching': 125},
    # ... (remaining data)
    {'Month': 'December', 'Jogging': 250, 'Cycling': 200, 'Yoga Classes': 70, 'Soccer': 260, 'Basketball': 220, 'Tennis': 190, 'Outdoor Gym': 110, 'Picnics': 320, 'Fishing': 90, 'Bird Watching': 140}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Set the index to the Month column to facilitate plotting
df.set_index('Month', inplace=True)

# Normalize month names to ensure they are plotted in temporal order
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
df = df.reindex(months_order)

# Plotting each activity one on top of the other to create a stacked effect
fig, ax = plt.subplots(figsize=(12, 6))
activities = df.columns  # All columns except 'Month'

# Starting point for the stack
start = [0] * df.shape[0]

for activity in activities:
    ax.fill_between(df.index, start, start + df[activity].values, label=activity)
    # Update starting height for the next stack
    start += df[activity].values

# Customizing the plot
ax.set_title('Monthly Activity Participation')
ax.set_ylabel('Number of Participants')
ax.set_xlabel('Month')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Activity')
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot with a legend outside the axes
plt.show()