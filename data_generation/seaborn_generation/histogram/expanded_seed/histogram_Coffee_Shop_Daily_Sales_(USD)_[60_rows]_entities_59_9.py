
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chart table data provided
data = [
    {'Date': '01-Jan-2023', 'Sales': 157},
    {'Date': '02-Jan-2023', 'Sales': 123},
    {'Date': '03-Jan-2023', 'Sales': 165},
    {'Date': '04-Jan-2023', 'Sales': 189},
    {'Date': '05-Jan-2023', 'Sales': 210},
    {'Date': '06-Jan-2023', 'Sales': 198},
    {'Date': '07-Jan-2023', 'Sales': 175},
    {'Date': '08-Jan-2023', 'Sales': 160},
    {'Date': '09-Jan-2023', 'Sales': 190},
    {'Date': '10-Jan-2023', 'Sales': 220},
    {'Date': '11-Jan-2023', 'Sales': 230},
    {'Date': '12-Jan-2023', 'Sales': 225},
    {'Date': '13-Jan-2023', 'Sales': 208},
    {'Date': '14-Jan-2023', 'Sales': 170},
    {'Date': '15-Jan-2023', 'Sales': 130}
]

# Convert the chart table data into a pandas DataFrame
df = pd.DataFrame(data)

# Ensure the Date column is a datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Set a theme
sns.set_theme()

# Create the histogram for Sales data
plt.figure(figsize=(10, 6))
histplot = sns.histplot(
    data=df,
    x='Sales',
    bins=5, # Number of bins can be adjusted depending on data granularity
    kde=True, # Overlay a kernel density estimate to smooth the distribution
    color='blue', # Set histogram color
    edgecolor='black', # Color of the bin edges
    linewidth=1.5 # Width of the bin edges
)

# Additional visual encodings
histplot.set_title('Histogram of Sales Data')
histplot.set_xlabel('Sales Amount')
histplot.set_ylabel('Frequency')

# Customize the histogram appearance
plt.xticks(rotation=45) # Rotate x-axis labels if needed
plt.yticks(rotation=0)
plt.grid(True, which='both', linestyle='--', linewidth=0.5) # Enable grid with customization
plt.tight_layout()

# Show the plot
plt.show()