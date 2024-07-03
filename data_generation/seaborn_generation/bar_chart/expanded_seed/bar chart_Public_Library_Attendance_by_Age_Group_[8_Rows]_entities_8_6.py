
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data provided
chart_table_data = [
    {'Age Group': '0-12', 'January': 150, 'February': 120, 'March': 180, 'April': 200, 'May': 190, 'June': 210, 'July': 230, 'August': 220},
    {'Age Group': '13-18', 'January': 90, 'February': 80, 'March': 95, 'April': 110, 'May': 100, 'June': 115, 'July': 105, 'August': 100},
    {'Age Group': '19-25', 'January': 120, 'February': 100, 'March': 130, 'April': 140, 'May': 145, 'June': 150, 'July': 160, 'August': 155},
    {'Age Group': '26-35', 'January': 200, 'February': 190, 'March': 210, 'April': 220, 'May': 225, 'June': 230, 'July': 240, 'August': 235},
    {'Age Group': '36-50', 'January': 250, 'February': 240, 'March': 260, 'April': 265, 'May': 270, 'June': 275, 'July': 280, 'August': 275},
    {'Age Group': '51-65', 'January': 180, 'February': 170, 'March': 190, 'April': 195, 'May': 200, 'June': 205, 'July': 210, 'August': 205},
    {'Age Group': '65+', 'January': 140, 'February': 130, 'March': 150, 'April': 155, 'May': 160, 'June': 165, 'July': 170, 'August': 165},
    {'Age Group': 'Unknown', 'January': 10, 'February': 5, 'March': 15, 'April': 20, 'May': 20, 'June': 25, 'July': 30, 'August': 25}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(chart_table_data)

# Melt the DataFrame to have "Months" and "Values" columns
df_melted = df.melt(id_vars='Age Group', var_name='Month', value_name='Value')

# Create a FacetGrid for each Month and plot bar charts
g = sns.FacetGrid(df_melted, col="Month", col_wrap=4, height=4, sharey=False)
g.map(sns.barplot, 'Age Group', 'Value', ci=None, palette='viridis')

# Rotate the x-axis labels for readability
for ax in g.axes.flatten():
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

# Set the title and adjust spacing
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Monthly Figures by Age Group')

# Show the plot
plt.show()