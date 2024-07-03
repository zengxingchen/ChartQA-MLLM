
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Category': ['Fashion', 'Beauty', 'Accessories', 'Footwear', 'Jewelry', 'Cosmetics', 'Hairstyling', 'Skincare', 'Perfume', 'Nail Care', 'Watches', 'Eyewear'],
    'Population': [1000, 1200, 1500, 1100, 950, 1300, 800, 900, 700, 600, 750, 850]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FF8C33", "#D4FF33", "#33FFF0", "#E033FF", "#FF3367", "#33FFB6", "#3375FF", "#FF3344"]
squarify.plot(sizes=df['Population'], label=df['Category'], alpha=0.8, color=colors)
plt.title('Distribution of Fashion & Beauty Categories by Population', fontsize=20, pad=30)
plt.axis('off')
plt.show()