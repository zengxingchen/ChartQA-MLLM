
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Company": ["Apple", "Microsoft", "Amazon", "Google", "Facebook",
                "Tesla", "Berkshire Hathaway", "Visa", "Johnson & Johnson", "Walmart",
                "Samsung", "Mastercard", "NVIDIA", "Home Depot", "Procter & Gamble"],
    "MarketCapitalization": [2250000, 2000000, 1600000, 1500000, 900000,
                             800000, 700000, 500000, 470000, 420000,
                             400000, 360000, 350000, 320000, 310000]
}

df = pd.DataFrame(data)

color_mapper = {
    'Apple': '#FF5733', 
    'Microsoft': '#33FF57', 
    'Amazon': '#3357FF', 
    'Google': '#FF33A1', 
    'Facebook': '#F3FF33', 
    'Tesla': '#33FFF6', 
    'Berkshire Hathaway': '#FF8A33', 
    'Visa': '#8A33FF', 
    'Johnson & Johnson': '#57FF33', 
    'Walmart': '#3357FF', 
    'Samsung': '#33FFF6', 
    'Mastercard': '#FF333A', 
    'NVIDIA': '#8A33FF', 
    'Home Depot': '#FF33A1', 
    'Procter & Gamble': '#57FF33'
}

colors = [color_mapper[company] for company in df['Company']]

fig, ax = plt.subplots(1, figsize=(16, 12))

squarify.plot(sizes=df['MarketCapitalization'], label=df['Company'], color=colors, alpha=0.8, text_kwargs={'fontsize':9})

plt.title('Market Capitalization of Top Companies (in million USD)', fontsize=18)
plt.axis('off')
plt.show()