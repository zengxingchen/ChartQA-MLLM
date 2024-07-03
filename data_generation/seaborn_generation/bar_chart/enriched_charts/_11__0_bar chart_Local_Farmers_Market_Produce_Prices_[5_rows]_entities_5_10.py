
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given dataset
data = {
    'Genre': ['Rock', 'Pop', 'Hip-Hop', 'Classical', 'Jazz', 'Electronic', 'Country', 'Reggae', 'Blues', 'Metal'],
    'Average Ticket Price (USD)': [120, 110, 95, 75, 85, 100, 90, 80, 70, 105]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize a Matplotlib figure and set its size
plt.figure(figsize=(12, 6))

# Create vertical bar chart
sns.barplot(
    x='Genre',
    y='Average Ticket Price (USD)',
    data=df,
    palette=[
        '#FF5733', '#C70039', '#900C3F', '#571845', '#2E86C1',
        '#1F618D', '#3498DB', '#AED6F1', '#5DADE2', '#2874A6'
    ]
)

# Customize the chart
plt.title('Average Ticket Prices for Concerts by Genre', fontsize=16, pad=20)
plt.xlabel('Genre', fontsize=14)
plt.ylabel('Average Ticket Price (USD)', fontsize=14)

# Adjust the width of the bars
for patch in plt.gca().patches:
    patch.set_width(0.5)

# Show the plot
plt.show()