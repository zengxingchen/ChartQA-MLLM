
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Creating the DataFrame
data = {
    'Date': ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
             "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10",
             "2023-01-11", "2023-01-12", "2023-01-13", "2023-01-14", "2023-01-15",
             "2023-01-16", "2023-01-17", "2023-01-18", "2023-01-19", "2023-01-20",
             "2023-01-21", "2023-01-22", "2023-01-23", "2023-01-24", "2023-01-25",
             "2023-01-26", "2023-01-27", "2023-01-28", "2023-01-29", "2023-01-30",
             "2023-01-31"],
    'Temperature': [5, 6, 7, 5, 8, 9, 6, 7, 8, 7, 5, 6, 9, 5, 7, 8, 9, 5, 8, 5, 6,
                    7, 8, 9, 5, 6, 8, 9, 7, 6, 5]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Set the width and height of the figure
plt.figure(figsize=(12, 6))

# Create an area plot
sns.lineplot(data=df, x='Date', y='Temperature', color='#0077b6')

# Fill the area under the line
plt.fill_between(df['Date'], df['Temperature'], color="#90e0ef")

# Rotate x-tick labels for better visibility
plt.xticks(rotation=45)

# Annotation for the highest temperature in the dataset
highest_temp_date = df.loc[df['Temperature'].idxmax(), 'Date']
highest_temp = df['Temperature'].max()
plt.text(highest_temp_date, highest_temp, f'Highest: {highest_temp}°C', ha='left', va='bottom')

# Setting chart title and labels
plt.title("Average Daily Temperature in January 2023")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")

# Show the plot
plt.show()