
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Provided data
data = [
    {'Year': 2019, 'Aerobic': '40%', 'Strength': '25%', 'Flexibility': '15%', 'Balance': '10%', 'Mindfulness': '10%'},
    {'Year': 2020, 'Aerobic': '42%', 'Strength': '20%', 'Flexibility': '18%', 'Balance': '10%', 'Mindfulness': '10%'},
    {'Year': 2021, 'Aerobic': '45%', 'Strength': '20%', 'Flexibility': '15%', 'Balance': '10%', 'Mindfulness': '10%'},
    {'Year': 2022, 'Aerobic': '43%', 'Strength': '22%', 'Flexibility': '15%', 'Balance': '10%', 'Mindfulness': '10%'},
    {'Year': 2023, 'Aerobic': '50%', 'Strength': '20%', 'Flexibility': '10%', 'Balance': '10%', 'Mindfulness': '10%'}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert percentage strings to numbers
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

# Reshape the DataFrame from wide to long format
df_long = df.melt(id_vars='Year', var_name='Activity', value_name='Percentage')

# Calculate the bottom position for each bar segment
df_long['Bottom'] = df_long.groupby('Year')['Percentage'].cumsum() - df_long['Percentage']

# Begin plotting
plt.figure(figsize=(10, 6))

# Create a color palette
colors = ['#FFA07A', '#20B2AA', '#778899', '#FF6347', '#6A5ACD']

# Plot each activity
for i, activity in enumerate(df.columns[1:]):
    sns.barplot(
        data=df_long[df_long['Activity'] == activity],
        x='Year',
        y='Percentage',
        color=colors[i],
        label=activity,
        bottom=df_long[df_long['Activity'] == activity]['Bottom'],
        width=0.6
    )

# Additional plot formatting
plt.title('Distribution of Physical Activities Over Years', fontsize=16)
plt.ylabel('Percentage (%)', fontsize=12)
plt.xlabel('Year', fontsize=12)

# Move the legend outside the plot
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()