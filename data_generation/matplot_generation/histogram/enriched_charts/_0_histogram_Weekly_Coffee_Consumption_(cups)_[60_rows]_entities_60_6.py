
import matplotlib.pyplot as plt

# Assuming data_points is a list obtained from the above table's 'Books_Read' column
data_points = [
    5, 8, 12, 18, 22, 25, 18, 30, 34, 37,
    15, 20, 25, 28, 14, 21, 29, 33, 36, 41,
    9, 16, 24, 31, 3, 7, 13, 20, 35, 23,
    27, 11, 17, 26, 4, 19, 32, 38, 42, 44,
    45, 47, 2, 6, 10
]

plt.figure(figsize=(12, 8))  # Change the width and height of the chart
plt.hist(
    data_points,
    bins=10,  # Change the band width/height for histograms
    orientation='horizontal',  # Change the direction of chart
    color='#007acc',  # Modify the color scheme
    edgecolor='#000000',  # Adding an edge color for clarity
    alpha=0.7,  # Making histogram slightly transparent
    rwidth=0.9  # Change width of histograms
)

plt.title('Distribution of Books Read in a Year')
plt.xlabel('Frequency')
plt.ylabel('Number of Books Read')
plt.grid(axis='y', alpha=0.75)  # Adding a grid on the y-axis

plt.show()