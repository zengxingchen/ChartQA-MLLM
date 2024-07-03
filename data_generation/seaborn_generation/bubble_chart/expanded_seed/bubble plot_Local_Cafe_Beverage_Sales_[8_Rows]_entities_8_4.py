
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = [
    {'Month': 'Jan', 'Espresso Sales': 120, 'Cappuccino Sales': 180, 'Latte Sales': 250, 'Hot Chocolate Sales': 90, 'Average Price Per Cup': 2.5, 'Total Sales': 2640},
    {'Month': 'Feb', 'Espresso Sales': 150, 'Cappuccino Sales': 160, 'Latte Sales': 230, 'Hot Chocolate Sales': 110, 'Average Price Per Cup': 2.55, 'Total Sales': 2625},
    {'Month': 'Mar', 'Espresso Sales': 130, 'Cappuccino Sales': 190, 'Latte Sales': 220, 'Hot Chocolate Sales': 95, 'Average Price Per Cup': 2.6, 'Total Sales': 2605},
    {'Month': 'Apr', 'Espresso Sales': 160, 'Cappuccino Sales': 200, 'Latte Sales': 240, 'Hot Chocolate Sales': 100, 'Average Price Per Cup': 2.65, 'Total Sales': 2720},
    {'Month': 'May', 'Espresso Sales': 170, 'Cappuccino Sales': 210, 'Latte Sales': 260, 'Hot Chocolate Sales': 105, 'Average Price Per Cup': 2.7, 'Total Sales': 2860},
    {'Month': 'Jun', 'Espresso Sales': 180, 'Cappuccino Sales': 220, 'Latte Sales': 270, 'Hot Chocolate Sales': 110, 'Average Price Per Cup': 2.75, 'Total Sales': 3020},
    {'Month': 'Jul', 'Espresso Sales': 190, 'Cappuccino Sales': 230, 'Latte Sales': 280, 'Hot Chocolate Sales': 115, 'Average Price Per Cup': 2.8, 'Total Sales': 3195},
    {'Month': 'Aug', 'Espresso Sales': 200, 'Cappuccino Sales': 240, 'Latte Sales': 290, 'Hot Chocolate Sales': 120, 'Average Price Per Cup': 2.85, 'Total Sales': 3360}
]
df = pd.DataFrame(data)

# We need to reshape the dataframe to have 'Type', 'Sales', and 'Month' columns
melted_df = pd.melt(df, id_vars=['Month', 'Average Price Per Cup', 'Total Sales'], value_vars=['Espresso Sales', 'Cappuccino Sales', 'Latte Sales', 'Hot Chocolate Sales'], var_name='Type', value_name='Sales')

# Create a bubble chart
plt.figure(figsize=(10, 8))
bubble_chart = sns.scatterplot(data=melted_df, x='Month', y='Type', size='Average Price Per Cup', hue='Total Sales', sizes=(20, 400), alpha=0.7)

# Customize the axes and legend
bubble_chart.set_title('Sales by Coffee Type and Month')
bubble_chart.set_xlabel('Month')
bubble_chart.set_ylabel('Coffee Type')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
plt.tight_layout()

# Show the plot
plt.show()