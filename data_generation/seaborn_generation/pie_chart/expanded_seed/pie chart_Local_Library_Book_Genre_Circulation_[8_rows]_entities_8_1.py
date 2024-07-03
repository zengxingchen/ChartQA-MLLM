
import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data = [{'Genre': 'Mystery', 'Checkouts': 320},
        {'Genre': 'Science Fiction', 'Checkouts': 280},
        {'Genre': 'Romance', 'Checkouts': 450},
        {'Genre': 'Biographies', 'Checkouts': 300},
        {'Genre': "Children's Literature", 'Checkouts': 600},
        {'Genre': 'Young Adult', 'Checkouts': 400},
        {'Genre': 'Non-Fiction', 'Checkouts': 350},
        {'Genre': 'Classics', 'Checkouts': 200}]

# Converting the data into a format for plotting
genres = [entry['Genre'] for entry in data]
checkouts = [entry['Checkouts'] for entry in data]

# Seaborn style setting
sns.set(style="whitegrid")

# Create a color palette
colors = sns.color_palette('pastel')[0:len(data)]

# Create the pie chart using matplotlib
plt.figure(figsize=(10, 8))
plt.pie(checkouts, labels=genres, colors=colors, autopct='%1.1f%%', startangle=140)

# Customizing the pie chart to look better
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.title('Library Genre Checkout Distribution')

# Display the chart
plt.show()