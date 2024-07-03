
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Type': ['Petrol Small', 'Petrol Medium', 'Petrol Large', 'Diesel Small',
             'Diesel Medium', 'Diesel Large', 'Hybrid Small', 'Hybrid Medium',
             'Hybrid Large', 'Electric Small', 'Electric Medium', 'Electric SUV',
             'Electric Coupe', 'Electric Sedan', 'Hybrid Sedan', 'Diesel SUV',
             'Petrol SUV', 'Petrol Coupe'],
    'Emissions': [120, 150, 200, 130, 160, 210, 100, 110, 140, 70, 80, 90, 95, 85, 135, 205, 190, 180]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
colors = ["#ff6347", "#4682b4", "#32cd32", "#ff4500", "#1e90ff", "#adff2f", 
          "#ff69b4", "#7fffd4", "#daa520", "#40e0d0", "#ffa07a", "#9acd32",
          "#00ced1", "#ffb6c1", "#f4a460", "#d2691e", "#8b0000", "#2e8b57"]
squarify.plot(sizes=df['Emissions'], label=df['Type'], alpha=0.8, color=colors)
plt.title('Distribution of Vehicle Types by CO2 Emissions in 2024', fontsize=16, fontweight='bold')
plt.axis('off')
plt.show()