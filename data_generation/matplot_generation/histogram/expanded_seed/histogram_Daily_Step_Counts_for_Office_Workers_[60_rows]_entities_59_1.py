
import matplotlib.pyplot as plt

# Provided data in a list of dictionaries
data = [
    {'Steps Count': 10234}, {'Steps Count': 8905}, {'Steps Count': 11567},
    {'Steps Count': 9765}, {'Steps Count': 7922}, {'Steps Count': 8281},
    {'Steps Count': 9054}, {'Steps Count': 10876}, {'Steps Count': 9678},
    {'Steps Count': 7564}, {'Steps Count': 11532}, {'Steps Count': 9856},
    {'Steps Count': 7633}, {'Steps Count': 10456}, {'Steps Count': 8732}
]

# Extracting the steps count into a list for plotting
steps_counts = [entry['Steps Count'] for entry in data]

# Plotting the histogram
plt.figure(figsize=(10, 6)) # setting the size of the plot

# Creating the histogram with diversified visual encoding
n, bins, patches = plt.hist(steps_counts, bins=5, color='skyblue', edgecolor='black')

# Highlighting the maximum bin
max_bin = max(n)
max_bin_index = list(n).index(max_bin)
patches[max_bin_index].set_fc('tomato')  # Changing fill color
patches[max_bin_index].set_edgecolor('darkred')  # Changing edge color
patches[max_bin_index].set_linewidth(1.5)  # Changing line width
patches[max_bin_index].set_alpha(0.7)  # Changing transparency

# Adding additional visual elements for clarity and aesthetics
plt.title('Histogram of Steps Count', fontsize=18)
plt.xlabel('Steps Count', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True, which='major', linestyle='--', linewidth=0.5)
plt.axvline(x=sum(steps_counts)/len(steps_counts), color='deeppink', linestyle='dashed', linewidth=2, label='Average')
plt.legend()

# Annotating the average line
average_steps = sum(steps_counts) / len(steps_counts)
plt.text(average_steps + 300, max_bin - 0.1 * max_bin, f'Average: {average_steps:.2f}', color='deeppink')

# Adding text to the bars
for count, rect in zip(n, patches):
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2., height, f'{int(count)}', ha='center', va='bottom')

# Show the plot
plt.show()