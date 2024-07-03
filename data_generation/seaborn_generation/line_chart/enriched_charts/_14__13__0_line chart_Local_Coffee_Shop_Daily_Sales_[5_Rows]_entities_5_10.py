
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Month": ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"],
    "AverageTemperature": [28.3, 29.1, 30.2, 31.5, 32.8, 33.1, 32.7, 32.5, 31.0, 29.5, 28.0, 27.5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type to maintain month order in the plot
df['Month'] = pd.Categorical(df['Month'], categories=[
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"], ordered=True)

# Create the line plot
plt.figure(figsize=(16, 8))
sns.lineplot(x="Month", y="AverageTemperature", data=df, marker='o', color='#FF5733')

# Annotate each point with the temperature value
for i in range(df.shape[0]):
    plt.text(x=df['Month'][i], y=df['AverageTemperature'][i] + 0.2, s=f"{df['AverageTemperature'][i]}°C", 
             horizontalalignment='center')

# Set the title and labels
plt.title('Monthly Average Temperature in a Tropical City', fontsize=18, pad=20)
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')

# Show the plot
plt.show()