
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'Month': 'January', ' Number of Members': 45},
    {'Month': 'February', ' Number of Members': 47},
    {'Month': 'March', ' Number of Members': 50},
    {'Month': 'April', ' Number of Members': 55},
    {'Month': 'May', ' Number of Members': 60},
    {'Month': 'June', ' Number of Members': 65},
    {'Month': 'July', ' Number of Members': 70}
]

# Convert the raw data to a pandas DataFrame
df = pd.DataFrame(data)

# Adjust the column names as seaborn expects no leading/trailing spaces
df.columns = df.columns.str.strip()

# Set the style of seaborn chart
sns.set_style("whitegrid")

# Create a line chart
plt.figure(figsize=(10, 6))   # Set the figure size
line_chart = sns.lineplot(x='Month', y='Number of Members', data=df, marker='o')

# Customizing the plot to make it more readable
plt.title('Monthly Number of Members', fontsize=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Members', fontsize=14)
plt.xticks(rotation=45)       # Rotate x-axis labels to make them readable
plt.tight_layout()            # Adjust the plot to make sure everything fits without overlapping

# Show the plot
plt.show()