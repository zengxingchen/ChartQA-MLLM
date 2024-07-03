
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Date': '2023-03-01', 'Steps': 7584},
    {'Date': '2023-03-02', 'Steps': 8320},
    {'Date': '2023-03-03', 'Steps': 9921},
    {'Date': '2023-03-04', 'Steps': 12043},
    {'Date': '2023-03-05', 'Steps': 11086}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set the style of the seaborn chart
sns.set_theme(style="darkgrid")

# Create the line plot
plt.figure(figsize=(10, 6))  # Custom figure size
line_plot = sns.lineplot(data=df, x='Date', y='Steps', marker='o', linewidth=2.5)

# Set the title and labels of the plot
plt.title('Daily Steps Trend', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Steps', fontsize=14)

# Optionally, you can format the x-axis to show the date format more clearly
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Highlight each data point on the plot with annotations
for i in range(len(df)):
    plt.text(df.loc[i, 'Date'], df.loc[i, 'Steps'] + 300,  # Position of the text
             f"{df.loc[i, 'Steps']:,}",                 # Format the number with commas
             ha='center')                               # Centrally align the text for neatness

# Tight layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()