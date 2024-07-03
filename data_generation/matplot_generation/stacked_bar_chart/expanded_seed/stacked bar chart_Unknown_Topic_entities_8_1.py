
import matplotlib.pyplot as plt

# Our chart table data
data = [
    {'Month': 'January', ' Bread Loaves': 320, ' Pastries': 150, ' Cakes': 90, ' Sandwiches': 200},
    {'Month': 'February', ' Bread Loaves': 280, ' Pastries': 120, ' Cakes': 110, ' Sandwiches': 190},
    {'Month': 'March', ' Bread Loaves': 300, ' Pastries': 130, ' Cakes': 95, ' Sandwiches': 210},
    {'Month': 'April', ' Bread Loaves': 310, ' Pastries': 145, ' Cakes': 105, ' Sandwiches': 205},
    {'Month': 'May', ' Bread Loaves': 325, ' Pastries': 160, ' Cakes': 120, ' Sandwiches': 220},
    {'Month': 'June', ' Bread Loaves': 340, ' Pastries': 175, ' Cakes': 130, ' Sandwiches': 230},
    {'Month': 'July', ' Bread Loaves': 360, ' Pastries': 190, ' Cakes': 140, ' Sandwiches': 240},
    {'Month': 'August', ' Bread Loaves': 355, ' Pastries': 185, ' Cakes': 135, ' Sandwiches': 235}
]

# Parsing the data for plotting
months = [d['Month'] for d in data]
bread = [d[' Bread Loaves'] for d in data]
pastries = [d[' Pastries'] for d in data]
cakes = [d[' Cakes'] for d in data]
sandwiches = [d[' Sandwiches'] for d in data]

# Define the width of the bars
bar_width = 0.5

# Define an index for the x-axis positions of the bars
index = range(len(months))

# Plotting the bars
plt.figure(figsize=(10, 7))

# Stack bread
plt.bar(index, bread, bar_width, label='Bread Loaves', color='brown')

# Stack pastries on top with previous cumulative sum
plt.bar(index, pastries, bar_width, bottom=bread, label='Pastries', color='yellow')

# Adding cakes atop bread+pastries
combined_cakes = [b + p for b, p in zip(bread, pastries)]
plt.bar(index, cakes, bar_width, bottom=combined_cakes, label='Cakes', color='pink')

# Adding sandwiches atop bread+pastries+cakes
combined_sandwiches = [b + p + c for b, p, c in zip(bread, pastries, cakes)]
plt.bar(index, sandwiches, bar_width, bottom=combined_sandwiches, label='Sandwiches', color='green')

# Labeling the chart
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.xticks(index, months, rotation=30)
plt.legend()

# Add values on top of each stack
for i in index:
    y_offset = 0
    for category in (bread, pastries, cakes, sandwiches):
        plt.text(i, y_offset + category[i]/2, str(category[i]), ha='center', va='center')
        y_offset += category[i]

# Display plot
plt.tight_layout()
plt.show()