
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Humidity': [65, 60, 55, 50, 45, 40, 35, 38, 42, 50, 55, 60]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Creating a line chart using seaborn
plt.figure(figsize=(12, 8))  # width: 12 inches, height: 8 inches
sns.set_theme(style="whitegrid")

# Plotting the data
lineplot = sns.lineplot(x='Month', y='Average_Humidity', data=df, 
                        color="#1f77b4", linewidth=2.5, marker='o')

# Annotating each point with its value
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Average_Humidity'][i] + 0.5, 
             df['Average_Humidity'][i], horizontalalignment='center')

# Customizing the chart appearance
lineplot.set_title('Monthly Average Humidity Trend', fontsize=18)
lineplot.set_xlabel('Month', fontsize=12)
lineplot.set_ylabel('Average Humidity (%)', fontsize=12)
plt.xticks(rotation=45)  # Rotate the x labels for better readability
plt.tight_layout()  # Adjusts the plot to make sure everything fits without overlap

# Display the plot
plt.show()