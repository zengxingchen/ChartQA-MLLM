
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Mock data for the average annual temperature of various cities
data = {
    'Temperature': [
        15, 16, 15, 14, 16, 17, 14, 15, 16, 17, 17, 18, 19, 15, 16, 17, 18, 19, 
        20, 21, 22, 23, 24, 24, 23, 22, 21, 24, 25, 26, 27, 29, 27, 28, 28
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(10, 6))

# Create the histogram
sns.histplot(data=df, x='Temperature', bins=15, color='#3498db', binwidth=1)

# Customizing the plot's aesthetics
plt.title('Histogram of Average Annual Temperatures')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')

# Show the plot
plt.show()