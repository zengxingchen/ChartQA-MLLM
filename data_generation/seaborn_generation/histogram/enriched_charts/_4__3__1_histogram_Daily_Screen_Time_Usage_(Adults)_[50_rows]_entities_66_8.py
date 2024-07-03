
import seaborn as sns
import matplotlib.pyplot as plt

# Table data represented as a Python list for seaborn
star_brightness_data = [
    1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.3, 2.5, 2.7, 2.8, 2.9, 3.0, 
    3.1, 3.3, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.3, 4.5, 4.6, 4.7, 4.8, 5.0, 
    5.1, 5.3, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.2, 6.3, 6.5, 6.6, 6.8, 7.0, 7.1, 
    7.3, 7.5, 7.6, 7.8, 8.0, 8.1, 8.3, 8.5, 8.7, 8.8, 9.0, 9.1, 9.3, 9.5, 9.7, 
    9.8, 10.0, 10.2, 10.4, 10.6, 10.8, 11.0
]

# Create the histogram
plt.figure(figsize=(10, 14))  # Change the width and height of the chart
sns.histplot(star_brightness_data, color="#1f77b4", binwidth=0.5, orientation='vertical')  # Change color and bin width

# Set titles and labels
plt.title('Observed Star Brightness Distribution', fontsize=16)
plt.xlabel('Star Brightness (Magnitude)')
plt.ylabel('Frequency')

# Display the histogram
plt.show()