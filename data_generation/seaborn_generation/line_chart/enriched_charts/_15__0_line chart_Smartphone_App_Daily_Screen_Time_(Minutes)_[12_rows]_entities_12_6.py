
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Number_of_Visitors': [500, 450, 600, 800, 1200, 1500, 1800, 1750, 1400, 900, 700, 550]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Creating a line chart using seaborn
plt.figure(figsize=(16, 8))  # width: 16 inches, height: 8 inches
sns.set_theme(style="whitegrid")

# Plotting the data
lineplot = sns.lineplot(x='Month', y='Number_of_Visitors', data=df, 
                        color="#1f77b4", linewidth=2.5, marker='o')

# Annotating each point with its value
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Number_of_Visitors'][i] + 50, 
             df['Number_of_Visitors'][i], horizontalalignment='center')

# Customizing the chart appearance
lineplot.set_title('Monthly Visitor Trends at the Museum', fontsize=20, pad=20)
lineplot.set_xlabel('Month', fontsize=14)
lineplot.set_ylabel('Number of Visitors', fontsize=14)
plt.xticks(rotation=45)  # Rotate the x labels for better readability
plt.tight_layout()  # Adjusts the plot to make sure everything fits without overlap

# Display the plot
plt.show()