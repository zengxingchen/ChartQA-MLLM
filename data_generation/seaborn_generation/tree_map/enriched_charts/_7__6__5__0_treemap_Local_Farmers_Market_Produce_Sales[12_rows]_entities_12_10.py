
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the data
data = {
    'Category': [
        'Stock Market', 'Cryptocurrency', 'Real Estate', 'Insurance', 
        'Banking', 'Hedge Funds', 'Mutual Funds', 'Private Equity', 
        'Venture Capital', 'Commodities', 'Foreign Exchange', 'Bonds', 
        'Fintech', 'Investment Banking'
    ],
    'Value': [
        1500, 950, 1300, 850, 1200, 780, 920, 670, 750, 600, 1100, 880, 760, 890
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color palette
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA5', '#FFA533', 
    '#A533FF', '#FF8F33', '#33FFF7', '#FF3333', '#33FF33', '#5733FF', 
    '#FF333F', '#33FF4F'
]

# Define size of the figure
plt.figure(figsize=(18, 10))

# Plot the treemap with the specified colors and data
squarify.plot(sizes=df['Value'], label=df['Category'], color=colors, alpha=0.8)

plt.title('Key Sectors in Economics & Finance by Market Value (in Millions)', fontsize=22)
plt.axis('off')
plt.show()