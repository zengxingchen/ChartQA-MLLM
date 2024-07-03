
import seaborn as sns
import matplotlib.pyplot as plt

# Your table data
data = [
    {'Profession': 'Software Developer', 'Cups of Coffee Per Day': 3},
    {'Profession': 'Nurse', 'Cups of Coffee Per Day': 4},
    {'Profession': 'Teacher', 'Cups of Coffee Per Day': 2},
    {'Profession': 'Police Officer', 'Cups of Coffee Per Day': 2}
]

# Convert your table data into a suitable format for Seaborn
import pandas as pd
df = pd.DataFrame(data)

# Start the figure
plt.figure(figsize=(10, 6))

# Create a barplot
barplot = sns.barplot(
    x='Profession', 
    y='Cups of Coffee Per Day', 
    data=df,
    palette='viridis',        # Use a diverging color palette
    edgecolor='black',        # Add a border to the bars
    linewidth=1.5,            # Set the width of the bar borders
    hatch='///',              # Add a pattern to the bars
)

# Customize further details
plt.title('Cups of Coffee Per Day by Profession', fontsize=16)
plt.xlabel('Profession', fontsize=14)
plt.ylabel('Cups of Coffee Per Day', fontsize=14)
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

# Add value labels to the bars
for p in barplot.patches:
    barplot.annotate(f"{int(p.get_height())}",
                     (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='center',
                     fontsize=12, color='black', 
                     xytext=(0, 9),
                     textcoords='offset points')

# Show the plot
plt.tight_layout()
plt.show()