
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data = [
    {'Date': '2023-03-01', 'Steps': 7500},
    {'Date': '2023-03-02', 'Steps': 5300},
    {'Date': '2023-03-03', 'Steps': 9200},
    {'Date': '2023-03-04', 'Steps': 11000},
    {'Date': '2023-03-05', 'Steps': 6400}
]

# Convert the given data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert the "Date" column to datetime format for proper plotting
df['Date'] = pd.to_datetime(df['Date'])

# Sort dataframe by date just in case they are out of order
df = df.sort_values('Date')

# Set the style of the seaborn chart
sns.set_theme(style="whitegrid")

# Create a lineplot with seaborn
lineplot = sns.lineplot(data=df, x='Date', y='Steps')

# Fill the area under the lineplot with a color
plt.fill_between(df['Date'], df['Steps'], color="skyblue", alpha=0.4)

# Add a title to the chart
plt.title('Daily Steps Over Time')

# Enhance x and y axis labels
plt.xlabel('Date')
plt.ylabel('Steps')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Remove left spine for aesthetics
sns.despine(left=True)

# Show the plot
plt.show()