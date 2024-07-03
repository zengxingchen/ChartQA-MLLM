
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data from the chart table provided
data = [
    {'Date': '2023-03-01', '0-12 Years': 45, '13-18 Years': 30, '19-35 Years': 87, '36-50 Years': 58, '51+ Years': 72},
    {'Date': '2023-03-04', '0-12 Years': 50, '13-18 Years': 45, '19-35 Years': 95, '36-50 Years': 60, '51+ Years': 80},
    {'Date': '2023-03-08', '0-12 Years': 40, '13-18 Years': 32, '19-35 Years': 110, '36-50 Years': 50, '51+ Years': 67},
    {'Date': '2023-03-12', '0-12 Years': 55, '13-18 Years': 48, '19-35 Years': 100, '36-50 Years': 65, '51+ Years': 75},
    {'Date': '2023-03-16', '0-12 Years': 60, '13-18 Years': 50, '19-35 Years': 95, '36-50 Years': 70, '51+ Years': 70},
    {'Date': '2023-03-20', '0-12 Years': 42, '13-18 Years': 35, '19-35 Years': 102, '36-50 Years': 60, '51+ Years': 76},
    {'Date': '2023-03-24', '0-12 Years': 65, '13-18 Years': 55, '19-35 Years': 108, '36-50 Years': 58, '51+ Years': 82},
    {'Date': '2023-03-28', '0-12 Years': 50, '13-18 Years': 40, '19-35 Years': 99, '36-50 Years': 55, '51+ Years': 85},
    {'Date': '2023-03-31', '0-12 Years': 70, '13-18 Years': 60, '19-35 Years': 120, '36-50 Years': 67, '51+ Years': 90}
]

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(data)
# Ensure Date is of datetime type
df['Date'] = pd.to_datetime(df['Date'])

# We need to first melt the dataframe to have separate rows for each age group
df_melted = df.melt(id_vars='Date', var_name='Age Group', value_name='Value')

# Now create the plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_melted, x='Date', y='Value', hue='Age Group', marker="o")

# Beautify the plot
plt.title('Age Group Trends over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend(title='Age Group')

# Ensure the x-axis labels are not cramped
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()