
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Date': '2023-04-01', 'Children (0-12)': 120, 'Teens (13-18)': 60, 'Adults (19-64)': 200, 'Seniors (65+)': 80},
    {'Date': '2023-04-02', 'Children (0-12)': 95, 'Teens (13-18)': 45, 'Adults (19-64)': 150, 'Seniors (65+)': 65},
    {'Date': '2023-04-03', 'Children (0-12)': 130, 'Teens (13-18)': 70, 'Adults (19-64)': 220, 'Seniors (65+)': 90},
    {'Date': '2023-04-04', 'Children (0-12)': 110, 'Teens (13-18)': 55, 'Adults (19-64)': 180, 'Seniors (65+)': 70},
    {'Date': '2023-04-05', 'Children (0-12)': 150, 'Teens (13-18)': 75, 'Adults (19-64)': 230, 'Seniors (65+)': 95},
    {'Date': '2023-04-06', 'Children (0-12)': 115, 'Teens (13-18)': 60, 'Adults (19-64)': 200, 'Seniors (65+)': 75},
    {'Date': '2023-04-07', 'Children (0-12)': 80, 'Teens (13-18)': 40, 'Adults (19-64)': 160, 'Seniors (65+)': 60},
    {'Date': '2023-04-08', 'Children (0-12)': 100, 'Teens (13-18)': 50, 'Adults (19-64)': 175, 'Seniors (65+)': 65}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Melt the dataframe to make it long-form
df_melted = df.melt(id_vars='Date', var_name='Age Group', value_name='Count')

# Plot using lineplot
plt.figure(figsize=(12, 6))
age_groups = df_melted['Age Group'].unique()[::-1]

# Initialize the baseline (very important for stacked plots)
baseline = pd.Series([0] * df.shape[0], index=df['Date'])

# We'll need to re-arrange the age group order to plot the correct stacking
for age_group in age_groups:
    # Get the data for the current age group
    series = df[age_group]
    
    # Plot the "fill" between the current series and the baseline
    plt.fill_between(df['Date'], baseline + series, baseline,
                     label=age_group, alpha=0.5)
    
    # Update the baseline to be the new top of the stack
    baseline += series

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Population by Age Group Over Time')
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

# Add legend at the bottom
plt.legend(title='Age Group', loc='upper left', bbox_to_anchor=(1, 1), frameon=False)

# Optimize layout
plt.tight_layout()

# Show plot
plt.show()