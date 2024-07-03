
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Category": ["Artificial Intelligence", "Artificial Intelligence", "Artificial Intelligence", "Artificial Intelligence", "Artificial Intelligence",
                 "Renewable Energy", "Renewable Energy", "Renewable Energy", "Renewable Energy", "Renewable Energy",
                 "Smart Cities", "Smart Cities", "Smart Cities", "Smart Cities", "Smart Cities",
                 "Blockchain & Crypto", "Blockchain & Crypto", "Blockchain & Crypto", "Blockchain & Crypto", "Blockchain & Crypto"],
    "Subcategory": ["Machine Learning", "Neural Networks", "Computer Vision", "Natural Language Processing", "Robotics",
                    "Solar Power", "Wind Energy", "Hydropower", "Bioenergy", "Geothermal Energy",
                    "Internet of Things", "Urban Mobility", "Smart Buildings", "Smart Infrastructure", "Energy Efficiency",
                    "Cryptocurrencies", "Smart Contracts", "Decentralized Finance", "NFTs", "Blockchain Platforms"],
    "Value": [220000, 180000, 150000, 170000, 200000,
              300000, 250000, 230000, 210000, 270000,
              180000, 150000, 160000, 190000, 140000,
              250000, 200000, 220000, 230000, 240000]
}

df = pd.DataFrame(data)

color_mapper = {
    'Artificial Intelligence': '#ff5733',
    'Renewable Energy': '#33ff57',
    'Smart Cities': '#3357ff',
    'Blockchain & Crypto': '#ff33a1'
}

colors = [color_mapper[category] for category in df['Category']]

fig, ax = plt.subplots(1, figsize=(18, 14))

squarify.plot(sizes=df['Value'], label=df['Subcategory'], color=colors, alpha=0.8, text_kwargs={'fontsize':9})

plt.title('Investment Distribution in Future Technologies & Society', fontsize=18)
plt.axis('off')
plt.show()