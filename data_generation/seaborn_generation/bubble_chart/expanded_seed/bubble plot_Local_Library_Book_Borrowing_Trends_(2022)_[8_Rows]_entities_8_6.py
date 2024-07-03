
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Convert the chart table data into a pandas DataFrame
data = [
    {'Month': 'January', 'Total Books Borrowed': 1200, 'Library Visitors': 800, 'Average Borrowing Time (days)': 14},
    {'Month': 'February', 'Total Books Borrowed': 1150, 'Library Visitors': 790, 'Average Borrowing Time (days)': 12},
    {'Month': 'March', 'Total Books Borrowed': 1300, 'Library Visitors': 850, 'Average Borrowing Time (days)': 16},
    {'Month': 'April', 'Total Books Borrowed': 1350, 'Library Visitors': 890, 'Average Borrowing Time (days)': 15},
    {'Month': 'May', 'Total Books Borrowed': 1450, 'Library Visitors': 900, 'Average Borrowing Time (days)': 18},
    {'Month': 'June', 'Total Books Borrowed': 1550, 'Library Visitors': 950, 'Average Borrowing Time (days)': 20},
    {'Month': 'July', 'Total Books Borrowed': 1600, 'Library Visitors': 970, 'Average Borrowing Time (days)': 19},
    {'Month': 'August', 'Total Books Borrowed': 1650, 'Library Visitors': 980, 'Average Borrowing Time (days)': 17}
]
df = pd.DataFrame(data)

# Map month names to numbers for better plotting on the x-axis
month_to_num = {month: index for index, month in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'], start=1)}
df['Month_Num'] = df['Month'].map(month_to_num)

# Use Seaborn's scatterplot function to create a bubble chart
plt.figure(figsize=(10, 6))
bubble_chart = sns.scatterplot(
    data=df,
    x='Month_Num',
    y='Library Visitors',
    size='Total Books Borrowed',
    hue='Average Borrowing Time (days)',
    sizes=(100, 1000),  # Range of bubble sizes
    alpha=0.7,  # Transparency of bubbles
    palette='viridis'  # Color palette for different 'Average Borrowing Time (days)'
)

# Adjust legend to not overlap the bubbles
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# Adding customizations to the plot
bubble_chart.set_xticks(range(1, 9))  # Set x-axis ticks to match the number of months
bubble_chart.set_xticklabels(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'])
plt.title('Library Data Bubble Chart')
plt.xlabel('Month')
plt.ylabel('Library Visitors')

# Show the plot
plt.show()