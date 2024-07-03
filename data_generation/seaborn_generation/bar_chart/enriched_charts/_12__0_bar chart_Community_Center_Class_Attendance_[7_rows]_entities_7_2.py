
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create the dataframe from the given data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Visitors_Thousands': [50, 45, 60, 80, 110, 150, 200, 180, 130, 90, 60, 40]
}

df = pd.DataFrame(data)

# Define a color palette with hexadecimal color codes
colors = ["#1b9e77", "#d95f02", "#7570b3", "#e7298a",
          "#66a61e", "#e6ab02", "#a6761d", "#666666",
          "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]

# Create a figure and adjust its size
plt.figure(figsize=(10, 12))

# Draw a vertical barplot
barplot = sns.barplot(
    x='Month',
    y='Average_Visitors_Thousands',
    data=df,
    palette=colors,
    orient='v'
)

# Modify bar width
for bar in barplot.patches:
    bar.set_width(0.5)

# Draw the plot
plt.title('Average Monthly Visitors to a National Park', pad=20)
plt.xlabel('Month')
plt.ylabel('Visitors (Thousands)')

plt.tight_layout()
plt.show()