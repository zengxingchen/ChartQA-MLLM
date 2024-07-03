
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create the dataframe from the given data
data = {
    'Age_Group': ['Under 18', '18-25', '26-35', '36-45', '46-55', '56-65', '65 and over'],
    'Average_Weekly_Exercise_Hours': [5, 7, 6, 5, 4, 3, 2]
}

df = pd.DataFrame(data)

# Define a color palette with hexadecimal color codes
colors = ["#ff5733", "#33ff57", "#3357ff", "#ff33a8",
          "#a833ff", "#33ffd6", "#ff8c33"]

# Create a figure and adjust its size
plt.figure(figsize=(10, 12))

# Draw a vertical barplot
barplot = sns.barplot(
    x='Age_Group',
    y='Average_Weekly_Exercise_Hours',
    data=df,
    palette=colors
)

# Modify bar width
for bar in barplot.patches:
    bar.set_width(0.6)

# Draw the plot
plt.title('Average Weekly Exercise Hours by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Weekly Exercise Hours')

plt.tight_layout()
plt.show()