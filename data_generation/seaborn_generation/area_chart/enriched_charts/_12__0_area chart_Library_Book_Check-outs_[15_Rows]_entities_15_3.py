
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
    'Distance': [3.5, 4.2, 5.0, 3.8, 4.6, 5.5, 4.9, 5.1, 4.0, 3.7, 4.4, 5.3, 3.6, 4.7, 
                 5.6, 4.8, 3.9, 4.5, 5.4, 4.1, 3.4, 4.3, 5.2, 3.8, 4.9, 5.0, 4.2, 3.7, 
                 4.6, 5.1, 3.9]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Set the width and height of the figure
plt.figure(figsize=(14, 7))

# Create an area plot
sns.lineplot(data=df, x='Date', y='Distance', color='#1f77b4')

# Fill the area under the line
plt.fill_between(df['Date'], df['Distance'], color="#aec7e8")

# Rotate x-tick labels for better visibility
plt.xticks(rotation=45)

# Annotation for the highest distance in the dataset
highest_distance_date = df.loc[df['Distance'].idxmax(), 'Date']
highest_distance = df['Distance'].max()
plt.text(highest_distance_date, highest_distance, f'Highest: {highest_distance} km', ha='left', va='bottom')

# Setting chart title and labels
plt.title("Daily Running Distance in January 2023", pad=20)
plt.xlabel("Date")
plt.ylabel("Distance (km)")

# Show the plot
plt.show()