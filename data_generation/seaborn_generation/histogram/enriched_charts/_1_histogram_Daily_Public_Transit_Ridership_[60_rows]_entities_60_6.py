
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data from table above
data = {
    'Average_Monthly_Temperature': [
        16.7, 19.5, 21.2, 15.8, 22.6, 14.2, 13.8, 17.1, 18.4,
        20.2, 15.9, 22.3, 17.0, 16.2, 20.5, 17.3, 19.0, 21.7,
        14.1, 13.7, 22.0, 12.9, 23.5, 24.8, 14.8, 11.4, 16.9,
        13.2, 13.5, 17.4, 18.7, 19.9, 15.6, 21.0, 23.2, 17.7,
        19.6, 20.4, 13.9, 10.8, 15.3, 19.8, 21.1, 13.4, 12.6,
        20.7, 22.9, 24.2, 14.3, 11.2
    ]
}

df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(12, 6))

# Plotting the histogram with specific color codes and modified band width
sns.histplot(df['Average_Monthly_Temperature'], color="#3498db", binwidth=0.5, kde=True)

# Adding titles and labels
plt.title('Distribution of Average Monthly Temperatures')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')

# Display the plot
plt.show()