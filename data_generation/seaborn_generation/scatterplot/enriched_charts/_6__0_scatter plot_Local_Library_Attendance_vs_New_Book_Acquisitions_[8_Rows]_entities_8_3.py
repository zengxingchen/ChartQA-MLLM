
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Constructing DataFrame from the table data.
data = {
    'City': ['London', 'Paris', 'Rome', 'Berlin', 'Madrid', 'Amsterdam', 'Prague', 
             'Vienna', 'Venice', 'Barcelona', 'Lisbon', 'Athens',
             'Dublin', 'Oslo', 'Stockholm', 'Helsinki', 'Copenhagen', 
             'Budapest', 'Warsaw', 'Istanbul'],
    'BookSales': [1200, 1100, 950, 850, 1020, 900, 800, 880, 870, 950, 
                  780, 920, 700, 680, 750, 650, 800, 720, 730, 950],
    'LibraryVisits': [3200, 2900, 2500, 2200, 2600, 2300, 2000, 2150, 2100, 
                      2400, 1950, 2450, 1800, 1750, 1900, 1600,
                      2100, 1850, 1900, 2550]
}

df = pd.DataFrame(data)

# Create a scatterplot.
plt.figure(figsize=(14, 10))
sns.scatterplot(data=df, x='BookSales', y='LibraryVisits', 
                palette=['#FFA07A', '#20B2AA'], 
                s=150)  # s is the marker size

# Add chart title and labels
plt.title('Relationship between Book Sales and Library Visits in European Cities', fontsize=18)
plt.xlabel('Book Sales (Units)', fontsize=14)
plt.ylabel('Number of Library Visits', fontsize=14)

# Show the plot
plt.show()