
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Category": ["Sports & Fitness", "Sports & Fitness", "Sports & Fitness", "Sports & Fitness", "Sports & Fitness", 
                 "Sports & Fitness", "Sports & Fitness", "Sports & Fitness", "Sports & Fitness", "Sports & Fitness",
                 "Health & Wellness", "Health & Wellness", "Health & Wellness", "Health & Wellness", "Health & Wellness",
                 "Travel & Adventure", "Travel & Adventure", "Travel & Adventure", "Travel & Adventure", "Travel & Adventure"],
    "Subcategory": ["Running", "Cycling", "Swimming", "Gym & Fitness", "Yoga & Pilates",
                    "Team Sports", "Outdoor Activities", "Martial Arts", "Fitness Technology", "Nutrition & Supplements",
                    "Mental Health", "Physical Therapy", "Healthcare Technology", "Wellness Programs", "Nutrition Counseling",
                    "Adventure Tourism", "Cultural Tourism", "Ecotourism", "Backpacking", "Luxury Travel"],
    "Value": [200000, 180000, 150000, 220000, 170000,
              140000, 160000, 130000, 210000, 190000,
              120000, 110000, 140000, 135000, 125000,
              200000, 190000, 180000, 170000, 160000]
}

df = pd.DataFrame(data)

color_mapper = {
    'Sports & Fitness': '#1f77b4',
    'Health & Wellness': '#ff7f0e',
    'Travel & Adventure': '#2ca02c'
}

colors = [color_mapper[category] for category in df['Category']]

fig, ax = plt.subplots(1, figsize=(18, 14))

squarify.plot(sizes=df['Value'], label=df['Subcategory'], color=colors, alpha=0.8, text_kwargs={'fontsize':9})

plt.title('Market Valuation by Subcategories in Sports & Fitness, Health & Wellness, and Travel & Adventure', fontsize=18)
plt.axis('off')
plt.show()