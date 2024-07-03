
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Visitors': [120, 150, 200, 300, 500, 700, 1000, 900, 600, 400, 200, 150]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Creating a line chart using seaborn
plt.figure(figsize=(16, 8))  # width: 16 inches, height: 8 inches
sns.set_theme(style="whitegrid")

# Plotting the data
lineplot = sns.lineplot(x='Month', y='Visitors', data=df, 
                        color="#1f77b4", linewidth=2.5, marker='o')

# Annotating each point with its value
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Visitors'][i] + 20, 
             df['Visitors'][i], horizontalalignment='center')

# Customizing the chart appearance
lineplot.set_title('Monthly Tourist Visitors Trend', fontsize=20, pad=20)
lineplot.set_xlabel('Month', fontsize=14)
lineplot.set_ylabel('Number of Visitors', fontsize=14)
plt.xticks(rotation=45)  # Rotate the x labels for better readability
plt.tight_layout()  # Adjusts the plot to make sure everything fits without overlap

# Display the plot
plt.show()