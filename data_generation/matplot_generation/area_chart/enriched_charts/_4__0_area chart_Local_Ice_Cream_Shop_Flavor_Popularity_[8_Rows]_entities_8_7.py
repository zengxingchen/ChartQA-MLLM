
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a dataset
data = {
    'Month': [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ],
    'Visitors': [
        5000, 4200, 5500, 6000, 7500, 8100,
        9000, 8600, 7800, 7300, 6000, 4800
    ]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Convert 'Month' into categorical data type for correct plotting
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
], ordered=True)

# Set the size of the chart
plt.figure(figsize=(14, 8))

# Create the area chart
area_chart = sns.lineplot(data=df, x='Month', y='Visitors', color="#FF5733")
area_chart.fill_between(df['Month'], df['Visitors'], color="#FF5733", alpha=0.4)

# Add an annotation/text label
for index, value in enumerate(df['Visitors']):
    plt.text(df['Month'][index], value, f"{value}", 
             horizontalalignment='center', size='small', color='black')

# Customize title and axis labels
plt.title('Monthly Visitors to the Museum')
plt.xlabel('Month')
plt.ylabel('Number of Visitors')

# Display the chart
plt.show()