
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given chart table data
data = [
    {'Business Name': 'Local Grocers Co-op', 'Year Established': 2008, 'Market Value (Million USD)': 12, 'Employee Count': 47},
    {'Business Name': 'Green Energy Solutions', 'Year Established': 2011, 'Market Value (Million USD)': 25, 'Employee Count': 75},
    {'Business Name': 'City Booksellers Collective', 'Year Established': 1999, 'Market Value (Million USD)': 5, 'Employee Count': 24},
    {'Business Name': 'Urban Farming Association', 'Year Established': 2015, 'Market Value (Million USD)': 8, 'Employee Count': 33},
    {'Business Name': 'Community Health Clinic', 'Year Established': 2003, 'Market Value (Million USD)': 18, 'Employee Count': 40}
]

# Convert the chart data to a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(10, 6))

# Create the seaborn bubble chart
splot = sns.scatterplot(data=df,
                        x='Market Value (Million USD)',
                        y='Year Established',
                        size='Employee Count',
                        sizes=(100, 2000),  # you can adjust the range for the size of the bubbles
                        hue='Business Name',  # color by business name
                        legend=False,  # turn off legend when detailed individual labeling is necessary
                        palette='viridis')  # using the viridis color palette

# Adjust more aesthetics
plt.title('Market Value vs Year Established with Employee Count as Bubble Size')
plt.xlabel('Market Value (Million USD)')
plt.ylabel('Year Established')

# Label each bubble with the business name
for line in range(0, df.shape[0]):
    splot.text(df['Market Value (Million USD)'][line] + 0.2, df['Year Established'][line], 
               df['Business Name'][line], horizontalalignment='left', 
               size='medium', color='black', weight='semibold')

# Show the plot
plt.show()