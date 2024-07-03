
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Date': '2023-02-01', 'Children (0-12)': 120, 'Teens (13-18)': 80, 'Adults (19-64)': 200, 'Seniors (65+)': 40},
    {'Date': '2023-02-08', 'Children (0-12)': 130, 'Teens (13-18)': 90, 'Adults (19-64)': 190, 'Seniors (65+)': 50},
    {'Date': '2023-02-15', 'Children (0-12)': 110, 'Teens (13-18)': 70, 'Adults (19-64)': 210, 'Seniors (65+)': 60},
    {'Date': '2023-02-22', 'Children (0-12)': 100, 'Teens (13-18)': 65, 'Adults (19-64)': 205, 'Seniors (65+)': 55},
    {'Date': '2023-03-01', 'Children (0-12)': 90, 'Teens (13-18)': 85, 'Adults (19-64)': 220, 'Seniors (65+)': 65},
    {'Date': '2023-03-08', 'Children (0-12)': 140, 'Teens (13-18)': 95, 'Adults (19-64)': 230, 'Seniors (65+)': 70},
    {'Date': '2023-03-15', 'Children (0-12)': 150, 'Teens (13-18)': 100, 'Adults (19-64)': 240, 'Seniors (65+)': 75},
    {'Date': '2023-03-22', 'Children (0-12)': 160, 'Teens (13-18)': 110, 'Adults (19-64)': 250, 'Seniors (65+)': 80},
    {'Date': '2023-03-29', 'Children (0-12)': 170, 'Teens (13-18)': 120, 'Adults (19-64)': 260, 'Seniors (65+)': 85}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Melt the dataframe to long form
df_long = df.melt(id_vars='Date', var_name='Age Group', value_name='Count')

# Convert 'Date' to a datetime type
df_long['Date'] = pd.to_datetime(df_long['Date'])

# Set the style and palette of the plot
sns.set(style="whitegrid")
palette = sns.color_palette("husl", 4)

# Create a lineplot with different markers for each age group
plt.figure(figsize=(10, 6))
lineplot = sns.lineplot(
    x='Date',
    y='Count',
    hue='Age Group',
    style='Age Group',
    markers=True,
    dashes=False,
    data=df_long,
    palette=palette
)

# Customize the plot with titles and labels
plt.title('Attendance by Age Group Over Time')
plt.xlabel('Date')
plt.ylabel('Count')

# Show a legend with no title
plt.legend(title=None)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Tight layout for better spacing
plt.tight_layout()

# Display the plot
plt.show()