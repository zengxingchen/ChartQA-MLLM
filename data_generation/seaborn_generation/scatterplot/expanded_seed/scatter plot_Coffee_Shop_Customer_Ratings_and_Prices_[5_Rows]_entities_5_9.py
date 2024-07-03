
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Provided table data
data = [
    {'Customer Rating (out of 5)': 4.2, 'Price per Coffee (USD)': 3.5},
    {'Customer Rating (out of 5)': 3.8, 'Price per Coffee (USD)': 2.95},
    {'Customer Rating (out of 5)': 4.7, 'Price per Coffee (USD)': 4.2},
    {'Customer Rating (out of 5)': 4.0, 'Price per Coffee (USD)': 3.0},
    {'Customer Rating (out of 5)': 3.5, 'Price per Coffee (USD)': 2.75}
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Create the scatterplot
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    x='Price per Coffee (USD)',
    y='Customer Rating (out of 5)',
    data=df,
    palette='deep',        # you may choose a different color palette
    s=100,                 # size of the markers can be adjusted
    style='Customer Rating (out of 5)',  # optional: map the customer rating to different marker styles
    markers={'Customer Rating (out of 5)': 'o'},  # using circular markers, but other shapes are available
    legend='full'
)

# Optional: you may add title and labels for clarity
plt.title('Customer Rating vs. Price per Coffee')
plt.xlabel('Price per Coffee (USD)')
plt.ylabel('Customer Rating (out of 5)')

# Show the plot
plt.show()