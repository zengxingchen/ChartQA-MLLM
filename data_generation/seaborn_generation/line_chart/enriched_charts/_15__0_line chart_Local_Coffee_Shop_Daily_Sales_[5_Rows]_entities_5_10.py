
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "AverageRainfall": [80.5, 70.2, 85.1, 90.3, 95.7, 100.2, 105.4, 103.8, 98.5, 88.7, 78.6, 75.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type to maintain month order in the plot
df['Month'] = pd.Categorical(df['Month'], categories=[
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"], ordered=True)

# Create the line plot
plt.figure(figsize=(14, 7))
sns.lineplot(x="Month", y="AverageRainfall", data=df, marker='o', color='#1E90FF')

# Annotate each point with the rainfall value
for i in range(df.shape[0]):
    plt.text(x=df['Month'][i], y=df['AverageRainfall'][i] + 2, s=f"{df['AverageRainfall'][i]} mm", 
             horizontalalignment='center')

# Set the title and labels
plt.title('Monthly Average Rainfall in Rainforest Region')
plt.xlabel('Month')
plt.ylabel('Average Rainfall (mm)')

# Show the plot
plt.show()