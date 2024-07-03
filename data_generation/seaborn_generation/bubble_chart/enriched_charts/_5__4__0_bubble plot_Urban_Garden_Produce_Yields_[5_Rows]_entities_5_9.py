
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for visualization
data = {
    'Category': ['Climate Change', 'Climate Change', 'Biodiversity', 'Biodiversity', 'Energy', 'Energy', 'Water Management', 'Water Management', 'Pollution Control', 'Pollution Control', 'Sustainable Agriculture', 'Sustainable Agriculture', 'Waste Management', 'Waste Management', 'Forest Conservation', 'Forest Conservation'],
    'Subcategory': ['Carbon Emissions', 'Global Warming', 'Species Conservation', 'Ecosystem Restoration', 'Solar Power', 'Wind Power', 'Water Purification', 'Desalination', 'Air Quality', 'Soil Remediation', 'Organic Farming', 'Urban Gardening', 'Recycling', 'Composting', 'Reforestation', 'Deforestation'],
    'ImpactScore': [85, 88, 90, 87, 92, 89, 84, 91, 86, 88, 90, 87, 93, 89, 91, 92],
    'EffortHours': [12, 14, 10, 11, 13, 15, 12, 13, 14, 10, 11, 12, 14, 10, 12, 13]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a Bubble Chart with Seaborn
plt.figure(figsize=(18, 12)) # Modified width and height
bubble = sns.scatterplot(data=df, x="Category", y="Subcategory", size="EffortHours", 
                         legend=False, sizes=(100, 1000), 
                         hue="ImpactScore", palette=["#FF6347", "#4682B4", "#9ACD32", "#FF4500", "#32CD32", "#1E90FF", "#FFD700", "#BA55D3"])

# Customizing the axes and title (with changed topic and headline)
plt.title("Impact and Effort in Environmental Projects", fontsize=20)
plt.xlabel("Category", fontsize=15)
plt.ylabel("Subcategory", fontsize=15)

# Adding legend
plt.legend(title="Impact Score", fontsize=12, title_fontsize=14, loc='upper left')

plt.show()