
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Category': ['Cryptocurrency', 'Stock Market', 'Real Estate', 'Mutual Funds', 'Bonds', 'Commodities', 
                 'Savings Accounts', 'Pension Funds', 'Insurance', 'Hedge Funds', 'Private Equity', 
                 'Venture Capital', 'Crowdfunding', 'Peer-to-Peer Lending', 'Foreign Exchange', 'Precious Metals',
                 'Space Exploration', 'Environmental Conservation', 'Technology Startups', 'Renewable Energy', 
                 'Healthcare Innovations', 'Education Funding', 'Artificial Intelligence', 'Global Connectivity', 
                 'Climate Change Mitigation'],
    'Amount': [320.5, 280.9, 210.7, 160.4, 130.8, 105.6, 85.3, 70.9, 55.7, 45.8, 35.6, 28.9, 23.4, 18.5, 12.3, 6.7, 
               50.1, 42.5, 95.4, 78.9, 60.2, 37.1, 29.3, 17.6, 11.8]
}

df = pd.DataFrame(data)

# Color scheme picked to be distinct and visually appealing
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8C33', 
          '#33FFF8', '#F833FF', '#57FF33', '#FF5733', '#FF3388', 
          '#8833FF', '#33FFBB', '#FF3357', '#33AAFF', '#FF3388', 
          '#AA33FF', '#33FF44', '#FF3344', '#4433FF', '#FF8833', 
          '#FF33CC', '#33CCFF', '#FFCC33', '#33FFDD', '#FF33DD']

# Plotting the Treemap
plt.figure(figsize=(24, 14))  # Adjusted width and height
squarify.plot(sizes=df['Amount'], label=df['Category'], color=colors, alpha=0.8)
plt.title('Investment in Future Technologies & Society (in Millions USD)', fontsize=18, y=1.05)
plt.axis('off')
plt.show()