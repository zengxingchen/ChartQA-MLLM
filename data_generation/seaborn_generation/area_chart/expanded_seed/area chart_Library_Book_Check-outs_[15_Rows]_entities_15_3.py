
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data provided
data = [
    {'Date': '2023-01-01', 'Books Checked Out': 72},
    {'Date': '2023-01-02', 'Books Checked Out': 95},
    {'Date': '2023-01-03', 'Books Checked Out': 110},
    {'Date': '2023-01-04', 'Books Checked Out': 99},
    {'Date': '2023-01-05', 'Books Checked Out': 103},
    {'Date': '2023-01-06', 'Books Checked Out': 88},
    {'Date': '2023-01-07', 'Books Checked Out': 105},
    {'Date': '2023-01-08', 'Books Checked Out': 123},
    {'Date': '2023-01-09', 'Books Checked Out': 115},
    {'Date': '2023-01-10', 'Books Checked Out': 97},
    {'Date': '2023-01-11', 'Books Checked Out': 78},
    {'Date': '2023-01-12', 'Books Checked Out': 134},
    {'Date': '2023-01-13', 'Books Checked Out': 149},
    {'Date': '2023-01-14', 'Books Checked Out': 90},
    {'Date': '2023-01-15', 'Books Checked Out': 80}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Ensure 'Date' is a datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Set pretty Seaborn style
sns.set_theme(style="whitegrid")

# Plot
plt.figure(figsize=(12, 6))

# Fill the area under the line
plt.fill_between(x=df['Date'], y1=df['Books Checked Out'], alpha=0.3)

# Plot the line on top of the filled area
sns.lineplot(x=df['Date'], y=df['Books Checked Out'], sort=False, lw=1.5)

# Beautify the plot with Seaborn's despine
sns.despine()

# Additional customizations
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
plt.title('Books Checked Out Over Time')  # Add a title
plt.xlabel('Date')  # X-axis label
plt.ylabel('Books Checked Out')  # Y-axis label
plt.tight_layout()  # Fit the layout nicely in the figure

# Show the plot
plt.show()