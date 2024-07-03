
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data = [
    {'Year': 2010, 'Standard Package Subscribers (Mbps<100)': 1500, 'Enhanced Package Subscribers (100<=Mbps<300)': 300, 'Premium Package Subscribers (Mbps>=300)': 50, 'Average Speed (Mbps)': 45},
    {'Year': 2011, 'Standard Package Subscribers (Mbps<100)': 1480, 'Enhanced Package Subscribers (100<=Mbps<300)': 320, 'Premium Package Subscribers (Mbps>=300)': 70, 'Average Speed (Mbps)': 50},
    # Add all the other data points...
    {'Year': 2021, 'Standard Package Subscribers (Mbps<100)': 500, 'Enhanced Package Subscribers (100<=Mbps<300)': 800, 'Premium Package Subscribers (Mbps>=300)': 600, 'Average Speed (Mbps)': 130}
]

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Set the style
sns.set_style("whitegrid")

# Create stackplot
plt.figure(figsize=(10, 6))
plt.stackplot(df['Year'],
              [df['Standard Package Subscribers (Mbps<100)'],
               df['Enhanced Package Subscribers (100<=Mbps<300)'],
               df['Premium Package Subscribers (Mbps>=300)']],
              labels=['Standard Package', 'Enhanced Package', 'Premium Package'],
              colors=sns.color_palette("hls", 3),
              alpha=0.8)

# Add titles and labels
plt.title('Subscribers over the years by Package type', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Subscribers', fontsize=12)

# Move the legend out of the plot
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Package Type")

# Annotate average speed
for x, y, label in zip(df['Year'], df['Average Speed (Mbps)'], df['Average Speed (Mbps)']):
    plt.text(x, y, f'{label} Mbps', fontsize=9, verticalalignment='bottom')

sns.despine()  # Remove the top and right spines from plot

# Show plot
plt.tight_layout()
plt.show()