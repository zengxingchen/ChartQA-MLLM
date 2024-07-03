
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a dataframe from your chart data
data = [
    {'Year': 2019, 'Electricity (%)': 44, 'Natural Gas (%)': 30, 'Heating Oil (%)': 10, 'Renewable Sources (%)': 16},
    {'Year': 2020, 'Electricity (%)': 42, 'Natural Gas (%)': 29, 'Heating Oil (%)': 9, 'Renewable Sources (%)': 20},
    {'Year': 2021, 'Electricity (%)': 40, 'Natural Gas (%)': 28, 'Heating Oil (%)': 7, 'Renewable Sources (%)': 25},
    {'Year': 2022, 'Electricity (%)': 38, 'Natural Gas (%)': 27, 'Heating Oil (%)': 5, 'Renewable Sources (%)': 30}
]
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert the dataframe to a 100% stacked format
df_percent = df.div(df.sum(axis=1), axis=0)

# Plot the 100% stacked bar chart
ax = df_percent.plot(kind='bar', stacked=True, colormap='viridis', figsize=(10, 7))

# Customizing the plot to make it more informative
plt.title('Energy Source Distribution Over Years (Percentage Stacked)')
plt.xlabel('Year')
plt.ylabel('Percentage %')

# Annotate the percentages on top of the bars
for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy() 
    if height > 0:
        ax.text(x+width/2, 
                y+height/2, 
                '{:.0%}'.format(height), 
                horizontalalignment='center', 
                verticalalignment='center')

# Adjust legend
plt.legend(title='Energy Sources', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()