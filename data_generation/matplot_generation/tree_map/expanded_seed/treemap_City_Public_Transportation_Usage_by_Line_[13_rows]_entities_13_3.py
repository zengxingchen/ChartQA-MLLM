
import matplotlib.pyplot as plt
import squarify

# Your data
chart_data = [
    {'Line': 'Blue Line', 'Passenger Count (Daily)': 12000, 'Length (miles)': 22, 'Areas Covered': 'Downtown to Suburbs'},
    #... include all other lines here
    {'Line': 'Cyan Line', 'Passenger Count (Daily)': 6000, 'Length (miles)': 11, 'Areas Covered': 'Shopping Centers to Housing Estates'}
]

# Create lists of sizes and labels based on the passenger count, and a list of colors based on the length
sizes = [data['Passenger Count (Daily)'] for data in chart_data]
labels = [f"{data['Line']}\n({data['Passenger Count (Daily)']} passengers)" for data in chart_data]
lengths = [data['Length (miles)'] for data in chart_data]

# Normalize the lengths to a suitable color range
max_length = max(lengths)
min_length = min(lengths)
colors = [(length - min_length) / (max_length - min_length) for length in lengths]

# Create a color map
cmap = plt.cm.Blues
normed_colors = [cmap(color) for color in colors]

# Create a figure
plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=sizes, label=labels, color=normed_colors, alpha=.7)

# Add title and remove axes
plt.title("Treemap of Passenger Counts")
plt.axis('off')

# Show plot
plt.show()