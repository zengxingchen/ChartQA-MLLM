
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given chart table data in a list of dictionaries
data = [
    {'Date': '2023-03-20', 'Cups Sold': 150},
    {'Date': '2023-03-21', 'Cups Sold': 200},
    {'Date': '2023-03-22', 'Cups Sold': 175},
    {'Date': '2023-03-23', 'Cups Sold': 190},
    {'Date': '2023-03-24', 'Cups Sold': 180}
]

# Converting the list of dictionaries into a DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by 'Date', in case it's not sorted
df = df.sort_values('Date')

# We'll create the lineplot first, then fill the area beneath it
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))  # Size of the figure can be adjusted according to need

# Creating the line plot
line = sns.lineplot(x='Date', y='Cups Sold', data=df, color='blue', lw=2)

# Now we fill the area under the lineplot
plt.fill_between(df['Date'], df['Cups Sold'], alpha=0.3)

# Additional customizations
plt.title('Cups Sold over Time')
plt.xlabel('Date')
plt.ylabel('Cups Sold')
plt.tight_layout()  # Ensure nothing is cut off when saving the plot

# Optionally, save the figure to a file
# plt.savefig('area_chart.png')

# Display the plot
plt.show()