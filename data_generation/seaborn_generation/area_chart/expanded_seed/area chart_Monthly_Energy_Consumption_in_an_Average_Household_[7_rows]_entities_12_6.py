
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Month': 'January', 'Electricity (kWh)': 775},
    {'Month': 'February', 'Electricity (kWh)': 698},
    {'Month': 'March', 'Electricity (kWh)': 625},
    {'Month': 'April', 'Electricity (kWh)': 515},
    {'Month': 'May', 'Electricity (kWh)': 485},
    {'Month': 'June', 'Electricity (kWh)': 457},
    {'Month': 'July', 'Electricity (kWh)': 422},
    {'Month': 'August', 'Electricity (kWh)': 439},
    {'Month': 'September', 'Electricity (kWh)': 465},
    {'Month': 'October', 'Electricity (kWh)': 538},
    {'Month': 'November', 'Electricity (kWh)': 612},
    {'Month': 'December', 'Electricity (kWh)': 760}
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Create a categorical color palette
palette = sns.color_palette("flare", as_cmap=True)

# Create lineplot (Seaborn relplot is flexible and allows for creating line charts)
sns.set_style("whitegrid") # Set the seaborn style
lineplot = sns.relplot(data=df, x='Month', y='Electricity (kWh)', kind='line', aspect=2, height=5, palette=palette)

# Renaming for clarity
ax = lineplot.axes[0,0]

# Now fill the area under the plot line
ax.fill_between(x=df['Month'], y1=df['Electricity (kWh)'], alpha=0.3)

# Customize the ticks on x-axis for better readability
plt.xticks(rotation=45)

# Set the plot title and labels
ax.set_title('Monthly Electricity Usage (kWh)', fontsize=16)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Electricity (kWh)', fontsize=12)

# Remove the right and top spines
sns.despine()

# Show the plot
plt.show()