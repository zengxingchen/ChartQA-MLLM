
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a dataframe from the chart data
data = [
    {'Year': 2019, 'Proteins (%)': 30, 'Carbohydrates (%)': 40, 'Fats (%)': 20, 'Vitamins & Minerals (%)': 10},
    {'Year': 2020, 'Proteins (%)': 32, 'Carbohydrates (%)': 38, 'Fats (%)': 18, 'Vitamins & Minerals (%)': 12},
    {'Year': 2021, 'Proteins (%)': 35, 'Carbohydrates (%)': 35, 'Fats (%)': 20, 'Vitamins & Minerals (%)': 10},
    {'Year': 2022, 'Proteins (%)': 33, 'Carbohydrates (%)': 37, 'Fats (%)': 22, 'Vitamins & Minerals (%)': 8}
]
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert the dataframe to a 100% stacked format
df_percent = df.div(df.sum(axis=1), axis=0)

# Plot the 100% stacked bar chart
ax = df_percent.plot(kind='bar', stacked=True, color=['#3498db', '#2ecc71', '#e74c3c', '#f1c40f'], figsize=(8, 6), width=0.7)

# Customizing the plot to make it more informative
plt.title('Nutrient Distribution in Balanced Diet Over Years (Percentage Stacked)', pad=20)
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
plt.legend(title='Nutrient Sources', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()