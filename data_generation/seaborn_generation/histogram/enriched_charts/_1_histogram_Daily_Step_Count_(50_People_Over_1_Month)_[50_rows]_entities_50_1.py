
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame directly from the data provided
data = {
    'Temperature': [
        16.4, 17.1, 18.5, 19.8, 21.6, 22.4, 24.0, 24.8, 23.5, 22.1,
        20.6, 19.2, 18.1, 17.8, 16.3, 22.7, 23.3, 23.8, 23.2, 22.9,
        21.5, 20.0, 19.5, 17.2, 21.2, 21.9, 22.5, 24.1, 24.3, 24.9,
        23.6, 22.8, 20.8, 19.6, 18.2, 17.9, 16.6
    ]
}
df = pd.DataFrame(data)

# Customize the plot size
plt.figure(figsize=(10, 6))

# Plot the histogram with custom bin width (band) and color
sns.histplot(df['Temperature'], bins=15, color='#3498db', kde=False, binwidth=0.5)

# Customize the plot labels and title
plt.title('Average Monthly Temperatures Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')

# Show the plot
plt.show()