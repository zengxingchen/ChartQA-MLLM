
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data for treemap
data = {
    'Sector': [
        'Banking', 'Insurance', 'Investment_Funds', 'Real_Estate', 'Fintech',
        'Pension_Funds', 'Private_Equity', 'Hedge_Funds', 'Microfinance', 'Crowdfunding',
        'Wealth_Management', 'Cryptocurrency'
    ],
    'Market_Share': [
        450, 300, 350, 280, 200,
        150, 180, 220, 120, 140,
        170, 130
    ]
}

# Convert the data into DataFrame
df = pd.DataFrame(data)

# Define color palette
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#9edae5', '#dbdb8d'
]

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(14, 10))

# Create a treemap
squarify.plot(sizes=df['Market_Share'], label=df['Sector'], alpha=0.8, color=colors)

# Remove the axes
plt.axis('off')

# Add a title
plt.title('Global Market Share of Financial Sectors', fontsize=18)

# Show the plot
plt.show()