
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create the dataframe from the given data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature_Celsius': [5, 6, 10, 15, 19, 23, 26, 25, 20, 14, 9, 6]
}

df = pd.DataFrame(data)

# Define a color palette with hexadecimal color codes
colors = ["#003f5c", "#2f4b7c", "#665191", "#a05195",
          "#d45087", "#f95d6a", "#ff7c43", "#ffa600",
          "#acd27e", "#65a56f", "#2b7a78", "#003f5a"]

# Create a figure and adjust its size
plt.figure(figsize=(14, 8))

# Draw a horizontal barplot
barplot = sns.barplot(
    y='Month',
    x='Average_Temperature_Celsius',
    data=df,
    palette=colors,
    orient='h'
)

# Modify bar width
for bar in barplot.patches:
    bar.set_height(0.6)

# Draw the plot
plt.title('Average Monthly Temperature in a City')
plt.xlabel('Temperature (°C)')
plt.ylabel('Month')

plt.tight_layout()
plt.show()