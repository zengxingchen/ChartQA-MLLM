
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given table data as a list of dictionaries
data = [
    {'Library Name': 'Main Street Library', 'Month': 'January', 'Borrower Registrations': 150, 'Age Group': 'Adults', 'Major Category': 'Fiction', 'Borrowed Books (count)': 1200, 'Electronic Books Downloads': 350},
    {'Library Name': 'Pine Cone Library', 'Month': 'January', 'Borrower Registrations': 90, 'Age Group': 'Children', 'Major Category': 'Education', 'Borrowed Books (count)': 700, 'Electronic Books Downloads': 150},
    # ... (other data entries would go here)
    {'Library Name': 'Hilltop Library', 'Month': 'March', 'Borrower Registrations': 65, 'Age Group': 'Adults', 'Major Category': 'Non-Fiction', 'Borrowed Books (count)': 410, 'Electronic Books Downloads': 95}
]

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Start a figure
plt.figure(figsize=(10, 8))

# Create the bubble chart
bubble_chart = sns.scatterplot(
    data=df,
    x="Electronic Books Downloads",     # x-axis data
    y="Borrowed Books (count)",         # y-axis data
    size="Borrower Registrations",      # Bubble sizes reflect the number of registrations
    sizes=(50, 500),                    # Range of bubble sizes
    hue="Major Category",               # Color the points by the Major Category
    style="Age Group",                  # Different shapes for Age Groups
    palette="viridis",                  # Color palette
    alpha=0.7                           # Transparency of bubbles
)

# Adjust the legend for bubble sizes
bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Title and labels
plt.title('Library Data: Electronic Book Downloads vs. Borrowed Books')
plt.xlabel('Electronic Books Downloads')
plt.ylabel('Borrowed Books (Count)')

# Adjust layout for better fit
plt.tight_layout()

# Show the plot
plt.show()