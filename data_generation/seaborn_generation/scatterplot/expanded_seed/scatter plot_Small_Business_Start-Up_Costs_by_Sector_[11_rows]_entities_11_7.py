
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Sector': 'Retail', 'Initial Investment (Thousands)': 75, 'Yearly Operating Costs (Thousands)': 120, 'Break Even Point (Years)': 2},
    {'Sector': 'Restaurant', 'Initial Investment (Thousands)': 60, 'Yearly Operating Costs (Thousands)': 150, 'Break Even Point (Years)': 3},
    {'Sector': 'Tech Start-up', 'Initial Investment (Thousands)': 150, 'Yearly Operating Costs (Thousands)': 200, 'Break Even Point (Years)': 4},
    {'Sector': 'Agriculture', 'Initial Investment (Thousands)': 30, 'Yearly Operating Costs (Thousands)': 50, 'Break Even Point (Years)': 2},
    {'Sector': 'Real Estate', 'Initial Investment (Thousands)': 200, 'Yearly Operating Costs (Thousands)': 80, 'Break Even Point (Years)': 5},
    {'Sector': 'Healthcare', 'Initial Investment (Thousands)': 100, 'Yearly Operating Costs (Thousands)': 150, 'Break Even Point (Years)': 3},
    {'Sector': 'Beauty & Wellness', 'Initial Investment (Thousands)': 20, 'Yearly Operating Costs (Thousands)': 40, 'Break Even Point (Years)': 1},
    {'Sector': 'Consulting', 'Initial Investment (Thousands)': 10, 'Yearly Operating Costs (Thousands)': 30, 'Break Even Point (Years)': 1},
    {'Sector': 'Craftsmanship', 'Initial Investment (Thousands)': 15, 'Yearly Operating Costs (Thousands)': 25, 'Break Even Point (Years)': 2},
    {'Sector': 'Education', 'Initial Investment (Thousands)': 50, 'Yearly Operating Costs (Thousands)': 60, 'Break Even Point (Years)': 3},
    {'Sector': 'Sports & Recreation', 'Initial Investment (Thousands)': 40, 'Yearly Operating Costs (Thousands)': 80, 'Break Even Point (Years)': 2}
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Create a scatterplot
plt.figure(figsize=(12, 8))
scatterplot = sns.scatterplot(
    data=df,
    x='Initial Investment (Thousands)',
    y='Yearly Operating Costs (Thousands)',
    size='Break Even Point (Years)', # Size encodes the break-even point
    hue='Sector', # Color encodes the sector
    sizes=(50, 500), # Size range for scaling point sizes
    legend='full', # Full legend for sizes and hues
    palette='deep' # Color palette to use
)

# Customizing the plot further
scatterplot.set_title('Sector-wise Scatterplot on Initial Investment vs. Yearly Operating Costs')
scatterplot.set_xlabel('Initial Investment (Thousands)')
scatterplot.set_ylabel('Yearly Operating Costs (Thousands)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') # Shift the legend to the right side of the plot
plt.grid(True) # Adding a grid for better readability
plt.show()