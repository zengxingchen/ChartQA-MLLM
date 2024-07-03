
import matplotlib.pyplot as plt

# Data provided in the form of list of dictionaries
data_dicts = [
    {'Data Usage (GB)': 245}, {'Data Usage (GB)': 320}, {'Data Usage (GB)': 389},
    {'Data Usage (GB)': 280}, {'Data Usage (GB)': 435}, {'Data Usage (GB)': 410},
    {'Data Usage (GB)': 275}, {'Data Usage (GB)': 350}, {'Data Usage (GB)': 300},
    {'Data Usage (GB)': 265}, {'Data Usage (GB)': 488}, {'Data Usage (GB)': 290},
    {'Data Usage (GB)': 375}, {'Data Usage (GB)': 260}, {'Data Usage (GB)': 215}
]

# Extracting 'Data Usage (GB)' values from each dictionary and creating a list
data_usage = [d['Data Usage (GB)'] for d in data_dicts]

# Setting up the figure and axis
plt.figure(figsize=(10, 6))

# Creating the histogram
n, bins, patches = plt.hist(data_usage, bins=8, color='skyblue', edgecolor='black')

# Customizing the histogram with labels, title, and grid
plt.xlabel('Data Usage (GB)')
plt.ylabel('Frequency')
plt.title('Histogram of Data Usage')
plt.grid(axis='y', alpha=0.75)

# Adding a mean line
mean_usage = sum(data_usage) / len(data_usage)
plt.axvline(mean_usage, color='red', linestyle='dashed', linewidth=1)
plt.text(mean_usage + 5, max(n)/2, f'Mean: {mean_usage:.2f} GB', color = 'red')

# Display the histogram
plt.show()