
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Platform': 'Facebook', 'Jan Engagements': 2200, 'Feb Engagements': 2100, 'Mar Engagements': 2500, 'Apr Engagements': 2350, 'May Engagements': 2400, 'Jun Engagements': 2700},
    {'Platform': 'Instagram', 'Jan Engagements': 2800, 'Feb Engagements': 2750, 'Mar Engagements': 3000, 'Apr Engagements': 3100, 'May Engagements': 3200, 'Jun Engagements': 3400},
    # ... (Include all other platform data here)
    {'Platform': 'WeChat', 'Jan Engagements': 700, 'Feb Engagements': 750, 'Mar Engagements': 800, 'Apr Engagements': 850, 'May Engagements': 870, 'Jun Engagements': 890}
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to a long format
df_long = df.melt(id_vars='Platform', var_name='Month', value_name='Engagements')

# Customize Seaborn's aesthetics
sns.set(style="whitegrid")

# Create the bar chart using Seaborn
plt.figure(figsize=(18, 8))  # Customize the figure size
chart = sns.barplot(
    x='Platform', 
    y='Engagements', 
    hue='Month', 
    data=df_long,
    palette='viridis' # Using a Seaborn palette for color coding
)

# Customize the chart
chart.set_title('Monthly Engagements per Platform')
chart.set_xlabel('Platform')
chart.set_ylabel('Engagements')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend(title='Month')

# Display the plot
plt.show()