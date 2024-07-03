
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Manufacturer": ["Samsung", "Apple", "Huawei", "Xiaomi", "Oppo", 
                     "Vivo", "Motorola", "Lenovo", "LG", "Nokia", 
                     "Sony", "HTC", "Google", "OnePlus", "Realme", "BlackBerry", "Asus"],
    "NutritionalValue": [8.5, 9.2, 7.5, 8.0, 6.5, 7.0, 6.0, 6.8, 5.5, 7.2, 8.8, 5.2, 9.0, 8.3, 7.8, 6.3, 8.1],
    "Calories": [200, 180, 210, 190, 220, 195, 250, 240, 260, 230, 170, 270, 160, 185, 200, 245, 205],
    "FatContent": [10, 5, 12, 8, 15, 10, 20, 18, 22, 17, 6, 24, 4, 9, 11, 19, 13],
    "Popularity": [95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 50, 65],
})

plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=data, x="Calories", y="NutritionalValue", size="FatContent",
                               sizes=(100, 1000), alpha=0.7, palette=["#FF6347", "#4682B4", "#9ACD32", 
                               "#DAA520", "#BA55D3", "#40E0D0", "#FF4500", "#8B0000",
                               "#2E8B57", "#6A5ACD", "#FFD700", "#008080", "#D2691E",
                               "#B0E0E6", "#C71585", "#808000", "#FF69B4"])

bubble_chart.set_xlabel("Calories")
bubble_chart.set_ylabel("Nutritional Value")
bubble_chart.set_title("Calories vs Nutritional Value and Fat Content by Manufacturer", y=1.03)

h, lbls = bubble_chart.get_legend_handles_labels()
bubble_chart.legend(h[1:5], lbls[1:5], title="Fat Content (g)", borderpad=1, loc='upper left', labelspacing=1.5)

plt.show()