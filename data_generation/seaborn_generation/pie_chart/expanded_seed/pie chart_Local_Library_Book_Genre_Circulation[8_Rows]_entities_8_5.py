
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame from the provided data
data = [
    {'Genre': 'Mystery', 'Checkout Count': 340},
    {'Genre': 'Science Fiction', 'Checkout Count': 289},
    {'Genre': 'Romance', 'Checkout Count': 425},
    {'Genre': 'Biographies', 'Checkout Count': 123},
    {'Genre': 'History', 'Checkout Count': 210},
    {'Genre': "Children's Books", 'Checkout Count': 391},
    {'Genre': 'Self-help', 'Checkout Count': 95},
    {'Genre': 'Graphic Novels', 'Checkout Count': 179}
]

df = pd.DataFrame(data)

# Set up the matplotlib figure
plt.figure(figsize=(10, 6))

# Use the 'Spectral' color palette from seaborn
colors = sns.color_palette('Spectral', len(df))

# Plot the pie chart
plt.pie(df['Checkout Count'], labels=df['Genre'], colors=colors, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that the pie is drawn as a circle
plt.axis('equal')

# Title of the pie chart
plt.title('Checkout Count by Genre')

# Show the plot
plt.show()