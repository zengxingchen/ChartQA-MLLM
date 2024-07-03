
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chart table data
data = [
    {'Year': 2019, 'Plastic (tons)': 120, 'Paper (tons)': 250, 'Glass (tons)': 75, 'Metal (tons)': 50},
    {'Year': 2020, 'Plastic (tons)': 135, 'Paper (tons)': 270, 'Glass (tons)': 80, 'Metal (tons)': 65},
    {'Year': 2021, 'Plastic (tons)': 150, 'Paper (tons)': 300, 'Glass (tons)': 85, 'Metal (tons)': 70},
    {'Year': 2022, 'Plastic (tons)': 160, 'Paper (tons)': 320, 'Glass (tons)': 90, 'Metal (tons)': 80},
    {'Year': 2023, 'Plastic (tons)': 175, 'Paper (tons)': 340, 'Glass (tons)': 95, 'Metal (tons)': 90}
]

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Set the style of seaborn
sns.set_style('whitegrid')

# Prepare data for the stacked area chart
x = df['Year']
y = [df['Plastic (tons)'], df['Paper (tons)'], df['Glass (tons)'], df['Metal (tons)']]

# Set the figure size and create a color palette
plt.figure(figsize=(10, 7))
colors = sns.color_palette('pastel', len(y))

# Plot the stacked area chart
plt.stackplot(x, y, labels=['Plastic', 'Paper', 'Glass', 'Metal'], colors=colors, alpha=0.8)

# Adding the aesthetics
plt.title('Waste materials collected over years (in tons)')
plt.xlabel('Year')
plt.ylabel('Material (tons)')

# Add legend to the plot
plt.legend(loc='upper left')

# Display the plot
plt.show()