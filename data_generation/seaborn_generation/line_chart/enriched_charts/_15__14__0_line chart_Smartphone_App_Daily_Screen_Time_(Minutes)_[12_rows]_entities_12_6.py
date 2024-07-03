
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Happiness_Index': [70, 72, 75, 73, 78, 80, 77, 76, 74, 72, 69, 71]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Creating a line chart using seaborn
plt.figure(figsize=(14, 10))  # width: 14 inches, height: 10 inches
sns.set_theme(style="whitegrid")

# Plotting the data
lineplot = sns.lineplot(x='Month', y='Happiness_Index', data=df, 
                        color="#FF5733", linewidth=2.5, marker='o')

# Annotating each point with its value
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Happiness_Index'][i] + 0.5, 
             df['Happiness_Index'][i], horizontalalignment='center')

# Customizing the chart appearance
lineplot.set_title('Monthly Happiness Index Trend', fontsize=18, pad=20)
lineplot.set_xlabel('Month', fontsize=12)
lineplot.set_ylabel('Happiness Index', fontsize=12)
plt.xticks(rotation=45)  # Rotate the x labels for better readability
plt.tight_layout()  # Adjusts the plot to make sure everything fits without overlap

# Display the plot
plt.show()