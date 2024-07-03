
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "AverageRainfall": [78.3, 62.5, 85.6, 70.8, 95.1, 112.3, 103.4, 110.8, 92.5, 81.7, 67.2, 75.4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type to maintain month order in the plot
df['Month'] = pd.Categorical(df['Month'], categories=[
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"], ordered=True)

# Create the line plot
plt.figure(figsize=(14, 7))
sns.lineplot(x="Month", y="AverageRainfall", data=df, marker='o', color='#1f77b4')

# Annotate each point with the rainfall value
for i in range(df.shape[0]):
    plt.text(x=df['Month'][i], y=df['AverageRainfall'][i] + 2, s=f"{df['AverageRainfall'][i]} mm", 
             horizontalalignment='center')

# Set the title and labels
plt.title('Monthly Average Rainfall in Rainforest Region', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Average Rainfall (mm)')

# Show the plot
plt.show()