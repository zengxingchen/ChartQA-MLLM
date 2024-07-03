
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Provided data
data = [
    {'Year': 2019, 'Math': '25%', 'Science': '20%', 'History': '15%', 'Art': '30%', 'Language': '10%'},
    {'Year': 2020, 'Math': '23%', 'Science': '22%', 'History': '18%', 'Art': '27%', 'Language': '10%'},
    {'Year': 2021, 'Math': '20%', 'Science': '25%', 'History': '20%', 'Art': '25%', 'Language': '10%'},
    {'Year': 2022, 'Math': '22%', 'Science': '23%', 'History': '19%', 'Art': '26%', 'Language': '10%'},
    {'Year': 2023, 'Math': '21%', 'Science': '24%', 'History': '21%', 'Art': '24%', 'Language': '10%'}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert percentage strings to numbers
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

# Reshape the DataFrame from wide to long format
df_long = df.melt(id_vars='Year', var_name='Subject', value_name='Percentage')

# Calculate the bottom position for each bar segment
df_long['Bottom'] = df_long.groupby('Year')['Percentage'].cumsum() - df_long['Percentage']

# Begin plotting
plt.figure(figsize=(14, 8))

# Create a color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot each field
for i, subject in enumerate(df.columns[1:]):
    sns.barplot(
        data=df_long[df_long['Subject'] == subject],
        x='Year',
        y='Percentage',
        color=colors[i],
        label=subject,
        bottom=df_long[df_long['Subject'] == subject]['Bottom'],
        ci=None
    )

# Additional plot formatting
plt.title('Distribution of Subjects Over Years in Education', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)

# Move the legend outside the plot
plt.legend(title='Subject', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()