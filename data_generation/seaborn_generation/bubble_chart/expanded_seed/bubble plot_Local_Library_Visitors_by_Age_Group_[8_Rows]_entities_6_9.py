
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given dataset
data = [
    {'Age Group': '0-12', 'Week 1': 120, 'Week 2': 130, 'Week 3': 110, 'Week 4': 140, 'Total Visitors': 500, 'Area (sq ft)': 450},
    {'Age Group': '13-19', 'Week 1': 95, 'Week 2': 100, 'Week 3': 90, 'Week 4': 85, 'Total Visitors': 370, 'Area (sq ft)': 600},
    {'Age Group': '20-35', 'Week 1': 210, 'Week 2': 190, 'Week 3': 220, 'Week 4': 205, 'Total Visitors': 825, 'Area (sq ft)': 750},
    {'Age Group': '36-50', 'Week 1': 170, 'Week 2': 160, 'Week 3': 165, 'Week 4': 175, 'Total Visitors': 670, 'Area (sq ft)': 500},
    {'Age Group': '51-65', 'Week 1': 130, 'Week 2': 120, 'Week 3': 125, 'Week 4': 140, 'Total Visitors': 515, 'Area (sq ft)': 550},
    {'Age Group': '66+', 'Week 1': 60, 'Week 2': 70, 'Week 3': 65, 'Week 4': 75, 'Total Visitors': 270, 'Area (sq ft)': 400}
]

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Calculate size for bubble sizes - normalizing the 'Total Visitors' value to improve visualization
size_scale = 1000  # Adjust this value to increase/decrease bubble sizes
df['Bubble Size'] = df['Total Visitors'] / size_scale

# Create the bubble chart
plt.figure(figsize=(10, 8))
bubble_plot = sns.scatterplot(data=df, x="Area (sq ft)", y="Total Visitors", size="Bubble Size",
                              sizes=(100, 2000),  # Adjust the range of bubble sizes
                              hue="Age Group", legend=False, palette="viridis", alpha=0.6)

# Customize the plot with titles and labels
plt.title('Total Visitors vs Area by Age Group', fontsize=16)
plt.xlabel('Area (sq ft)', fontsize=14)
plt.ylabel('Total Visitors', fontsize=14)

# Annotating each bubble with the corresponding Age Group
for line in range(0, df.shape[0]):
     bubble_plot.text(df["Area (sq ft)"][line]+10, df["Total Visitors"][line], df["Age Group"][line], 
                      horizontalalignment='left', size='medium', color='black', weight='semibold')

plt.grid(True)
plt.show()