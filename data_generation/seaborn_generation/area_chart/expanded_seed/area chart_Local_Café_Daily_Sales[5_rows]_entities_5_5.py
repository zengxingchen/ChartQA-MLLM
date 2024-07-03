
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Date': '2023-03-01', 'Sales (USD)': 350},
    {'Date': '2023-03-02', 'Sales (USD)': 415},
    {'Date': '2023-03-03', 'Sales (USD)': 320},
    {'Date': '2023-03-04', 'Sales (USD)': 570},
    {'Date': '2023-03-05', 'Sales (USD)': 630}
]

# Convert list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sorting the DataFrame just in case the data isn't in date order
df.sort_values('Date', inplace=True)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create the line plot
sns.lineplot(data=df, x='Date', y='Sales (USD)', color="blue", lw=2)

# Use Matplotlib to fill the area under the line
plt.fill_between(df['Date'], df['Sales (USD)'], color='blue', alpha=0.3)

# Adding titles and labels
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales (USD)')

# Optimize date format on x-axis
plt.gcf().autofmt_xdate()

# Display the plot
plt.show()