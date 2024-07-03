
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Week': '2023-03-01', 'Price per Pound ($)': 7.5},
    {'Week': '2023-03-08', 'Price per Pound ($)': 7.75},
    {'Week': '2023-03-15', 'Price per Pound ($)': 7.6},
    {'Week': '2023-03-22', 'Price per Pound ($)': 8.0},
    {'Week': '2023-03-29', 'Price per Pound ($)': 8.25},
    {'Week': '2023-04-05', 'Price per Pound ($)': 8.5},
    {'Week': '2023-04-12', 'Price per Pound ($)': 8.75}
]

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'Week' column to datetime for proper plotting
df['Week'] = pd.to_datetime(df['Week'])

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 6))

# Plot filled area under the Price per Pound using 'fill_between'
ax.fill_between(x=df['Week'], y1=df['Price per Pound ($)'], alpha=0.3)

# Additional visual encoding
sns.lineplot(x=df['Week'], y=df['Price per Pound ($)'], sort=False, linewidth=2.5, color='navy')

# Beautifying the plot
ax.set(xlim=(df['Week'].min(), df['Week'].max()), ylim=(df['Price per Pound ($)'].min(), df['Price per Pound ($)'].max()))
ax.xaxis.label.set_visible(False)  # Hide the X-axis label
ax.yaxis.label.set_visible(False)  # Hide the Y-axis label
sns.despine(left=True, bottom=True)  # Remove the top and right spines
plt.xticks(rotation=45)  # Rotate X-axis labels for better readability
plt.title('Price per Pound Over Time')  # Title of the chart
plt.tight_layout()  # Fit the layout tightly to the plot area

# Show the plot
plt.show()