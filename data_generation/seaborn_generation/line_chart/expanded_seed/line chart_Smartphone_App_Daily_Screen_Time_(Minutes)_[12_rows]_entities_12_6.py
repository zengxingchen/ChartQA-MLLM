
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
data = [
    {'Date': '2023-03-11', 'Social Media': 35, 'Games': 25, 'Productivity': 55, 'News': 15},
    {'Date': '2023-03-12', 'Social Media': 40, 'Games': 30, 'Productivity': 60, 'News': 20},
    {'Date': '2023-03-13', 'Social Media': 42, 'Games': 28, 'Productivity': 58, 'News': 18},
    {'Date': '2023-03-14', 'Social Media': 45, 'Games': 25, 'Productivity': 62, 'News': 17},
    {'Date': '2023-03-15', 'Social Media': 50, 'Games': 20, 'Productivity': 65, 'News': 22},
    {'Date': '2023-03-16', 'Social Media': 55, 'Games': 18, 'Productivity': 70, 'News': 20},
    {'Date': '2023-03-17', 'Social Media': 60, 'Games': 15, 'Productivity': 75, 'News': 25},
    {'Date': '2023-03-18', 'Social Media': 62, 'Games': 10, 'Productivity': 80, 'News': 30},
    {'Date': '2023-03-19', 'Social Media': 58, 'Games': 12, 'Productivity': 85, 'News': 32},
    {'Date': '2023-03-20', 'Social Media': 60, 'Games': 14, 'Productivity': 90, 'News': 29},
    {'Date': '2023-03-21', 'Social Media': 63, 'Games': 11, 'Productivity': 88, 'News': 31},
    {'Date': '2023-03-22', 'Social Media': 65, 'Games': 10, 'Productivity': 93, 'News': 33}
]

df = pd.DataFrame(data)

# Convert 'Date' to datetime for proper plotting
df['Date'] = pd.to_datetime(df['Date'])

# Set the style of the plot
sns.set_theme(style="whitegrid")

# Create a figure and a set of subplots
plt.figure(figsize=(10, 6))

# Plot each category as a separate line
sns.lineplot(x='Date', y='Social Media', data=df, marker='o', label='Social Media')
sns.lineplot(x='Date', y='Games', data=df, marker='v', label='Games')
sns.lineplot(x='Date', y='Productivity', data=df, marker='s', label='Productivity')
sns.lineplot(x='Date', y='News', data=df, marker='^', label='News')

# Add some visual improvements
plt.title('Daily Usage of Apps over Time')
plt.xlabel('Date')
plt.ylabel('Usage Time (minutes)')
plt.legend(title='App Categories')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show or save the plot
plt.tight_layout()
plt.show()