
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Type': ['Historical Sites', 'Natural Wonders', 'Cultural Monuments', 'Historical Cities',
             'Archaeological Sites', 'Museums', 'Art Galleries', 'Ancient Ruins',
             'Historical Landmarks', 'National Parks', 'World Heritage Sites', 'Battlefields',
             'Historic Buildings', 'Archaeological Excavations', 'Historical Villages', 'Architectural Masterpieces',
             'Cultural Landscapes', 'Historic Homes', 'Ancient Temples', 'Forts and Castles', 'Historic Districts'],
    'Emissions': [120, 150, 200, 130, 160, 210, 100, 110, 140, 70, 80, 90, 95, 85, 135, 205, 190, 180, 175, 145, 155]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
colors = ["#ff7f0e", "#1f77b4", "#2ca02c", "#d62728", "#9467bd", "#8c564b", 
          "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#ffbb78", "#aec7e8",
          "#98df8a", "#ff9896", "#c5b0d5", "#c49c94", "#f7b6d2", "#c7c7c7",
          "#dbdb8d", "#9edae5", "#ffbb78"]
squarify.plot(sizes=df['Emissions'], label=df['Type'], alpha=0.8, color=colors)
plt.title('Distribution of Historical and Cultural Sites by Visitor Interest in 2024', fontsize=16, fontweight='bold', pad=20)
plt.axis('off')
plt.show()