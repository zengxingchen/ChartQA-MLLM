
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Provided data
data = [
    {'Year': 2019, 'Streaming': '35%', 'Reading': '20%', 'Traveling': '15%', 'Music': '10%', 'Movies': '20%'},
    {'Year': 2020, 'Streaming': '40%', 'Reading': '25%', 'Traveling': '10%', 'Music': '15%', 'Movies': '10%'},
    {'Year': 2021, 'Streaming': '50%', 'Reading': '20%', 'Traveling': '10%', 'Music': '10%', 'Movies': '10%'},
    {'Year': 2022, 'Streaming': '45%', 'Reading': '20%', 'Traveling': '15%', 'Music': '10%', 'Movies': '10%'},
    {'Year': 2023, 'Streaming': '50%', 'Reading': '25%', 'Traveling': '5%', 'Music': '10%', 'Movies': '10%'}
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
plt.figure(figsize=(12, 8))

# Create a color palette
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFBD33']

# Plot each activity
for i, activity in enumerate(df.columns[1:]):
    sns.barplot(
        data=df_long[df_long['Activity'] == activity],
        x='Year',
        y='Percentage',
        color=colors[i],
        label=activity,
        bottom=df_long[df_long['Activity'] == activity]['Bottom'],
        width=0.8
    )

# Additional plot formatting
plt.title('Entertainment Activities Over the Years', fontsize=18)
plt.ylabel('Percentage (%)', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Move the legend outside the plot
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()