
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data you provided
data = [
    {'Week': '2023-W10', ' Average Steps': 7000},
    {'Week': '2023-W11', ' Average Steps': 7500},
    {'Week': '2023-W12', ' Average Steps': 7200},
    {'Week': '2023-W13', ' Average Steps': 8000},
    {'Week': '2023-W14', ' Average Steps': 8200},
    {'Week': '2023-W15', ' Average Steps': 7800},
    {'Week': '2023-W16', ' Average Steps': 7900},
    {'Week': '2023-W17', ' Average Steps': 8100}
]

# Turn data into a pandas DataFrame
df = pd.DataFrame(data)

# Format 'Week' column to proper datetime format for easy plotting
df['Week'] = pd.to_datetime(df['Week'] + "0", format='%G-W%V%w')

# Set seaborn style
sns.set_theme(style="whitegrid")

# Initialize the matplotlib figure 
f, ax = plt.subplots(figsize=(10, 6))

# Plotting the line
sns.lineplot(data=df, x='Week', y=' Average Steps', ax=ax, color="skyblue", lw=3)

# Filling the area underneath the line
plt.fill_between(x=df['Week'], y1=df[' Average Steps'], color="skyblue", alpha=0.3)

# Customizing titles and labels
ax.set_title('Average Steps by Week')
ax.set_xlabel('Week')
ax.set_ylabel('Average Steps')

# Formatting x-axis to show dates in a nicer format
plt.xticks(rotation=45)
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))

# Show the plot
plt.tight_layout()
plt.show()