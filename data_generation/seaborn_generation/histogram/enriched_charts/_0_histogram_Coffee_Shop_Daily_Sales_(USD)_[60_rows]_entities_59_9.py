
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the dataframe from the provided data points
data = {
    'Temperature': [
        22, 23, 23, 24, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27,
        27, 27, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29,
        29, 30, 30, 30, 30, 30, 31, 31, 31, 31, 32, 32, 32, 33,
        33, 34
    ]
}
df = pd.DataFrame(data)

# Set the size of the chart
plt.figure(figsize=(10, 6))

# Plot a horizontal histogram (orient='h') with a modified color scheme and adjusted band width
sns.histplot(data=df, y='Temperature', binwidth=0.5, color='#3498db')

# Customize the appearance of the plot
plt.title('Distribution of Daily Average Temperatures')
plt.xlabel('Frequency')
plt.ylabel('Temperature (°C)')

# Show the plot
plt.show()