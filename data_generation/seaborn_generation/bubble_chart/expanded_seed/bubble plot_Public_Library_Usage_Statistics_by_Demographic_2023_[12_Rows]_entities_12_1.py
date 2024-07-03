
import seaborn as sns
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Age Group': '0-12', 'Number of Patrons': 320, 'Books Checked Out': 1200, 'Visits per Month': 3.0, 'Electronic Resources Downloads': 500},
    {'Age Group': '13-18', 'Number of Patrons': 410, 'Books Checked Out': 900, 'Visits per Month': 2.5, 'Electronic Resources Downloads': 700},
    {'Age Group': '19-25', 'Number of Patrons': 570, 'Books Checked Out': 800, 'Visits per Month': 1.8, 'Electronic Resources Downloads': 950},
    {'Age Group': '26-35', 'Number of Patrons': 630, 'Books Checked Out': 950, 'Visits per Month': 1.5, 'Electronic Resources Downloads': 1100},
    # Rest of your data goes here...
    {'Age Group': 'Teachers', 'Number of Patrons': 65, 'Books Checked Out': 300, 'Visits per Month': 3.0, 'Electronic Resources Downloads': 220},
    {'Age Group': 'Researchers', 'Number of Patrons': 45, 'Books Checked Out': 150, 'Visits per Month': 2.0, 'Electronic Resources Downloads': 300}
]

# Convert data to a pandas DataFrame for use with seaborn
import pandas as pd
df = pd.DataFrame(data)

# Define the bubble size scale, you can adjust this as needed
bubble_scale = 100

# Create a bubble chart
plt.figure(figsize=(12, 8))
bubble_chart = sns.scatterplot(
    data=df,
    x='Number of Patrons',
    y='Books Checked Out',
    size='Visits per Month',
    sizes=(20, 200), # Range of bubble sizes
    hue='Electronic Resources Downloads',
    palette='coolwarm', # Color spectrum variation
    alpha=0.6,  # Transparency of bubbles
    legend='full' # Include legend for sizes and colors
)

# Customizing the plot further as required
bubble_chart.set_title('Library Usage Statistics by Age Group', fontsize=16)
bubble_chart.set_xlabel('Number of Patrons', fontsize=14)
bubble_chart.set_ylabel('Books Checked Out', fontsize=14)
plt.legend(title='Visits per Month & Downloads', bbox_to_anchor=(1, 1), loc=2)

# To ensure the legend for sizes is visible and not cut off
plt.tight_layout()

# Show the plot
plt.show()