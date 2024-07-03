
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Category': ['Physics Books', 'Chemistry Books', 'Biology Books', 'Mathematics Books', 'Computer Science Books',
                 'Engineering Books', 'History Books', 'Geography Books', 'Literature Books', 'Art Books',
                 'Music Books', 'Philosophy Books', 'Economics Books', 'Politics Books', 'Psychology Books', 'Sociology Books'],
    'Amount': [250, 300, 200, 180, 220, 260, 190, 150, 170, 160, 140, 130, 210, 120, 110, 100]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
colors = ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f", "#edc949", "#af7aa1", "#ff9da7", "#9c755f", "#bab0ab",
          "#86bc25", "#d6c1b8", "#ce6dbd", "#17becf", "#bcbd22", "#7f7f7f"]
squarify.plot(sizes=df['Amount'], label=df['Category'], alpha=0.8, color=colors)
plt.title('Library Book Distribution by Category', fontsize=18)
plt.axis('off')
plt.show()