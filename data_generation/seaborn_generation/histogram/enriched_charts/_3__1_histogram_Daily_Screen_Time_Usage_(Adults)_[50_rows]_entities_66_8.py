
import seaborn as sns
import matplotlib.pyplot as plt

# Table data represented as a Python list for seaborn
steps_data = [
    3500, 4000, 4200, 4300, 4500, 4800, 5000, 5200, 5500, 5700, 5900, 
    6000, 6200, 6400, 6600, 6800, 7000, 7200, 7500, 7700, 8000, 8200, 
    8400, 8600, 8800, 9000, 9200, 9400, 9600, 9800, 10000, 10200, 10400, 
    10600, 10800, 11000, 11200, 11400, 11600, 11800, 12000, 12200, 12400, 
    12600, 12800, 13000, 13200, 13400, 13600, 13800, 14000, 14200, 14400, 
    14600, 14800, 15000
]

# Create the histogram
plt.figure(figsize=(12, 8))  # Change the width and height of the chart
sns.histplot(steps_data, color="#ff5733", binwidth=500, orientation='horizontal')  # Change color and bin width

# Set titles and labels
plt.title('Daily Steps Distribution')
plt.xlabel('Frequency')
plt.ylabel('Steps Walked Per Day')

# Display the histogram
plt.show()