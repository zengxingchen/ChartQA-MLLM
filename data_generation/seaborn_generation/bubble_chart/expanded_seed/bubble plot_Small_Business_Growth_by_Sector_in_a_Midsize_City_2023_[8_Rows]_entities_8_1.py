
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data provided in question
data = [
    {'Business Sector': 'Retail', 'Number of New Businesses': 20, 'Average Annual Revenue (Million $)': 1.2, 'Avg. Employees per Business': 15},
    {'Business Sector': 'Hospitality', 'Number of New Businesses': 15, 'Average Annual Revenue (Million $)': 2.0, 'Avg. Employees per Business': 22},
    {'Business Sector': 'IT Services', 'Number of New Businesses': 25, 'Average Annual Revenue (Million $)': 3.5, 'Avg. Employees per Business': 10},
    {'Business Sector': 'Health & Wellness', 'Number of New Businesses': 18, 'Average Annual Revenue (Million $)': 1.0, 'Avg. Employees per Business': 8},
    {'Business Sector': 'Education', 'Number of New Businesses': 10, 'Average Annual Revenue (Million $)': 1.5, 'Avg. Employees per Business': 18},
    {'Business Sector': 'Food Services', 'Number of New Businesses': 22, 'Average Annual Revenue (Million $)': 0.8, 'Avg. Employees per Business': 12},
    {'Business Sector': 'Real Estate', 'Number of New Businesses': 13, 'Average Annual Revenue (Million $)': 3.8, 'Avg. Employees per Business': 7},
    {'Business Sector': 'Entertainment', 'Number of New Businesses': 8, 'Average Annual Revenue (Million $)': 2.1, 'Avg. Employees per Business': 25}
]

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(10, 8))
bubble_chart = sns.scatterplot(
    data=df,
    x='Average Annual Revenue (Million $)',
    y='Number of New Businesses',
    size='Avg. Employees per Business',
    hue='Business Sector',
    sizes=(100, 1000),  # Control the range of bubble sizes
    legend='full',  # Display legend
    palette='viridis'  # Color palette for different sectors
)

# Improve the readability of the plot
plt.title('Bubble Chart of New Businesses')
plt.xlabel('Average Annual Revenue (Million $)')
plt.ylabel('Number of New Businesses')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # Place the legend outside the plot

# Display the plot
plt.show()