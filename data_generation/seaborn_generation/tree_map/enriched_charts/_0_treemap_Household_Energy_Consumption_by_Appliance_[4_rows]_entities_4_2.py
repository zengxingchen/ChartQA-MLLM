
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data from the CSV format above
data = {
    "Sector": ["Technology", "Technology", "Technology", "Finance", "Finance",
               "Healthcare", "Healthcare", "Consumer Discretionary",
               "Consumer Discretionary", "Consumer Staples", "Consumer Staples",
               "Energy", "Energy"],
    "Company": ["Apple", "Microsoft", "Google", "JPMorgan Chase", "Bank of America",
                "UnitedHealth Group", "Johnson & Johnson", "Tesla", "Amazon",
                "Procter & Gamble", "Coca-Cola", "ExxonMobil", "Chevron"],
    "MarketCap": [2290000, 1840000, 1012000, 390000, 325000,
                  350000, 380000, 600000, 1555000, 340000, 230000,
                  265000, 210000]
}

df = pd.DataFrame(data)

# Create a color palette, mapped to Sector
color_mapper = {
    'Technology': '#4285F4',  # Google Blue
    'Finance': '#34A853',     # Green
    'Healthcare': '#FBBC05',  # Yellow
    'Consumer Discretionary': '#EA4335',  # Red
    'Consumer Staples': '#673AB7',       # Deep purple
    'Energy': '#FF5722'       # Deep orange
}

colors = [color_mapper[sector] for sector in df['Sector']]

# Create the figure
fig, ax = plt.subplots(1, figsize=(12, 8))

# Create the treemap
squarify.plot(sizes=df['MarketCap'], label=df['Company'], color=colors, alpha=0.8, text_kwargs={'fontsize':9})

plt.title('Market Capitalization of Major Companies by Sector')
plt.axis('off')
plt.show()