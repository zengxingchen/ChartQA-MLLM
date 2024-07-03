
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Your data in a structured form
data = [{'Age Group': '0-12', 'Visitors Last Week': 150, 'Visitors This Week': 170, 'Change (%)': 13.3},
        {'Age Group': '13-18', 'Visitors Last Week': 200, 'Visitors This Week': 190, 'Change (%)': -5.0},
        {'Age Group': '19-24', 'Visitors Last Week': 250, 'Visitors This Week': 230, 'Change (%)': -8.0},
        {'Age Group': '25-34', 'Visitors Last Week': 300, 'Visitors This Week': 310, 'Change (%)': 3.3},
        {'Age Group': '35-44', 'Visitors Last Week': 280, 'Visitors This Week': 285, 'Change (%)': 1.8},
        {'Age Group': '45-54', 'Visitors Last Week': 220, 'Visitors This Week': 215, 'Change (%)': -2.3},
        {'Age Group': '55+', 'Visitors Last Week': 190, 'Visitors This Week': 200, 'Change (%)': 5.3}]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to make it suitable for sns.barplot
df_melted = df.melt(id_vars=['Age Group', 'Change (%)'], 
                    value_vars=['Visitors Last Week', 'Visitors This Week'],
                    var_name='Time Period', value_name='Number of Visitors')

# Set the style and color palette for the plot
sns.set(style="whitegrid")
color_palette = ["#4c72b0", "#55a868"]

# Create the barplot
plt.figure(figsize=(10, 6))
barplot = sns.barplot(x='Age Group', y='Number of Visitors', hue='Time Period', 
                      data=df_melted, palette=color_palette)

# Annotate the percentage change on top of the bars
for index, row in df.iterrows():
    barplot.text(index-0.2, row['Visitors Last Week'] + 3, f"{row['Change (%)']}%", 
                 color='black', ha="center", size=9)
    barplot.text(index+0.2, row['Visitors This Week'] + 3, f"{row['Change (%)']}%", 
                 color='black', ha="center", size=9)

# Customize the plot with labels and title
plt.xlabel('Age Group')
plt.ylabel('Number of Visitors')
plt.title('Visitors Comparison by Age Group')
plt.legend(title='Time Period')

# Show the plot
plt.tight_layout()
plt.show()