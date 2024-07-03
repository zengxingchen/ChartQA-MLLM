
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data points provided
data = {
    'Category': [f'Category {i}' for i in range(1, 21)],
    'Value': [100, 150, 130, 200, 180, 160, 170, 190, 210, 230, 220, 240, 260, 250, 270, 280, 300, 290, 310, 320]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the bar plot and modify it according to the given options
plt.figure(figsize=(14, 10))  # Change width and height of chart
barplot = sns.barplot(y='Category', x='Value', data=df, color="#33A1C9", orient='h')  # Horizontal and specific color

# Modify the width of bars using 'dodge'
barplot.set(xlim=(0, 350))  # Accommodate the increased bar width
sns.despine(left=True, bottom=True)

# Adjust the appearance of the plot
plt.title('Category Values Overview', fontsize=18)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Category', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Show the barplot
plt.show()