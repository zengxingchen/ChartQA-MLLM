
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = [
    {'Day': 'Monday', 'Sales ($)': 1200},
    {'Day': 'Tuesday', 'Sales ($)': 1500},
    {'Day': 'Wednesday', 'Sales ($)': 1800},
    {'Day': 'Thursday', 'Sales ($)': 1600},
    {'Day': 'Friday', 'Sales ($)': 2000}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame based on the days of the week so that the plot makes sense
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
df['Day'] = pd.Categorical(df['Day'], categories=weekdays, ordered=True)
df.sort_values('Day', inplace=True)

# Begin plot
sns.set_theme(style="whitegrid")  # Set the theme for Seaborn

# Create the line plot
fig, ax = plt.subplots()
sns.lineplot(x="Day", y="Sales ($)", data=df, ax=ax, marker='o')

# Fill the area under the line
plt.fill_between(x=df['Day'], y1=df['Sales ($)'], color='skyblue', alpha=0.3)

# Customize the axes and the plot
ax.set_title('Sales Throughout the Week')
ax.set_ylabel('Sales ($)')
ax.set_xlabel('Day of the Week')

# Remove the right and top spines (optional, for aesthetics)
sns.despine()

# Show plot
plt.show()