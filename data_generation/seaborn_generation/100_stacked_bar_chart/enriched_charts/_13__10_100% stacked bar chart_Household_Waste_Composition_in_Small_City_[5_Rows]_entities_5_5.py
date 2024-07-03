
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your provided data
data = [
    {'Year': 2019, 'Running': '30%', 'Swimming': '20%', 'Cycling': '25%', 'Yoga': '15%', 'Weightlifting': '10%'},
    {'Year': 2020, 'Running': '32%', 'Swimming': '18%', 'Cycling': '23%', 'Yoga': '16%', 'Weightlifting': '11%'},
    {'Year': 2021, 'Running': '29%', 'Swimming': '21%', 'Cycling': '26%', 'Yoga': '14%', 'Weightlifting': '10%'},
    {'Year': 2022, 'Running': '31%', 'Swimming': '19%', 'Cycling': '24%', 'Yoga': '15%', 'Weightlifting': '11%'},
    {'Year': 2023, 'Running': '33%', 'Swimming': '17%', 'Cycling': '22%', 'Yoga': '16%', 'Weightlifting': '12%'}
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
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

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
plt.title('Percentage of Time Spent on Different Activities Over Years')
plt.ylabel('Percentage (%)')
plt.xlabel('Year')

# Move the legend outside the plot
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()