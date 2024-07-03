
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Category": ["Food & Nutrition", "Food & Nutrition", "Food & Nutrition", "Food & Nutrition", "Food & Nutrition",
                 "Environment & Climate Change", "Environment & Climate Change", "Environment & Climate Change", "Environment & Climate Change", "Environment & Climate Change",
                 "Health & Psychology", "Health & Psychology", "Health & Psychology", "Health & Psychology", "Health & Psychology",
                 "Culture & Society", "Culture & Society", "Culture & Society", "Culture & Society", "Culture & Society"],
    "Subcategory": ["Fruits", "Vegetables", "Meat & Poultry", "Dairy Products", "Grains & Cereals",
                    "Renewable Energy", "Recycling", "Pollution Control", "Conservation", "Climate Research",
                    "Mental Health Services", "Physical Therapy", "Healthcare Tech", "Wellness Programs", "Nutrition Counseling",
                    "Literature", "Performing Arts", "Visual Arts", "Heritage Sites", "Festivals & Events"],
    "Value": [120000, 90000, 150000, 110000, 80000,
              250000, 100000, 95000, 125000, 175000,
              200000, 85000, 180000, 105000, 95000,
              140000, 130000, 120000, 90000, 150000]
}

df = pd.DataFrame(data)

color_mapper = {
    'Food & Nutrition': '#ff9999',
    'Environment & Climate Change': '#66b3ff',
    'Health & Psychology': '#99ff99',
    'Culture & Society': '#ffcc99'
}

colors = [color_mapper[category] for category in df['Category']]

fig, ax = plt.subplots(1, figsize=(16, 12))

squarify.plot(sizes=df['Value'], label=df['Subcategory'], color=colors, alpha=0.8, text_kwargs={'fontsize':9})

plt.title('Market Valuation by Subcategories in Various Fields', fontsize=16)
plt.axis('off')
plt.show()