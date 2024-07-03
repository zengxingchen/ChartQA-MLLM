
import matplotlib.pyplot as plt
import seaborn as sns

# Data provided
data = [
    {'Genre': 'Mystery', 'Percentage of Total Checkouts': '22%'},
    {'Genre': 'Science Fiction', 'Percentage of Total Checkouts': '18%'},
    {'Genre': 'Romance', 'Percentage of Total Checkouts': '16%'},
    {'Genre': 'Biographies', 'Percentage of Total Checkouts': '14%'},
    {'Genre': "Children's Literature", 'Percentage of Total Checkouts': '12%'},
    {'Genre': 'Historical Fiction', 'Percentage of Total Checkouts': '10%'},
    {'Genre': 'Self-help', 'Percentage of Total Checkouts': '8%'}
]

# Prepare the data for matplotlib
labels = [item['Genre'] for item in data]
sizes = [int(item['Percentage of Total Checkouts'].strip('%')) for item in data]
colors = sns.color_palette('pastel', len(labels))  # Use seaborn color palette

# Seaborn style
sns.set(style="whitegrid")  # You can choose other styles: darkgrid, whitegrid, dark, white, and ticks

# Create the pie chart
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85)

# Draw a circle at the center to turn the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Title of the pie chart
plt.title('Genre Distribution of Total Checkouts', pad=20)

# Render the plot
plt.show()