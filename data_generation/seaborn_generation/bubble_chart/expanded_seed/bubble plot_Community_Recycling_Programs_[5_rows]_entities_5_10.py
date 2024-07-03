
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming the data has been loaded into a list of dictionaries called 'data':
data = [
    {'City': 'Metropolis', 'Year': 2022, 'Population (thousands)': 1830, 'Recycling Rate (%)': 67, 'Total Waste Recycled (thousand tons)': 1226},
    {'City': 'Coastville', 'Year': 2022, 'Population (thousands)': 760, 'Recycling Rate (%)': 59, 'Total Waste Recycled (thousand tons)': 448},
    {'City': 'Greenburg', 'Year': 2022, 'Population (thousands)': 480, 'Recycling Rate (%)': 74, 'Total Waste Recycled (thousand tons)': 355},
    {'City': 'Stonefield', 'Year': 2022, 'Population (thousands)': 295, 'Recycling Rate (%)': 62, 'Total Waste Recycled (thousand tons)': 183},
    {'City': 'Redtown', 'Year': 2022, 'Population (thousands)': 1250, 'Recycling Rate (%)': 70, 'Total Waste Recycled (thousand tons)': 875}
]

# Convert the list of dictionaries to a pandas DataFrame:
import pandas as pd
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(10, 6))

# Create a scatter plot, also known as a bubble chart in this context
bubble_chart = sns.scatterplot(
    data=df, 
    x="Population (thousands)", 
    y="Recycling Rate (%)", 
    size="Total Waste Recycled (thousand tons)", 
    sizes=(100, 2000), # Control the range of bubble sizes
    hue="City", 
    palette="deep", # Use a predefined seaborn color palette
    alpha=0.6, # Set transparency of the bubbles
    legend="full" # Display the legend fully
)

# Adjust the legend to avoid covering data points
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Add titles and labels
plt.title('Bubble Chart of Cities by Population, Recycling Rate, and Total Waste Recycled', fontsize=16)
plt.xlabel('Population (thousands)', fontsize=12)
plt.ylabel('Recycling Rate (%)', fontsize=12)
plt.grid(True) # Add a grid for better readability

# Show the plot
plt.show()