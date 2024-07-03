
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = [
    {'Person': 'Person 1', 'Cups': 3},
    {'Person': 'Person 2', 'Cups': 1},
    {'Person': 'Person 3', 'Cups': 5},
    {'Person': 'Person 4', 'Cups': 2},
    {'Person': 'Person 5', 'Cups': 0},
    {'Person': 'Person 6', 'Cups': 4},
    {'Person': 'Person 7', 'Cups': 2},
    {'Person': 'Person 8', 'Cups': 3},
    {'Person': 'Person 9', 'Cups': 1},
    {'Person': 'Person 10', 'Cups': 2},
    {'Person': 'Person 11', 'Cups': 2},
    {'Person': 'Person 12', 'Cups': 0},
    {'Person': 'Person 13', 'Cups': 3},
    {'Person': 'Person 14', 'Cups': 4},
    {'Person': 'Person 15', 'Cups': 1}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Set the palette color
sns.set_palette('pastel')

# Create figure and axis
plt.figure(figsize=(10, 6))

# Create histogram
sns.histplot(data=df, x='Cups', bins=6, kde=False, hue='Person', multiple="stack")

# Additional visual encodings
plt.xticks(range(0, 6)) # x-axis labels representing the number of cups
plt.yticks(range(0, len(df) + 1)) # y-axis labels representing frequency
plt.xlabel('Number of Cups') # x-axis label
plt.ylabel('Number of People') # y-axis label
plt.title('Distribution of Cups consumed by Persons') # title
plt.legend(title='Person ID', bbox_to_anchor=(1.05, 1), loc='upper left') # legend outside the plot

# Show the plot
plt.tight_layout()
plt.show()