
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create the dataframe from the given data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Monthly_Internet_Users_Millions': [120, 115, 130, 140, 150, 160, 170, 165, 155, 145, 135, 125]
}

df = pd.DataFrame(data)

# Define a color palette with hexadecimal color codes
colors = ["#ff5733", "#33ff57", "#3357ff", "#ff33a1", "#a133ff", 
          "#33ffa1", "#ffaa33", "#33a1ff", "#ff3333", "#33ff33", 
          "#5733ff", "#a1ff33"]

# Create a figure and adjust its size
plt.figure(figsize=(12, 10))

# Draw a vertical barplot
barplot = sns.barplot(
    x='Month',
    y='Monthly_Internet_Users_Millions',
    data=df,
    palette=colors
)

# Modify bar width
for bar in barplot.patches:
    bar.set_width(0.5)

# Draw the plot
plt.title('Monthly Internet Users in a City')
plt.xlabel('Month')
plt.ylabel('Internet Users (Millions)')

plt.tight_layout()
plt.show()