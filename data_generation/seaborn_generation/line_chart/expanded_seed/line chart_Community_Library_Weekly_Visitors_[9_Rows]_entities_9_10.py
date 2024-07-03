
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame from the provided data
data = [
    {'Week': '2023-01-W1', 'Adults': 320, 'Children': 210, 'Total Books Borrowed': 650},
    {'Week': '2023-01-W2', 'Adults': 290, 'Children': 190, 'Total Books Borrowed': 550},
    {'Week': '2023-01-W3', 'Adults': 350, 'Children': 230, 'Total Books Borrowed': 700},
    {'Week': '2023-01-W4', 'Adults': 310, 'Children': 220, 'Total Books Borrowed': 650},
    {'Week': '2023-02-W1', 'Adults': 330, 'Children': 250, 'Total Books Borrowed': 680},
    {'Week': '2023-02-W2', 'Adults': 340, 'Children': 240, 'Total Books Borrowed': 720},
    {'Week': '2023-02-W3', 'Adults': 300, 'Children': 200, 'Total Books Borrowed': 600},
    {'Week': '2023-02-W4', 'Adults': 320, 'Children': 210, 'Total Books Borrowed': 640},
    {'Week': '2023-03-W1', 'Adults': 350, 'Children': 260, 'Total Books Borrowed': 750}
]
df = pd.DataFrame(data)

# Convert the 'Week' column to datetime to help with plotting
df['Week'] = pd.to_datetime(df['Week'].str.replace('W','-').str.replace('(\\d$)', r'0\1'))

# Melt the DataFrame to have "categories" for Adults and Children
df_melted = df.melt(id_vars='Week', value_vars=['Adults', 'Children'], var_name='Category', value_name='BooksBorrowed')

# Set the style 
sns.set_theme(style="whitegrid")

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the data
lineplot = sns.lineplot(data=df_melted, x='Week', y='BooksBorrowed', hue='Category', style='Category', markers=True, dashes=False, ax=ax)

# Customize the plot with titles and labels
plt.title('Books Borrowed by Adults and Children Over Weeks')
plt.xlabel('Week')
plt.ylabel('Number of Books Borrowed')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Place the legend
plt.legend(title='Category', loc='upper left')

# Show the plot
plt.show()