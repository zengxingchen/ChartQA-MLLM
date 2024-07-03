
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Date': '2023-04-01', '0-12': 25, '13-18': 30, '19-34': 45, '35-59': 70, '60+': 20},
    {'Date': '2023-04-02', '0-12': 20, '13-18': 25, '19-34': 35, '35-59': 60, '60+': 18},
    {'Date': '2023-04-03', '0-12': 30, '13-18': 40, '19-34': 55, '35-59': 80, '60+': 25},
    {'Date': '2023-04-04', '0-12': 15, '13-18': 20, '19-34': 40, '35-59': 75, '60+': 22},
    {'Date': '2023-04-05', '0-12': 35, '13-18': 45, '19-34': 60, '35-59': 85, '60+': 30},
    {'Date': '2023-04-06', '0-12': 22, '13-18': 35, '19-34': 50, '35-59': 65, '60+': 19},
    {'Date': '2023-04-07', '0-12': 28, '13-18': 33, '19-34': 47, '35-59': 72, '60+': 24},
    {'Date': '2023-04-08', '0-12': 40, '13-18': 50, '19-34': 70, '35-59': 90, '60+': 32}
]

# Convert the data into a pandas DataFrame and melt it into long-form
df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Date', var_name='Age_Group', value_name='Count')

# Convert the 'Date' column to datetime format for better plotting
df_melted['Date'] = pd.to_datetime(df_melted['Date'])

# Set the style and color palette for the plot
sns.set_style('whitegrid')
sns.set_palette('tab10')

# Initialize the figure
plt.figure(figsize=(12, 6))

# Create the line chart using Seaborn's lineplot function
lineplot = sns.lineplot(
    data=df_melted,
    x='Date',
    y='Count',
    hue='Age_Group',
    style='Age_Group',
    markers=True,
    dashes=False
)

# Customize the plot with labels, title, and a legend
plt.title('Counts by Age Group Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend(title='Age Group', loc='upper left', bbox_to_anchor=(1, 1))  # Place legend outside the plot

# Show the plot
plt.tight_layout()
plt.show()