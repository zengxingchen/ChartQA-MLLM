
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a dataframe from the chart data
data = [
    {'Year': 2019, 'Fiction (%)': 25, 'Non-Fiction (%)': 45, 'Magazines (%)': 20, 'Comics (%)': 10},
    {'Year': 2020, 'Fiction (%)': 30, 'Non-Fiction (%)': 40, 'Magazines (%)': 15, 'Comics (%)': 15},
    {'Year': 2021, 'Fiction (%)': 28, 'Non-Fiction (%)': 42, 'Magazines (%)': 18, 'Comics (%)': 12},
    {'Year': 2022, 'Fiction (%)': 32, 'Non-Fiction (%)': 38, 'Magazines (%)': 22, 'Comics (%)': 8},
    {'Year': 2023, 'Fiction (%)': 35, 'Non-Fiction (%)': 36, 'Magazines (%)': 20, 'Comics (%)': 9}
]
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert the dataframe to a 100% stacked format
df_percent = df.div(df.sum(axis=1), axis=0)

# Plot the 100% stacked bar chart
ax = df_percent.plot(kind='bar', stacked=True, color=['#8A2BE2', '#FF4500', '#32CD32', '#FFD700'], figsize=(10, 8), width=0.85)

# Customizing the plot to make it more informative
plt.title('Reading Preferences Over Years (Percentage Stacked)', pad=20)
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
plt.legend(title='Reading Materials', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()