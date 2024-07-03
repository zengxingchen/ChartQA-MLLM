
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a dataset
data = {
    'Month': [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ],
    'AverageTemperature': [
        0.7, 1.2, 4.5, 9.8, 14.3, 18.2,
        19.9, 19.7, 15.5, 10.6, 5.2, 2.3
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
plt.figure(figsize=(12, 6))

# Create the area chart
area_chart = sns.lineplot(data=df, x='Month', y='AverageTemperature', color="#1f77b4")
area_chart.fill_between(df['Month'], df['AverageTemperature'], color="#1f77b4", alpha=0.3)

# Optionally, add an annotation/text label
for index, value in enumerate(df['AverageTemperature']):
    plt.text(df['Month'][index], value, f"{value}°C", 
             horizontalalignment='center', size='small', color='black')

# Customize title and axis labels
plt.title('Monthly Average Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')

# Display the chart
plt.show()