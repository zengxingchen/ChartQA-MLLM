
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a dataframe from the chart data
data = [
    {'Year': 2019, 'Fashion Accessories (%)': 35, 'Clothing (%)': 40, 'Footwear (%)': 15, 'Jewelry (%)': 10},
    {'Year': 2020, 'Fashion Accessories (%)': 38, 'Clothing (%)': 37, 'Footwear (%)': 17, 'Jewelry (%)': 8},
    {'Year': 2021, 'Fashion Accessories (%)': 40, 'Clothing (%)': 35, 'Footwear (%)': 18, 'Jewelry (%)': 7},
    {'Year': 2022, 'Fashion Accessories (%)': 42, 'Clothing (%)': 33, 'Footwear (%)': 20, 'Jewelry (%)': 5}
]
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert the dataframe to a 100% stacked format
df_percent = df.div(df.sum(axis=1), axis=0)

# Plot the 100% stacked bar chart
ax = df_percent.plot(kind='bar', stacked=True, color=['#FF5733', '#33FF57', '#3357FF', '#F1C40F'], figsize=(8, 6), width=0.75)

# Customizing the plot to make it more informative
plt.title('Fashion Product Distribution Over Years (Percentage Stacked)', pad=20)
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
plt.legend(title='Fashion Products', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()