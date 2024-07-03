
import matplotlib.pyplot as plt

# The provided data
data = [
    {'Month': 'January', 'Mystery': '20%', 'Romance': '25%', 'Science Fiction': '15%', 'Non-Fiction': '25%', "Children's Literature": '15%'},
    {'Month': 'February', 'Mystery': '18%', 'Romance': '30%', 'Science Fiction': '12%', 'Non-Fiction': '22%', "Children's Literature": '18%'},
    {'Month': 'March', 'Mystery': '22%', 'Romance': '20%', 'Science Fiction': '18%', 'Non-Fiction': '24%', "Children's Literature": '16%'},
    {'Month': 'April', 'Mystery': '15%', 'Romance': '28%', 'Science Fiction': '15%', 'Non-Fiction': '27%', "Children's Literature": '15%'},
    {'Month': 'May', 'Mystery': '19%', 'Romance': '26%', 'Science Fiction': '16%', 'Non-Fiction': '23%', "Children's Literature": '16%'},
    {'Month': 'June', 'Mystery': '20%', 'Romance': '25%', 'Science Fiction': '20%', 'Non-Fiction': '20%', "Children's Literature": '15%'},
    {'Month': 'July', 'Mystery': '18%', 'Romance': '30%', 'Science Fiction': '17%', 'Non-Fiction': '20%', "Children's Literature": '15%'}
]

# Convert the percentage strings to float and stack them
months = [d['Month'] for d in data]
mystery_values = [float(d['Mystery'].strip('%')) for d in data]
romance_values = [float(d['Romance'].strip('%')) for d in data]
sf_values = [float(d['Science Fiction'].strip('%')) for d in data]
nf_values = [float(d['Non-Fiction'].strip('%')) for d in data]
children_values = [float(d["Children's Literature"].strip('%')) for d in data]

# Prepare the bottom values for stacking
romance_bottom = [m + r for m, r in zip(mystery_values, romance_values)]
sf_bottom = [r + s for r, s in zip(romance_bottom, sf_values)]
nf_bottom = [sf + nf for sf, nf in zip(sf_bottom, nf_values)]

# Colors and patterns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
patterns = ['/', '\\', '|', '-', '+']

fig, ax = plt.subplots(figsize=(10, 7))

# Plotting the bars
ax.bar(months, mystery_values, label='Mystery', color=colors[0], hatch=patterns[0])
ax.bar(months, romance_values, bottom=mystery_values, label='Romance', color=colors[1], hatch=patterns[1])
ax.bar(months, sf_values, bottom=romance_bottom, label='Science Fiction', color=colors[2], hatch=patterns[2])
ax.bar(months, nf_values, bottom=sf_bottom, label='Non-Fiction', color=colors[3], hatch=patterns[3])
ax.bar(months, children_values, bottom=nf_bottom, label="Children's Literature", color=colors[4], hatch=patterns[4])

# Adding the legend
ax.legend()

# Adding labels and title
ax.set_xlabel('Month')
ax.set_ylabel('Percentage')
ax.set_title('100% Stacked Bar Chart of Book Genres Over Time')

# Displaying the plot
plt.show()