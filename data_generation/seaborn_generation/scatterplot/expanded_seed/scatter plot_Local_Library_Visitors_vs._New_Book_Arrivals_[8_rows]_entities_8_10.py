
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your chart table data
data = [
    {'Week': '1st week of Jan', 'Visitors': 350, 'New Book Arrivals': 20},
    {'Week': '2nd week of Jan', 'Visitors': 270, 'New Book Arrivals': 15},
    {'Week': '3rd week of Jan', 'Visitors': 390, 'New Book Arrivals': 25},
    {'Week': '4th week of Jan', 'Visitors': 415, 'New Book Arrivals': 18},
    {'Week': '1st week of Feb', 'Visitors': 320, 'New Book Arrivals': 12},
    {'Week': '2nd week of Feb', 'Visitors': 280, 'New Book Arrivals': 30},
    {'Week': '3rd week of Feb', 'Visitors': 360, 'New Book Arrivals': 22},
    {'Week': '4th week of Feb', 'Visitors': 475, 'New Book Arrivals': 27}
]

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Convert the 'Week' column into a categorical type so they can be colour-encoded
df['Week'] = pd.Categorical(df['Week'], categories=[
    '1st week of Jan', '2nd week of Jan', '3rd week of Jan', '4th week of Jan',
    '1st week of Feb', '2nd week of Feb', '3rd week of Feb', '4th week of Feb'
])

# Create a scatterplot
plt.figure(figsize=(10, 6))
scatterplot = sns.scatterplot(
    x='Week', 
    y='Visitors',
    data=df,
    size='New Book Arrivals',  # Size of each point will represent the 'New Book Arrivals'
    hue='Week',  # Color encoding by 'Week'
    palette='viridis',  # Color palette used
    sizes=(50, 500)  # Control the range of sizes for the 'New Book Arrivals'
)

# Improve the legibility of the plot
plt.xticks(rotation=45)  # Rotate x-axis labels to avoid overlapping
plt.title('Visitors and New Book Arrivals per Week')  # Title of the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # Move the legend outside the plot

# Display the plot
plt.tight_layout()
plt.show()