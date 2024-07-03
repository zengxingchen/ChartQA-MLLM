
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the given table data
data = [
    {'Class': 'Yoga', 'Attendees': 25},
    {'Class': 'Water Aerobics', 'Attendees': 18},
    {'Class': 'Pilates', 'Attendees': 20},
    {'Class': 'Salsa Dancing', 'Attendees': 15},
    {'Class': 'Cooking for Beginners', 'Attendees': 22},
    {'Class': 'Photography', 'Attendees': 10},
    {'Class': 'Cycling', 'Attendees': 27}
]
df = pd.DataFrame(data)

# Sort the DataFrame by the number of Attendees to have a sorted bar chart
df_sorted = df.sort_values('Attendees', ascending=True)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(8, 6))

# Create a palette with a color for each class based on the number of attendees
palette = sns.color_palette("coolwarm", len(df_sorted['Attendees']))

# Plot the bar chart
sns.barplot(
    x='Attendees',
    y='Class',
    data=df_sorted,
    palette=palette,
    edgecolor=".2"
)

# Add the attendee counts on the bars
for index, row in df_sorted.iterrows():
    ax.text(
        row['Attendees'],  # X location of text
        index,  # Y location
        f' {row["Attendees"]}',  # Text (with space for padding)
        color='black',
        va='center'
    )

# Finalize the plot with labels, title, and aesthetics
ax.set_title('Class Attendance')
ax.set_xlabel('Number of Attendees')
ax.set_ylabel('Class Name')
sns.despine(left=True, bottom=True)  # Remove spines

# Show the plot
plt.show()