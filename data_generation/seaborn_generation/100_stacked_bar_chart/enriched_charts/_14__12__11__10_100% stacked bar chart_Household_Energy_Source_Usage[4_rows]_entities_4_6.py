
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a dataframe from the chart data
data = [
    {'Year': 2019, 'Science & Nature (%)': 25, 'Arts & Design (%)': 35, 'Sports & Fitness (%)': 25, 'Technology & Society (%)': 15},
    {'Year': 2020, 'Science & Nature (%)': 28, 'Arts & Design (%)': 32, 'Sports & Fitness (%)': 27, 'Technology & Society (%)': 13},
    {'Year': 2021, 'Science & Nature (%)': 30, 'Arts & Design (%)': 30, 'Sports & Fitness (%)': 25, 'Technology & Society (%)': 15},
    {'Year': 2022, 'Science & Nature (%)': 27, 'Arts & Design (%)': 33, 'Sports & Fitness (%)': 26, 'Technology & Society (%)': 14},
    {'Year': 2023, 'Science & Nature (%)': 29, 'Arts & Design (%)': 31, 'Sports & Fitness (%)': 28, 'Technology & Society (%)': 12}
]
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert the dataframe to a 100% stacked format
df_percent = df.div(df.sum(axis=1), axis=0)

# Plot the 100% stacked bar chart
ax = df_percent.plot(kind='bar', stacked=True, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], figsize=(10, 7), width=0.8)

# Customizing the plot to make it more informative
plt.title('Interests in Different Fields Over Years (Percentage Stacked)', pad=20)
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
plt.legend(title='Fields of Interest', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()