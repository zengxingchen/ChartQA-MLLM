
import matplotlib.pyplot as plt

# Data from the chart table
data = [
    {'Day': 1, 'Sales($)': 230},
    {'Day': 2, 'Sales($)': 185},
    {'Day': 3, 'Sales($)': 205},
    {'Day': 4, 'Sales($)': 260},
    {'Day': 5, 'Sales($)': 270},
    {'Day': 6, 'Sales($)': 290},
    {'Day': 7, 'Sales($)': 310},
    {'Day': 8, 'Sales($)': 200},
    {'Day': 9, 'Sales($)': 190},
    {'Day': 10, 'Sales($)': 210},
    {'Day': 11, 'Sales($)': 230},
    {'Day': 12, 'Sales($)': 240},
    {'Day': 13, 'Sales($)': 250},
    {'Day': 14, 'Sales($)': 320},
    {'Day': 15, 'Sales($)': 190}
]

# Extract sales amounts for the histogram
sales = [entry['Sales($)'] for entry in data]

# Create the histogram
plt.figure(figsize=(10, 6)) # Set the size of the figure
n, bins, patches = plt.hist(sales, bins=5, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Sales($)')
plt.ylabel('Frequency')
plt.title('Histogram of Sales Over 15 Days')

# Set the ticks to match the sales ranges
plt.xticks(bins, labels=[f'${int(bin)}' for bin in bins])

# Add each bin frequency as a text label above the corresponding patch
for rect in patches:
    height = rect.get_height()
    plt.annotate(f'{int(height)}',
                 xy=(rect.get_x() + rect.get_width() / 2, height),
                 xytext=(0, 5),  # 5 points vertical offset
                 textcoords='offset points',
                 ha='center', va='bottom')

# Show the plot
plt.show()