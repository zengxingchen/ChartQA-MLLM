
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate the data
data = {
    'Country': ['Canada', 'United States', 'Mexico', 'Brazil', 'United Kingdom', 'Germany', 
                'France', 'Italy', 'Russia', 'China', 'India', 'Australia', 'Japan', 
                'South Korea', 'Nigeria', 'Egypt'],
    'Average_Daily_Sleep_Time': [7.2, 6.8, 7.5, 7.0, 7.4, 7.6, 7.8, 8.0, 6.5, 6.8, 7.1, 7.3, 6.5, 6.0, 7.7, 7.4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create the horizontal bar chart
plt.figure(figsize=(14, 8))  # Change width and height of the chart
ax = sns.barplot(y='Country', x='Average_Daily_Sleep_Time', data=df, palette=['#3498db', '#e74c3c', '#2ecc71', 
                                                                               '#f39c12', '#9b59b6', '#34495e',
                                                                               '#e67e22', '#1abc9c', '#7f8c8d',
                                                                               '#2980b9', '#c0392b', '#27ae60',
                                                                               '#d35400', '#8e44ad', '#2c3e50',
                                                                               '#16a085'],
                 dodge=False)

# Modify the height of bars
for bar in ax.patches:
    bar.set_height(0.6)

# Set the title
ax.set_title('Average Daily Sleep Time by Country (hours per day)', fontsize=18, pad=20)

# Rotate x-axis labels for better readability
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

# Show the plot
plt.show()