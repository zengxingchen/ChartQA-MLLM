
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a dataframe from the chart data
data = [
    {'Year': 2019, 'Flights (%)': 50, 'Trains (%)': 20, 'Buses (%)': 15, 'Car Rentals (%)': 15},
    {'Year': 2020, 'Flights (%)': 45, 'Trains (%)': 25, 'Buses (%)': 20, 'Car Rentals (%)': 10},
    {'Year': 2021, 'Flights (%)': 40, 'Trains (%)': 30, 'Buses (%)': 20, 'Car Rentals (%)': 10},
    {'Year': 2022, 'Flights (%)': 35, 'Trains (%)': 30, 'Buses (%)': 25, 'Car Rentals (%)': 10},
    {'Year': 2023, 'Flights (%)': 30, 'Trains (%)': 35, 'Buses (%)': 25, 'Car Rentals (%)': 10}
]
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert the dataframe to a 100% stacked format
df_percent = df.div(df.sum(axis=1), axis=0)

# Plot the 100% stacked bar chart
ax = df_percent.plot(kind='bar', stacked=True, color=['#4c72b0', '#55a868', '#c44e52', '#8172b2'], figsize=(10, 8), width=0.6)

# Customizing the plot to make it more informative
plt.title('Travel Preferences Over Years (Percentage Stacked)', pad=20)
plt.xlabel('Year')
plt.ylabel('Percentage %')

# Annotate the percentages on top of the bars
for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy() 
    if height > 0:
        ax.text(x + width / 2, 
                y + height / 2, 
                '{:.0%}'.format(height), 
                horizontalalignment='center', 
                verticalalignment='center')

# Adjust legend
plt.legend(title='Transport Modes', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()