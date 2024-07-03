
import matplotlib.pyplot as plt

# Given data in list of dictionaries format
data = [
    {'Month': 'January', ' Cups of Coffee': 232}, 
    {'Month': 'February', ' Cups of Coffee': 218},
    {'Month': 'March', ' Cups of Coffee': 321},
    {'Month': 'April', ' Cups of Coffee': 349},
    {'Month': 'May', ' Cups of Coffee': 291},
    {'Month': 'June', ' Cups of Coffee': 280},
    {'Month': 'July', ' Cups of Coffee': 270},
    {'Month': 'August', ' Cups of Coffee': 256},
    {'Month': 'September', ' Cups of Coffee': 389},
    {'Month': 'October', ' Cups of Coffee': 406},
    {'Month': 'November', ' Cups of Coffee': 450},
    {'Month': 'December', ' Cups of Coffee': 479},
    {'Month': 'January', ' Cups of Coffee': 241},
    {'Month': 'February', ' Cups of Coffee': 230},
    {'Month': 'March', ' Cups of Coffee': 336}
]

# Extracting just the 'Cups of Coffee' values
coffee_values = [entry[' Cups of Coffee'] for entry in data]

# Creating the histogram with diversified visual encoding
plt.figure(figsize=(10, 6)) # Set the figure size

# Plot histogram with custom bin size, color and edge color
n, bins, patches = plt.hist(coffee_values, bins=15, color='skyblue', edgecolor='black')

# Adding a title and labels
plt.title('Distribution of Cups of Coffee Consumed per Month', fontsize=15)
plt.xlabel('Cups of Coffee', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Adding Grid to the plot
plt.grid(axis='y', alpha=0.75)

# Customize the tick labels if needed
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Optionally, you can label the bars with their count
for i in range(len(patches)):
    plt.text(patches[i].xy[0], patches[i].get_height()+0.5, str(int(n[i])), fontsize=8, ha='center')

# Show the plot
plt.show()