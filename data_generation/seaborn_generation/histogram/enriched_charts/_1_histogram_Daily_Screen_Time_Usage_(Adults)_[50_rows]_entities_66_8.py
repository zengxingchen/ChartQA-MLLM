
import seaborn as sns
import matplotlib.pyplot as plt

# Table data represented as a Python list for seaborn
temperature_data = [
    16, 17, 18, 19, 19, 20, 20, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23,
    23, 23, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 26, 26,
    26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 29, 29,
    29, 29, 30, 30, 30, 31, 31, 32
]

# Create the histogram
plt.figure(figsize=(10, 6))  # Change the width and height of the chart
sns.histplot(temperature_data, color="#3498db", binwidth=1)  # Change color and band width

# Set titles and labels
plt.title('Temperature Distribution in Celsius')
plt.xlabel('Temperature')
plt.ylabel('Frequency')

# Display the histogram
plt.show()