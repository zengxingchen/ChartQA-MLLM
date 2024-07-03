
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Let's create a DataFrame with daily average temperatures over a year
data = {
    'Temperature': [
        24.5, 18.2, 21.7, 22.1, 19.8, 18.3, 27.4, 26.1, 21.9, 20.3, 19.4, 17.2, 23.6, 24.8,
        # (Assuming more data points for the entire year are added here)
        22.6, 21.8, 19.9, 20.2, 23.3, 26.7, 24.9, 25.3, 22.4, 23.7, 21.5, 26.5
    ]
}

# Convert the data dictionary to a DataFrame
df = pd.DataFrame(data)

# Set the figure size for better clarity
plt.figure(figsize=(10, 6))

# Plotting the histogram using seaborn
sns.histplot(df['Temperature'], 
             bins=30, # You can change the number of bins for a different "band width"
             kde=False, 
             color='#FF5733', # A specific color code for better visual appeal
             binwidth=1 # Setting the width of each bin to 1 degree Celsius
            )

# Set the title and labels for the chart
plt.title('Histogram of Daily Average Temperatures Over a Year')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')

# Show the plot
plt.show()