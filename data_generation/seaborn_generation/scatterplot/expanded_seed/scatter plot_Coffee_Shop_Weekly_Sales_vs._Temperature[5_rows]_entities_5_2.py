
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Provided data
data = [
    {'Day': 'Monday', 'Temperature (°C)': 20, 'Sales ($)': 350},
    {'Day': 'Tuesday', 'Temperature (°C)': 22, 'Sales ($)': 420},
    {'Day': 'Wednesday', 'Temperature (°C)': 18, 'Sales ($)': 390},
    {'Day': 'Thursday', 'Temperature (°C)': 24, 'Sales ($)': 460},
    {'Day': 'Friday', 'Temperature (°C)': 25, 'Sales ($)': 500}
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Create a scatterplot using Seaborn
sns.set_theme()  # Set the theme for aesthetics
plt.figure(figsize=(10, 6))  # Set the figure size

# Scatterplot with diversified visual encoding
scatterplot = sns.scatterplot(
    x='Temperature (°C)',      # X-axis data
    y='Sales ($)',             # Y-axis data
    hue='Day',                 # Color by day of the week
    size='Sales ($)',          # Size by sales
    style='Day',               # Different marker style for each day
    palette='viridis',         # Color palette used
    sizes=(100, 400),          # Range of sizes for the sizes encoding
    data=df                    # Data source
)

# Additional customizations
plt.title('Sales ($) vs Temperature (°C) by Day of the Week')  # Set title
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')         # Legend outside plot

# Show the plot
plt.show()