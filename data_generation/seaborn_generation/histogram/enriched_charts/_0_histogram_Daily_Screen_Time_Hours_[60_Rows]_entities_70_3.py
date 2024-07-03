
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Table Data (provided above)
data = {
    "Temperature": [6.7, 9.3, 15.4, 7.2, 10.1, 13.9, 8.6, 14.0, 11.2, 9.5,
                    12.3, 14.2, 10.5, 8.2, 7.4, 13.8, 9.6, 12.9, 14.7, 11.5,
                    7.3, 10.2, 16.1, 8.9, 15.7, 9.7, 14.3, 11.0, 12.5, 10.9,
                    13.3, 7.8, 9.1, 12.7, 11.3, 14.9, 7.5, 15.0, 10.3, 13.5,
                    9.2, 11.9, 14.1, 7.6, 10.4, 12.8, 16.3, 7.0, 15.2, 14.5]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(10, 8))

# Create a horizontal histogram
sns.histplot(data=df, x="Temperature", color="#42A5F5", binwidth=0.5, orientation='horizontal')

# Additional customization
plt.title('Distribution of Average Yearly Temperatures')
plt.xlabel('Frequency')
plt.ylabel('Temperature (°C)')
plt.grid(True)

# Show the plot
plt.show()