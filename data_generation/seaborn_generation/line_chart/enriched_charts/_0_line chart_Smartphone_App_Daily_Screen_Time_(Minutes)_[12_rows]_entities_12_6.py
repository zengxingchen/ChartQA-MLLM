
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature': [5, 6, 10, 15, 20, 25, 28, 27, 22, 16, 10, 6]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Creating a line chart using seaborn
plt.figure(figsize=(14, 6))  # width: 14 inches , height: 6 inches
sns.set_theme(style="whitegrid")

# Plotting the data
lineplot = sns.lineplot(x='Month', y='Average_Temperature', data=df, 
                        palette=["#FF5733"], linewidth=2.5, marker='o')

# Annotating each point with its value
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Average_Temperature'][i] + 0.5, 
             df['Average_Temperature'][i], horizontalalignment='center')

# Customizing the chart appearance
lineplot.set_title('Monthly Average Temperature Trend', fontsize=18)
lineplot.set_xlabel('Month', fontsize=12)
lineplot.set_ylabel('Average Temperature (°C)', fontsize=12)
plt.xticks(rotation=45)  # Rotate the x labels for better readability
plt.tight_layout()  # Adjusts the plot to make sure everything fits without overlap

# Display the plot
plt.show()