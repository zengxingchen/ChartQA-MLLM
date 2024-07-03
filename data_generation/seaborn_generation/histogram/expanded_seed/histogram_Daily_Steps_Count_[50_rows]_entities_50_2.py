
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Convert the list of dictionaries into a pandas DataFrame
data = [
    {'PersonID': 1, 'Daily Steps': 3450},
    {'PersonID': 2, 'Daily Steps': 6891},
    {'PersonID': 3, 'Daily Steps': 5122},
    {'PersonID': 4, 'Daily Steps': 8089},
    {'PersonID': 5, 'Daily Steps': 10045},
    {'PersonID': 6, 'Daily Steps': 3221},
    {'PersonID': 7, 'Daily Steps': 4022},
    {'PersonID': 8, 'Daily Steps': 6891},
    {'PersonID': 9, 'Daily Steps': 7900},
    {'PersonID': 10, 'Daily Steps': 9780},
    {'PersonID': 11, 'Daily Steps': 11021},
    {'PersonID': 12, 'Daily Steps': 12090},
    {'PersonID': 13, 'Daily Steps': 4012},
    {'PersonID': 14, 'Daily Steps': 9543},
    {'PersonID': 15, 'Daily Steps': 7230}
]
df = pd.DataFrame(data)

# Set the style and color palette of the Seaborn plot
sns.set(style="whitegrid")
sns.set_palette("pastel")

# Create a histogram using Seaborn's histplot
plt.figure(figsize=(10, 6))  # Set the size of the figure
hist = sns.histplot(
    df['Daily Steps'],
    bins=8,  # Choose the number of bins
    kde=True,  # Add a Kernel Density Estimate plot
    color="skyblue",  # Set the color of the bars
    edgecolor="gray",  # Set the color of the border of the bars
    linewidth=1.5  # Set the linewidth of the border
)

# Additional customization for the plot
hist.set_title("Histogram of Daily Steps", fontsize=16)  # Title of the histogram
hist.set_xlabel("Daily Steps", fontsize=14)  # X-axis label
hist.set_ylabel("Frequency", fontsize=14)  # Y-axis label

# Show the plot
plt.show()