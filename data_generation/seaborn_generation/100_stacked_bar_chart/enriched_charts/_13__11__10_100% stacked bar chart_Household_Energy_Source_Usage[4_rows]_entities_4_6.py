
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a dataframe from the chart data
data = [
    {'Year': 2019, 'Restaurants (%)': 40, 'Grocery Stores (%)': 30, 'Online Delivery (%)': 20, 'Catering Services (%)': 10},
    {'Year': 2020, 'Restaurants (%)': 35, 'Grocery Stores (%)': 25, 'Online Delivery (%)': 30, 'Catering Services (%)': 10},
    {'Year': 2021, 'Restaurants (%)': 30, 'Grocery Stores (%)': 20, 'Online Delivery (%)': 35, 'Catering Services (%)': 15},
    {'Year': 2022, 'Restaurants (%)': 25, 'Grocery Stores (%)': 25, 'Online Delivery (%)': 40, 'Catering Services (%)': 10}
]
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert the dataframe to a 100% stacked format
df_percent = df.div(df.sum(axis=1), axis=0)

# Plot the 100% stacked bar chart
ax = df_percent.plot(kind='bar', stacked=True, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], figsize=(8, 12), width=0.5)

# Customizing the plot to make it more informative
plt.title('Revenue Distribution in Food Industry Over Years (Percentage Stacked)', pad=20)
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