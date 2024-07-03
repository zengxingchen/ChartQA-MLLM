
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data as a list of dictionaries
data = [
    {'Month': 'January', 'Sales ($ in thousands)': 42},
    {'Month': 'February', 'Sales ($ in thousands)': 38},
    {'Month': 'March', 'Sales ($ in thousands)': 47},
    {'Month': 'April', 'Sales ($ in thousands)': 55},
    {'Month': 'May', 'Sales ($ in thousands)': 62},
    {'Month': 'June', 'Sales ($ in thousands)': 66},
    {'Month': 'July', 'Sales ($ in thousands)': 70},
    {'Month': 'August', 'Sales ($ in thousands)': 73},
    {'Month': 'September', 'Sales ($ in thousands)': 68},
    {'Month': 'October', 'Sales ($ in thousands)': 65},
    {'Month': 'November', 'Sales ($ in thousands)': 58},
    {'Month': 'December', 'Sales ($ in thousands)': 48}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Set the style of the seaborn chart
sns.set(style="whitegrid")

# Create a line plot with `sns.lineplot` which can be filled with `plt.fill_between`
lineplot = sns.lineplot(x='Month', y='Sales ($ in thousands)', data=df, sort=False)

# To create an filled area chart, we use `plt.fill_between` on the axes object
plt.fill_between(x=df['Month'], y1=df['Sales ($ in thousands)'], alpha=0.3)

# Rotating the x-axis labels for better readability
plt.xticks(rotation=45)

# Setting the plot title
plt.title('Monthly Sales Data ($ in thousands)')

# Adjust the plot to make sure everything fits without overlapping
plt.tight_layout()

# Show the plot
plt.show()