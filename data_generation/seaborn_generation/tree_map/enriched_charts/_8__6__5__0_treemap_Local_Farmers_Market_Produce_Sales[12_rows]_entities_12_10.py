
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the data
data = {
    'Topic': [
        'Investment Banking', 'Stock Market Analysis', 'Venture Capital', 
        'Cryptocurrency', 'Real Estate', 'Private Equity', 
        'Insurance', 'Personal Finance', 'Economic Policy', 
        'Taxation', 'Corporate Finance', 'Financial Technology', 
        'Wealth Management', 'Commodities Trading', 'Debt Management', 
        'Derivatives Market', 'Risk Management', 'Mergers and Acquisitions', 
        'Pension Funds', 'Financial Planning', 'Auditing', 'Accounting'
    ],
    'Value': [
        1500, 1200, 1100, 950, 890, 760, 710, 670, 650, 
        630, 620, 600, 590, 580, 570, 550, 540, 530, 
        520, 510, 500, 490
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color palette
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', 
    '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', 
    '#dbdb8d', '#9edae5', '#393b79', '#637939'
]

# Define size of the figure
plt.figure(figsize=(18, 10))

# Plot the treemap with the specified colors and data
squarify.plot(sizes=df['Value'], label=df['Topic'], color=colors, alpha=0.8)

plt.title('Prominent Economic and Financial Sectors by Market Value (in Millions)', fontsize=20)
plt.axis('off')
plt.show()