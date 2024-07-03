
import matplotlib.pyplot as plt
import squarify

# Data for economics and finance activities
activities = [
    'Economics', 'Investment Banking', 'Stock Trading', 'Wealth Management', 
    'Cryptocurrency', 'Venture Capital', 'Personal Finance', 'Corporate Finance', 
    'Fintech', 'Insurance', 'Real Estate', 'Hedge Funds', 'Private Equity', 
    'Crowdfunding'
]
market_share = [18.0, 15.5, 14.0, 12.0, 10.0, 8.5, 7.0, 6.0, 5.5, 4.5, 3.5, 2.5, 1.5, 1.0]

# Custom color scheme
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1', 
    '#FF8C33', '#8CFF33', '#33A1FF', '#FF33D4', '#33FFD4', '#D433FF', 
    '#33FFD4', '#FFD433'
]

# Treemap
plt.figure(figsize=(14, 10))  # Adjusting the size of the treemap
squarify.plot(sizes=market_share, label=activities, color=colors, alpha=0.8)
plt.title('Popularity of Economics & Finance Activities', fontsize=20, pad=40)
plt.axis('off')  # No axes for a cleaner look

plt.show()