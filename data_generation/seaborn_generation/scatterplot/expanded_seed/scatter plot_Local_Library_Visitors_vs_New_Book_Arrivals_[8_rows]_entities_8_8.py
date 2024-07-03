
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Transforming your chart table data into a pandas DataFrame
data = [
    {'Month': 'January', 'Number of Visitors': 340, 'New Books Arrived': 30},
    {'Month': 'February', 'Number of Visitors': 280, 'New Books Arrived': 25},
    {'Month': 'March', 'Number of Visitors': 360, 'New Books Arrived': 42},
    {'Month': 'April', 'Number of Visitors': 390, 'New Books Arrived': 35},
    {'Month': 'May', 'Number of Visitors': 420, 'New Books Arrived': 20},
    {'Month': 'June', 'Number of Visitors': 370, 'New Books Arrived': 38},
    {'Month': 'July', 'Number of Visitors': 480, 'New Books Arrived': 50},
    {'Month': 'August', 'Number of Visitors': 520, 'New Books Arrived': 45}
]
df = pd.DataFrame(data)

# Map the 'Month' to a numerical value for plotting purposes
month_mapping = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8
}
df['Month_Num'] = df['Month'].map(month_mapping)

# Create a scatterplot using seaborn with diversified visual encodings
plt.figure(figsize=(10, 6))
scatterplot = sns.scatterplot(
    data=df,
    x='Month_Num', # Numerical representation of the month for the x-axis
    y='Number of Visitors', # Number of Visitors for the y-axis
    size='New Books Arrived', # The size of each point to represent the number of new books
    hue='Month', # Color points by Month for readability
    palette='deep', # Use a deep color palette
    sizes=(100, 400), # Control the range of sizes for 'New Books Arrived'
    legend='full' # Show the legend fully to explain markers
)

# Customize the tick labels for the x-axis to show month names
scatterplot.set_xticks(range(1, 9))
scatterplot.set_xticklabels(list(month_mapping.keys()))

# Add titles and labels
plt.title('Library Visitors and New Books Arrived by Month')
plt.xlabel('Month')
plt.ylabel('Number of Visitors')
plt.legend(title='Month / Size: New Books Arrived')

# Show the plot
plt.show()