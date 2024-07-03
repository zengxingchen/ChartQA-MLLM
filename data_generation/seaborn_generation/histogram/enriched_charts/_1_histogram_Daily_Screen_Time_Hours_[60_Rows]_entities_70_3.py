
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Constructing a DataFrame from our dataset
data = {
    'AverageTemperature': [
        15, 14.8, 15.2, 13, 12.5,
        # ... (data continues for each day of the year)
        14.6, 15, 15.3, 14.9, 15.1
    ]
}
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create the histogram
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x="AverageTemperature", color="#3498db", binwidth=0.5)

# Additional customizations
plt.title('Histogram of Daily Average Temperatures for a Year')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')

# Show the plot
plt.show()