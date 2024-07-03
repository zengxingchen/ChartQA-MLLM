
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate the data
data = {
    'Sport': ['Soccer', 'Basketball', 'Tennis', 'Cricket', 'Baseball', 'Rugby', 
              'Golf', 'Swimming', 'Cycling', 'Running', 'Volleyball', 'Gymnastics',
              'Badminton', 'Boxing', 'Skiing', 'Hiking'],
    'Participation Rate': [45, 20, 12, 8, 15, 5, 18, 25, 30, 40, 22, 10, 15, 7, 9, 27]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create the bar chart
plt.figure(figsize=(10, 12))  # Change width and height of the chart
ax = sns.barplot(x='Participation Rate', y='Sport', data=df, palette=['#1f77b4', '#ff7f0e', '#2ca02c', 
                                                                      '#d62728', '#9467bd', '#8c564b', 
                                                                      '#e377c2', '#7f7f7f', '#bcbd22', 
                                                                      '#17becf', '#1f77b4', '#ff7f0e', 
                                                                      '#2ca02c', '#d62728', '#9467bd', 
                                                                      '#8c564b'],
                 dodge=False)

# Modify the width of bars
for bar in ax.patches:
    bar.set_height(0.6)

# Set the title
ax.set_title('Participation Rates in Various Sports', fontsize=16, pad=20)

# Show the plot
plt.show()