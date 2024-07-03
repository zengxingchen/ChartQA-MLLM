
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given table data as a DataFrame
data = pd.DataFrame({
    'Temperature': [
        12, 15, 14, 10, 9, 13, 11, 16, 18, 17,
        19, 21, 20, 22, 21, 23, 25, 26, 24, 27,
        28, 29, 27, 30, 31, 29, 26, 25, 23, 22,
        24, 23, 22, 20, 19, 17, 16, 14, 13, 12
    ]
})

# Setting the style
sns.set(style='whitegrid')

# Changing the size of the plot
plt.figure(figsize=(10, 6))

# Creating the histogram
# Changing color scheme using hexadecimal color codes
# Changing the orientation to horizontal
# Adjusting the width of the bins
sns.histplot(data['Temperature'], color='#3498db', binwidth=1, binrange=(5,35), orientation='horizontal')

# Changing the chart title
plt.title('Distribution of Average Temperatures')

# Adjusting the labels
plt.xlabel('Frequency')
plt.ylabel('Average Temperature (°C)')

# Display the plot
plt.show()