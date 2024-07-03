
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Category": ["Health", "Health", "Health", "Health",
                 "Technology", "Technology", "Technology", "Technology",
                 "Environment", "Environment", "Environment", "Environment",
                 "Finance", "Finance", "Finance", "Finance",
                 "Education", "Education", "Education", "Education"],
    "Subcategory": ["Nutrition", "Exercise", "Mental Health", "Disease Prevention",
                    "AI", "Blockchain", "Quantum Computing", "VR/AR",
                    "Climate Change", "Recycling", "Wildlife Conservation", "Pollution Control",
                    "Investing", "Cryptocurrency", "Insurance", "Personal Finance",
                    "E-learning", "Higher Education", "Primary Education", "Vocational Training"],
    "Value": [1600, 1200, 800, 600, 
              1400, 900, 700, 500, 
              1500, 1100, 700, 500, 
              1300, 900, 800, 600, 
              1700, 1200, 800, 500]
}

df = pd.DataFrame(data)
grouped_data = df.groupby("Subcategory").sum().reset_index()

colors = ["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#FF33A1", "#33FFA5", "#FF8C33", "#A633FF", 
          "#FFD133", "#33FFD1", "#7F33FF", "#FF3388", "#33FF88", "#FF338A", "#33FF8C", "#8C33FF",
          "#FF5733", "#33FF57", "#3357FF", "#F333FF"]

plt.figure(figsize=(16, 12))
squarify.plot(sizes=grouped_data['Value'], label=grouped_data['Subcategory'], alpha=0.8, color=colors)
plt.title('Popular Topics in Different Categories', fontsize=18, pad=20)
plt.axis('off')
plt.show()