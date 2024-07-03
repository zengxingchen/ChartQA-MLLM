
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Category': ['Cryptocurrency', 'Stock Market', 'Real Estate', 'Mutual Funds', 'Bonds', 'Commodities', 
                 'Savings Accounts', 'Pension Funds', 'Insurance', 'Hedge Funds', 'Private Equity', 
                 'Venture Capital', 'Crowdfunding', 'Peer-to-Peer Lending', 'Foreign Exchange', 'Precious Metals'],
    'Amount': [300.4, 250.8, 200.3, 150.6, 120.9, 100.2, 80.5, 60.7, 50.8, 40.6, 30.4, 25.7, 20.3, 15.8, 10.2, 5.6]
}

df = pd.DataFrame(data)

# Color scheme picked to be distinct and visually appealing
colors = ['#FF4500', '#1E90FF', '#3CB371', '#FFD700', '#8A2BE2', 
          '#FF1493', '#7B68EE', '#32CD32', '#FF6347', '#00CED1', 
          '#ADFF2F', '#FF69B4', '#B22222', '#5F9EA0', '#FF7F50', '#20B2AA']

# Plotting the Treemap
plt.figure(figsize=(20, 12))  # Adjusted width and height
squarify.plot(sizes=df['Amount'], label=df['Category'], color=colors, alpha=0.8)
plt.title('Investment Distribution in Economics & Finance (in Millions USD)', fontsize=18)
plt.axis('off')
plt.show()