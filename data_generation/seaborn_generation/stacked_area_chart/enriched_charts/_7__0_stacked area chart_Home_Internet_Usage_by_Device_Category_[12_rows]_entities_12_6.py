
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Define the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Location A': [110, 130, 145, 135, 160, 175, 190, 210, 205, 220, 230, 240],
    'Location B': [140, 135, 160, 170, 180, 190, 200, 220, 215, 230, 240, 250],
    'Location C': [210, 220, 230, 240, 250, 265, 280, 295, 290, 310, 320, 330]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data preparation for stacked area chart
df_melted = df.melt('Month', var_name='Location', value_name='Visitors')

# Transformation of 'Month' to categorical type for proper ordering
df_melted['Month'] = pd.Categorical(df_melted['Month'],
                                    categories=data['Month'],
                                    ordered=True)

# Plotting
plt.figure(figsize=(14, 8))

# Location A: #FF5733 (Red Orange), Location B: #33FF57 (Green), Location C: #3357FF (Blue)
colors = ["#FF5733", "#33FF57", "#3357FF"]

# Stackplot
plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

# Beautifying the plot
plt.title('Monthly Visitors to Three Travel Locations', fontsize=18, pad=20)
plt.ylabel('Number of Visitors', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Location', loc='upper left', bbox_to_anchor=(1, 1))

# Annotation
for i, row in df.iterrows():
    total_visitors = row['Location A'] + row['Location B'] + row['Location C']
    plt.text(row['Month'], total_visitors, f'{total_visitors}', ha='center', va='bottom')

sns.despine()

# Show the plot
plt.tight_layout()
plt.show()