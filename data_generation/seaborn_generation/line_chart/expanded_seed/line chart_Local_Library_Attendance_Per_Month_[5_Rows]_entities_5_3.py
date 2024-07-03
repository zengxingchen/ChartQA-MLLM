
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = [{'Month': 'January', 'Visitors': 450},
        {'Month': 'February', 'Visitors': 370},
        {'Month': 'March', 'Visitors': 480},
        {'Month': 'April', 'Visitors': 520},
        {'Month': 'May', 'Visitors': 600}]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Create a line chart with Seaborn
sns.set_theme(style="whitegrid")  # Set the theme for aesthetic purposes

# Define the order of the months for proper plotting
month_order = ['January', 'February', 'March', 'April', 'May']

# Convert 'Month' to a categorical type to ensure it follows the specified order
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

# Create a lineplot
sns.lineplot(data=df, x='Month', y='Visitors', marker='o', linestyle='-', color='b', markersize=8)

# Additional visual enhancements
plt.title('Monthly Visitors')                  # Title of the plot
plt.xlabel('Month')                            # X-axis label
plt.ylabel('Number of Visitors')               # Y-axis label
plt.xticks(rotation=45)                        # Rotate X-axis labels for better readability
plt.tight_layout()                             # Adjust layout to prevent clipping of labels/titles

# Display the plot
plt.show()