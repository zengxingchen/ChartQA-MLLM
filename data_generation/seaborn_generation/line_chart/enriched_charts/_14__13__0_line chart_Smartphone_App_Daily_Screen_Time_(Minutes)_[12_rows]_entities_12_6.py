
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [500, 450, 480, 520, 580, 630, 700, 690, 670, 640, 600, 560]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Creating a line chart using seaborn
plt.figure(figsize=(12, 6))  # width: 12 inches, height: 6 inches
sns.set_theme(style="whitegrid")

# Plotting the data
lineplot = sns.lineplot(x='Month', y='Revenue', data=df, 
                        color="#FF5733", linewidth=2.5, marker='o')

# Annotating each point with its value
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Revenue'][i] + 10, 
             df['Revenue'][i], horizontalalignment='center')

# Customizing the chart appearance
lineplot.set_title('Monthly Revenue Trend in a Business', fontsize=20, pad=20)
lineplot.set_xlabel('Month', fontsize=14)
lineplot.set_ylabel('Revenue (in $)', fontsize=14)
plt.xticks(rotation=45)  # Rotate the x labels for better readability
plt.tight_layout()  # Adjusts the plot to make sure everything fits without overlap

# Display the plot
plt.show()