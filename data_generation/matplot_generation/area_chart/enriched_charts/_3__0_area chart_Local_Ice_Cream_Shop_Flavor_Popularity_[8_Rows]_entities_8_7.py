
import pandas as pd
import matplotlib.pyplot as plt

# Create a dataset
data = {
    'Month': [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ],
    'Number_of_Visits': [
        100, 120, 300, 450, 500, 700,
        850, 900, 750, 600, 400, 250
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
plt.figure(figsize=(14, 7))

# Create the area chart
area_chart = plt.plot(df['Month'], df['Number_of_Visits'], color="#ff5733")
plt.fill_between(df['Month'], df['Number_of_Visits'], color="#ff5733", alpha=0.3)

# Optionally, add an annotation/text label
for index, value in enumerate(df['Number_of_Visits']):
    plt.text(df['Month'][index], value, f"{value}", 
             horizontalalignment='center', size='small', color='black')

# Customize title and axis labels
plt.title('Monthly Visits to the Art Museum')
plt.xlabel('Month')
plt.ylabel('Number of Visits')

# Display the chart
plt.show()