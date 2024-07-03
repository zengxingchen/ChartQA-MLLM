
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a dataframe from the chart data
data = [
    {'Year': 2019, 'Advertising (%)': 25, 'Sponsorship (%)': 30, 'Merchandising (%)': 20, 'Broadcast Rights (%)': 25},
    {'Year': 2020, 'Advertising (%)': 28, 'Sponsorship (%)': 25, 'Merchandising (%)': 22, 'Broadcast Rights (%)': 25},
    {'Year': 2021, 'Advertising (%)': 30, 'Sponsorship (%)': 20, 'Merchandising (%)': 25, 'Broadcast Rights (%)': 25},
    {'Year': 2022, 'Advertising (%)': 32, 'Sponsorship (%)': 18, 'Merchandising (%)': 28, 'Broadcast Rights (%)': 22}
]
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert the dataframe to a 100% stacked format
df_percent = df.div(df.sum(axis=1), axis=0)

# Plot the 100% stacked bar chart
ax = df_percent.plot(kind='bar', stacked=True, color=['#FF5733', '#33FF57', '#3357FF', '#F1C40F'], figsize=(10, 7), width=0.6)

# Customizing the plot to make it more informative
plt.title('Revenue Distribution in Sports Industry Over Years (Percentage Stacked)', pad=20)
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
plt.legend(title='Revenue Streams', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()