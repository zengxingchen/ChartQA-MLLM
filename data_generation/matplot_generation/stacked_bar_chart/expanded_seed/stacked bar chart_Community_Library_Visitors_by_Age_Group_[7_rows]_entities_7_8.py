
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Month': 'January', 'Children (0-12)': 145, 'Teenagers (13-18)': 80, 'Adults (19-64)': 200, 'Seniors (65+)': 120},
    {'Month': 'February', 'Children (0-12)': 110, 'Teenagers (13-18)': 65, 'Adults (19-64)': 180, 'Seniors (65+)': 115},
    {'Month': 'March', 'Children (0-12)': 160, 'Teenagers (13-18)': 85, 'Adults (19-64)': 210, 'Seniors (65+)': 130},
    {'Month': 'April', 'Children (0-12)': 130, 'Teenagers (13-18)': 75, 'Adults (19-64)': 190, 'Seniors (65+)': 140},
    {'Month': 'May', 'Children (0-12)': 150, 'Teenagers (13-18)': 80, 'Adults (19-64)': 220, 'Seniors (65+)': 130},
    {'Month': 'June', 'Children (0-12)': 140, 'Teenagers (13-18)': 70, 'Adults (19-64)': 210, 'Seniors (65+)': 120},
    {'Month': 'July', 'Children (0-12)': 165, 'Teenagers (13-18)': 90, 'Adults (19-64)': 230, 'Seniors (65+)': 125}
]

# Prepare lists for the plot
months = [entry['Month'] for entry in data]
children_values = [entry['Children (0-12)'] for entry in data]
teenagers_values = [entry['Teenagers (13-18)'] for entry in data]
adults_values = [entry['Adults (19-64)'] for entry in data]
seniors_values = [entry['Seniors (65+)'] for entry in data]

# Numbers of pairs of bars you want
N = len(data)

# Position of bars on x-axis
ind = range(N)

# Figure size
plt.figure(figsize=(10, 7))

# Make the plot
p1 = plt.bar(ind, children_values, color='skyblue')
p2 = plt.bar(ind, teenagers_values, bottom=children_values, color='lightgreen')
p3 = plt.bar(ind, adults_values, bottom=[i+j for i,j in zip(children_values, teenagers_values)], color='salmon')
p4 = plt.bar(ind, seniors_values, bottom=[i+j+k for i,j,k in zip(children_values, teenagers_values, adults_values)], color='slateblue')

# Adding Xticks
plt.xlabel('Months', fontsize=12)
plt.ylabel('Number of People', fontsize=12)
plt.xticks(ind, months)
plt.yticks(range(0, 501, 50))

# Add legend
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Children (0-12)', 'Teenagers (13-18)', 'Adults (19-64)', 'Seniors (65+)'), loc='upper left')

# Show plot
plt.show()