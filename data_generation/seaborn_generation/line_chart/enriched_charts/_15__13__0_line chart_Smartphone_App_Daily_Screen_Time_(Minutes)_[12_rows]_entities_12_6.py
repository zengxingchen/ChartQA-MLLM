
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Investment': [50, 60, 80, 120, 180, 250, 400, 380, 300, 200, 120, 90]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Creating a line chart using seaborn
plt.figure(figsize=(14, 7))  # width: 14 inches, height: 7 inches
sns.set_theme(style="whitegrid")

# Plotting the data
lineplot = sns.lineplot(x='Month', y='Investment', data=df, 
                        color="#FF5733", linewidth=2.5, marker='o')

# Annotating each point with its value
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Investment'][i] + 10, 
             df['Investment'][i], horizontalalignment='center')

# Customizing the chart appearance
lineplot.set_title('Monthly Investment Growth', fontsize=20, pad=30)
lineplot.set_xlabel('Month', fontsize=14)
lineplot.set_ylabel('Investment (in Thousands)', fontsize=14)
plt.xticks(rotation=45)  # Rotate the x labels for better readability
plt.tight_layout()  # Adjusts the plot to make sure everything fits without overlap

# Display the plot
plt.show()