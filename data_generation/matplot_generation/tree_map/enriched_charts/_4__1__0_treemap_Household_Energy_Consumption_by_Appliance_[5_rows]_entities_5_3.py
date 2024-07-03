
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "City": ["New York", "New York", "New York", "San Francisco", "San Francisco", "San Francisco",
             "Seattle", "Seattle", "Seattle", "Austin", "Austin", "Austin", 
             "Boston", "Boston", "Boston", "Chicago", "Chicago", "Chicago",
             "Miami", "Miami", "Miami", "Los Angeles", "Los Angeles", "Los Angeles",
             "Denver", "Denver", "Denver", "Dallas", "Dallas", "Dallas", 
             "Phoenix", "Phoenix", "Phoenix", "Philadelphia", "Philadelphia", "Philadelphia",
             "San Diego", "San Diego", "San Diego", "San Jose", "San Jose", "San Jose"],
    "Category": ["Innovation", "Sustainability", "Artificial Intelligence", "Innovation",
                 "Sustainability", "Artificial Intelligence", "Innovation", "Sustainability",
                 "Artificial Intelligence", "Innovation", "Sustainability", "Artificial Intelligence",
                 "Innovation", "Sustainability", "Artificial Intelligence", "Innovation",
                 "Sustainability", "Artificial Intelligence", "Innovation", "Sustainability",
                 "Artificial Intelligence", "Innovation", "Sustainability", "Artificial Intelligence",
                 "Innovation", "Sustainability", "Artificial Intelligence", "Innovation",
                 "Sustainability", "Artificial Intelligence", "Innovation", "Sustainability",
                 "Artificial Intelligence", "Innovation", "Sustainability", "Artificial Intelligence",
                 "Innovation", "Sustainability", "Artificial Intelligence", "Innovation",
                 "Sustainability", "Artificial Intelligence"],
    "Number of Mentions": [320, 280, 150, 350, 290, 180, 200, 150, 120, 210, 170, 130, 190, 160, 110, 230, 190, 140, 180, 140, 100, 240, 200, 170, 190, 180, 160, 220, 190, 150, 200, 170, 140, 230, 210, 180, 210, 190, 160, 200, 180, 150]
}

df = pd.DataFrame(data)
grouped_data = df.groupby("Category").sum().reset_index()

colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#33FFF6", "#FF9633", "#9633FF", "#33FF96", "#FF3333", "#A633FF", "#33FFA6", "#FF3396", "#33FF33", "#FF33F6", "#FF9633", "#9633FF", "#33FF96", "#FF3333", "#A633FF", "#33FFA6", "#FF3396", "#33FF33", "#FF33F6", "#FF9633"]

plt.figure(figsize=(16, 12))
squarify.plot(sizes=grouped_data['Number of Mentions'], label=grouped_data['Category'], alpha=0.8, color=colors)
plt.title('Mentions of Future Technologies in Major Cities', fontsize=18, pad=20)
plt.axis('off')
plt.show()