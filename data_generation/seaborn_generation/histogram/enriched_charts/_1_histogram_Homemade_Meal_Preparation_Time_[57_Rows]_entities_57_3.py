
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {
    "Temperature": [
        16, 17, 18, 19, 21, 22, 22, 23, 24, 24, 25, 25, 26, 26, 26,
        27, 28, 28, 29, 30, 31, 31, 32, 33, 33, 34, 34, 35, 35, 35,
        36, 37, 37, 38, 39, 40
    ]
}

df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(12, 6))

# Create the histogram
sns.histplot(df['Temperature'], 
             bins=10, 
             kde=False, 
             color='#3498db', 
             binwidth=1)

# Set titles and labels
plt.title('Distribution of Average Daily Temperatures Over a Year')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Frequency')

# Display the plot
plt.show()