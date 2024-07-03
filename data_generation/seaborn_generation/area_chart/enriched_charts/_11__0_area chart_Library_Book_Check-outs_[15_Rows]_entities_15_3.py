
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
    'Steps': [5000, 5200, 4800, 5300, 5100, 5500, 5700, 5400, 5900, 6200, 6000, 6500, 
              6200, 6400, 6700, 6900, 7000, 7200, 7500, 7700, 7600, 7400, 7800, 8000, 
              8200, 8300, 8100, 8500, 8700, 8800, 9000]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Set the width and height of the figure
plt.figure(figsize=(14, 8))

# Create an area plot
sns.lineplot(data=df, x='Date', y='Steps', color='#ff5733')

# Fill the area under the line
plt.fill_between(df['Date'], df['Steps'], color="#ffe6e6")

# Rotate x-tick labels for better visibility
plt.xticks(rotation=45)

# Annotation for the highest step count in the dataset
highest_steps_date = df.loc[df['Steps'].idxmax(), 'Date']
highest_steps = df['Steps'].max()
plt.text(highest_steps_date, highest_steps, f'Highest: {highest_steps} steps', ha='left', va='bottom')

# Setting chart title and labels
plt.title("Average Daily Steps in January 2023", pad=20)
plt.xlabel("Date")
plt.ylabel("Steps")

# Show the plot
plt.show()