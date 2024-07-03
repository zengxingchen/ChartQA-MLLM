
import matplotlib.pyplot as plt

# Given table data as a list of ages
ages = [
    23, 27, 25, 30, 35, 30, 39, 40, 44, 50, 30, 32, 60, 55, 46, 43, 39, 58,
    63, 65, 70, 34, 31, 29, 47, 49, 52, 45, 40, 37, 36, 33, 48, 53, 38, 41,
    42, 51, 54, 57, 59, 62, 50, 56, 43
]

# Binning the data
bins = [20, 30, 40, 50, 60, 70, 80]

# Plotting the histogram with given specifications
plt.figure(figsize=(10, 6)) # Width and height of the chart
plt.hist(ages, bins=bins, color='#7E57C2', edgecolor='black', linewidth=1.2, orientation='horizontal')

# Adding some chart elements
plt.title('Distribution of Ages in a Community')
plt.xlabel('Frequency')
plt.ylabel('Ages')

# Changing the band height for the histograms
plt.yticks([25, 35, 45, 55, 65, 75])

# Show plot
plt.show()