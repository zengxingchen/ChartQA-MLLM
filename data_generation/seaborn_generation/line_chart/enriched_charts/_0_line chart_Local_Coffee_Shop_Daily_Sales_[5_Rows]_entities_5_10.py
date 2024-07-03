
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "AverageTemperature": [4.5, 5.2, 8.5, 12.3, 16.7, 20.1, 23.4, 22.8, 18.5, 13.7, 8.6, 5.0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type to maintain month order in the plot
df['Month'] = pd.Categorical(df['Month'], categories=[
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"], ordered=True)

# Create the line plot
plt.figure(figsize=(12, 6))
sns.lineplot(x="Month", y="AverageTemperature", data=df, marker='o', color='#FF5733')

# Annotate each point with the temperature value
for i in range(df.shape[0]):
    plt.text(x=df['Month'][i], y=df['AverageTemperature'][i] + 0.5, s=f"{df['AverageTemperature'][i]}°C", 
             horizontalalignment='center')

# Set the title and labels
plt.title('Monthly Average Temperature in Seaside City')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')

# Show the plot
plt.show()