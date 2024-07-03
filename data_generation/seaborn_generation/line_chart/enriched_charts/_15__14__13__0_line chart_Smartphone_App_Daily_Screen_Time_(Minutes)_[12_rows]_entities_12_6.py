
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Arrivals': [1500, 1800, 1750, 1600, 1700, 1800, 2100, 2200, 1900, 2000, 1850, 2400]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Creating a line chart using seaborn
plt.figure(figsize=(14, 7))  # width: 14 inches, height: 7 inches
sns.set_theme(style="whitegrid")

# Plotting the data
lineplot = sns.lineplot(x='Month', y='Arrivals', data=df, 
                        color="#4A90E2", linewidth=2.5, marker='o')

# Annotating each point with its value
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Arrivals'][i] + 50, 
             df['Arrivals'][i], horizontalalignment='center')

# Customizing the chart appearance
lineplot.set_title('Monthly Tourist Arrivals in a City', fontsize=20, pad=20)
lineplot.set_xlabel('Month', fontsize=14)
lineplot.set_ylabel('Arrivals', fontsize=14)
plt.xticks(rotation=45)  # Rotate the x labels for better readability
plt.tight_layout()  # Adjusts the plot to make sure everything fits without overlap

# Display the plot
plt.show()