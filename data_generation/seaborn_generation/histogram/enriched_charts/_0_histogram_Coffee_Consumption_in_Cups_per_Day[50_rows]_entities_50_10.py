
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Table data in DataFrame format (this would normally come from a CSV file directly)
data = pd.DataFrame({
    'temperature': [
        -2.5, -1.7, 0.2, 3.5, 9.3, 14.1, 17.8, 16.9, 12.6, 7.2, 3.0, -0.4,
        -3.2, -1.5, 0.8, 4.4, 10.2, 15.0, 18.3, 17.1, 12.9, 6.8, 2.1, -1.2,
        -2.8, -1.0, 1.3, 5.1, 10.9, 16.4, 19.0, 17.5, 13.4, 7.5, 2.5, -0.1,
    ]
})

# Set the width and height of the figure
plt.figure(figsize=(10, 6))

# Create the histogram
sns.histplot(data=data, x="temperature", bins=30, color="#6A5ACD", kde=False, binwidth=1.0, orientation='horizontal')

# Add title and labels
plt.title('Distribution of Average Monthly Temperatures')
plt.xlabel('Frequency')
plt.ylabel('Temperature (°C)')

# Show the plot
plt.show()