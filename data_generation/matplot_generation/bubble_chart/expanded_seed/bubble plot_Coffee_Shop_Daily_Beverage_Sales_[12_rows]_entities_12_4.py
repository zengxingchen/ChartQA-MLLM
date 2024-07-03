
import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Date': '2023-03-01', 'Time of Day': 'Morning', 'Location': 'Main St. Café', 'Beverage Type': 'Espresso', 'Sales': 75, 'Bubble Size (Customer Rating 1-5)': 4.2},
    # ... (other data records as provided)
    {'Date': '2023-03-02', 'Time of Day': 'Afternoon', 'Location': 'Lakeview Java', 'Beverage Type': 'Frappuccino', 'Sales': 90, 'Bubble Size (Customer Rating 1-5)': 4.8}
]

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(data)

# Create a new figure
plt.figure(figsize=(10, 6))

# Create a numeric index for x-axis to avoid overlapping
df['Time of Day'] = df['Time of Day'].map({'Morning': 1, 'Afternoon': 2})
df['Location'] = df['Location'].astype('category')
df['Location_codes'] = df['Location'].cat.codes

# Scatter plot with sales on the x-axis and bubble size representing customer rating
scatter = plt.scatter(
    x=df['Sales'], 
    y=df['Location_codes'],
    s=df['Bubble Size (Customer Rating 1-5)'] * 100,  # Multiply by 100 for better visibility
    c=df['Time of Day'],                             # Color code the time of day
    cmap='viridis',                                  # Color map
    alpha=0.6,                                       # Transparency of bubbles
    edgecolors='w',                                  # White edge color for better visibility
    linewidth=2                                      # Edge linewidth
)

# Convert the numeric labels back to their original values
plt.yticks(df['Location_codes'].unique(), df['Location'].unique())

# Add a color bar for the time of day
cbar = plt.colorbar(scatter)
cbar.set_label('Time of Day')
cbar.set_ticks([1, 2])
cbar.set_ticklabels(['Morning', 'Afternoon'])

# Set axis labels and chart title
plt.xlabel('Sales')
plt.ylabel('Location')
plt.title('Coffee Shop Sales Bubble Chart (Size indicates customer rating)')

# Show grid
plt.grid(True)

# Show plot
plt.show()