
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data = [
    {'Month': 'January', 'Average Screen Time (Hours)': 3.5},
    {'Month': 'February', 'Average Screen Time (Hours)': 3.6},
    {'Month': 'March', 'Average Screen Time (Hours)': 3.8},
    {'Month': 'April', 'Average Screen Time (Hours)': 4.0},
    {'Month': 'May', 'Average Screen Time (Hours)': 4.1},
    {'Month': 'June', 'Average Screen Time (Hours)': 3.9},
    {'Month': 'July', 'Average Screen Time (Hours)': 4.3},
    {'Month': 'August', 'Average Screen Time (Hours)': 4.2},
    {'Month': 'September', 'Average Screen Time (Hours)': 3.8},
    {'Month': 'October', 'Average Screen Time (Hours)': 3.7},
    {'Month': 'November', 'Average Screen Time (Hours)': 3.6},
    {'Month': 'December', 'Average Screen Time (Hours)': 3.9}
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Converting 'Month' to a categorical data type ordering by calendar months
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
], ordered=True)

# Create a lineplot and use fill_between to create the area chart effect
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
lineplot = sns.lineplot(data=df, x='Month', y='Average Screen Time (Hours)', sort=False, marker='o')
plt.fill_between(df['Month'], df['Average Screen Time (Hours)'], alpha=0.3)

# Additional customizations for a more engaging chart
plt.title('Average Screen Time by Month', fontsize=16)
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.ylabel('Hours')
plt.ylim(0, df['Average Screen Time (Hours)'].max() + 0.5)
sns.despine()  # Remove the top and right spines

# Show the plot
plt.show()