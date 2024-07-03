
import pandas as pd
import matplotlib.pyplot as plt

# Create a dataset
data = {
    'Month': [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ],
    'Number_of_Articles': [
        8, 12, 15, 22, 30, 35,
        40, 38, 33, 28, 20, 10
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
plt.figure(figsize=(16, 9))

# Create the area chart
plt.plot(df['Month'], df['Number_of_Articles'], color="#2E86C1")
plt.fill_between(df['Month'], df['Number_of_Articles'], color="#2E86C1", alpha=0.3)

# Optionally, add an annotation/text label
for index, value in enumerate(df['Number_of_Articles']):
    plt.text(df['Month'][index], value, f"{value}", 
             horizontalalignment='center', size='small', color='black')

# Customize title and axis labels
plt.title('Monthly Published Articles on Future Technologies & Society', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Articles')

# Display the chart
plt.show()