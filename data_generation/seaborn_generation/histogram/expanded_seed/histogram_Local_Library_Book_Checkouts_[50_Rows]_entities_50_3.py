
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = [
    {'Month': 'January', 'Checkouts': 450},
    {'Month': 'January', 'Checkouts': 375},
    {'Month': 'January', 'Checkouts': 320},
    {'Month': 'February', 'Checkouts': 290},
    {'Month': 'February', 'Checkouts': 310},
    {'Month': 'February', 'Checkouts': 250},
    {'Month': 'March', 'Checkouts': 400},
    {'Month': 'March', 'Checkouts': 420},
    {'Month': 'March', 'Checkouts': 380},
    {'Month': 'April', 'Checkouts': 360},
    {'Month': 'April', 'Checkouts': 335},
    {'Month': 'April', 'Checkouts': 340},
    {'Month': 'May', 'Checkouts': 500},
    {'Month': 'May', 'Checkouts': 475},
    {'Month': 'May', 'Checkouts': 520},
]

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Set the style and palette of the plot
sns.set_style("whitegrid")
sns.set_palette("pastel")

# Create the histogram
plt.figure(figsize=(10, 6)) # Set the figure size
sns.histplot(
    data=df,
    x='Checkouts', # Set the variable for the x-axis
    bins=10, # Define the number of bins in the histogram
    kde=True, # Plot the kernel density estimate
    hue='Month', # Color the bars by month
    element="step", # Use step-filled histogram
    cumulative=False, # Do not make it cumulative
)

# Additional customizations
plt.title('Checkouts Histogram by Month') # Add a title to the plot
plt.xlabel('Number of Checkouts') # Label the x-axis
plt.ylabel('Frequency') # Label the y-axis

# Show the plot
plt.show()