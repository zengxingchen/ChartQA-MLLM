
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Topic': ['Fashion Trends', 'Beauty Tips', 'Makeup Reviews', 'Hairstyle Ideas', 'Skincare Routines', 
              'Seasonal Fashion', 'Celebrity Styles', 'Accessory Guides', 'Streetwear Insights', 'Runway Highlights'],
    'Article Count': [25, 15, 20, 30, 18, 22, 27, 19, 16, 23]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))

sns.barplot(
    x='Topic',
    y='Article Count',
    data=df,
    palette=['#8E44AD', '#2980B9', '#16A085', '#F39C12', '#E74C3C', 
             '#D35400', '#2ECC71', '#3498DB', '#9B59B6', '#34495E'],
    dodge=False
)

plt.title('Article Distribution by Topic in Fashion & Beauty', fontsize=16)
plt.xlabel('Topic', fontsize=14)
plt.ylabel('Article Count', fontsize=14)

plt.xticks(rotation=45)
plt.ylim(0, 35)

for patch in plt.gca().patches:
    patch.set_width(0.4)

plt.show()