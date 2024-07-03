
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# The given dataset
data = [
    {'Chore': 'Cooking', 'Time (Minutes per Week)': 210},
    {'Chore': 'Cleaning', 'Time (Minutes per Week)': 130},
    {'Chore': 'Laundry', 'Time (Minutes per Week)': 95},
    {'Chore': 'Dishwashing', 'Time (Minutes per Week)': 70},
    {'Chore': 'Gardening', 'Time (Minutes per Week)': 40},
    {'Chore': 'Grocery Shopping', 'Time (Minutes per Week)': 60},
    {'Chore': 'Pet Care', 'Time (Minutes per Week)': 105},
    {'Chore': 'Managing Finances', 'Time (Minutes per Week)': 45}
]

# Convert the dataset to a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 6))

# Customize the palette for the bar colors
palette = sns.color_palette("husl", len(data))

# Create the barplot
sns.barplot(
    x="Time (Minutes per Week)",
    y="Chore",
    data=df,
    palette=palette,
    edgecolor=".2"  # Adding a bit of edgecolor for better separation
)

# Customize the aesthetics
sns.set_style("whitegrid")
ax.set_title('Weekly Time Spent on Different Chores')
ax.set_xlabel('Time (Minutes per Week)')
ax.set_ylabel('Chore')

# Add a vertical line for median time spent across all chores
median_time = df["Time (Minutes per Week)"].median()
ax.axvline(median_time, color='red', linestyle='--')

# Annotating the median line
ax.text(median_time + 3, 0.5, f'Median: {median_time}', color='red', va='center', fontweight='bold')

# Remove the left, top, and right frame lines
sns.despine(trim=True)

# Finally show the plot
plt.tight_layout()
plt.show()