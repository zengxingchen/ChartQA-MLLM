
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'City': 'Amsterdam', 'Year': 2021, 'Bicycles in Fleet': 50000, 'Number of Trips': 1000000, 'Average Trip Duration (Minutes)': 25},
    {'City': 'Berlin', 'Year': 2021, 'Bicycles in Fleet': 12000, 'Number of Trips': 750000, 'Average Trip Duration (Minutes)': 20},
    {'City': 'Copenhagen', 'Year': 2021, 'Bicycles in Fleet': 20800, 'Number of Trips': 600000, 'Average Trip Duration (Minutes)': 15},
    {'City': 'London', 'Year': 2021, 'Bicycles in Fleet': 13800, 'Number of Trips': 2000000, 'Average Trip Duration (Minutes)': 30},
    {'City': 'New York', 'Year': 2021, 'Bicycles in Fleet': 14500, 'Number of Trips': 1750000, 'Average Trip Duration (Minutes)': 22}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create a bubble chart
plt.figure(figsize=(10, 6))
bubble = sns.scatterplot(data=df, x="Number of Trips", y="Average Trip Duration (Minutes)",
                         size="Bicycles in Fleet", hue="City", sizes=(100, 2000), alpha=0.7, legend='brief')

# Customize the axes and title
plt.xlabel('Number of Trips')
plt.ylabel('Average Trip Duration (Minutes)')
plt.title('Bicycle Usage in Various Cities (2021)')

# Adjust legends
h,l = bubble.get_legend_handles_labels()
plt.legend(h[1:], l[1:], title="City", bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Show the plot
plt.tight_layout()
plt.show()