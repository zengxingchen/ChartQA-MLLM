
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Age Group': '0-12', 'Monday Visitors': 30, 'Tuesday Visitors': 25, 'Wednesday Visitors': 28},
    {'Age Group': '13-18', 'Monday Visitors': 45, 'Tuesday Visitors': 40, 'Wednesday Visitors': 50},
    {'Age Group': '19-25', 'Monday Visitors': 70, 'Tuesday Visitors': 65, 'Wednesday Visitors': 80},
    {'Age Group': '26-35', 'Monday Visitors': 60, 'Tuesday Visitors': 70, 'Wednesday Visitors': 75},
    {'Age Group': '36-50', 'Monday Visitors': 55, 'Tuesday Visitors': 45, 'Wednesday Visitors': 50},
    {'Age Group': '51-65', 'Monday Visitors': 40, 'Tuesday Visitors': 50, 'Wednesday Visitors': 45},
    {'Age Group': '66-75', 'Monday Visitors': 20, 'Tuesday Visitors': 15, 'Wednesday Visitors': 25},
    {'Age Group': '76+', 'Monday Visitors': 10, 'Tuesday Visitors': 10, 'Wednesday Visitors': 15}
]

# Convert the list of dictionaries to a dataframe
df = pd.DataFrame(data)

# Melt the dataframe to get it in 'long' format
df_melted = df.melt(id_vars='Age Group', var_name='Day', value_name='Visitors')

# Replace 'Monday Visitors', 'Tuesday Visitors', 'Wednesday Visitors' with 'Monday', 'Tuesday', 'Wednesday'
df_melted['Day'] = df_melted['Day'].str.replace(' Visitors', '')

# Generate a scatterplot
plt.figure(figsize=(10, 6))
scatterplot = sns.scatterplot(data=df_melted,
                              x='Age Group',
                              y='Visitors',
                              hue='Day',
                              style='Day',
                              palette='deep',
                              s=100) # s is the size of the markers

plt.title('Visitors by Age Group and Day of the Week')
plt.xlabel('Age Group')
plt.ylabel('Number of Visitors')
plt.xticks(rotation=45) # Rotating the x-axis labels for better readability
plt.legend(title='Day of the Week')
plt.tight_layout() # Adjusts plot to ensure everything fits without overlapping
plt.show()