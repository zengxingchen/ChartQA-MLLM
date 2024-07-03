
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data into a Pandas DataFrame
data = pd.DataFrame({
    "Manufacturer": ["Samsung", "Apple", "Huawei", "Xiaomi", "Oppo", 
                     "Vivo", "Motorola", "Lenovo", "LG", "Nokia", 
                     "Sony", "HTC", "Google", "OnePlus", "Realme"],
    "NutritionalValue": [8.5, 9.2, 7.5, 8.0, 6.5, 7.0, 6.0, 6.8, 5.5, 7.2, 8.8, 5.2, 9.0, 8.3, 7.8],
    "Calories": [200, 180, 210, 190, 220, 195, 250, 240, 260, 230, 170, 270, 160, 185, 200],
    "FatContent": [10, 5, 12, 8, 15, 10, 20, 18, 22, 17, 6, 24, 4, 9, 11],
    "Popularity": [95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25],
})

# Plot
plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=data, x="Calories", y="NutritionalValue", size="FatContent",
                               sizes=(100, 1000), alpha=0.7, palette=["#FF5733", "#33FF57", "#3357FF", 
                               "#8357FF", "#FF57B9", "#57FFC8", "#FFDA57", "#7CFF57",
                               "#578AFF", "#EF57FF", "#FF5757", "#57FFBE", "#57D2FF",
                               "#FF9D57", "#A7FF57"])

# Customize the axes and title
bubble_chart.set_xlabel("Calories")
bubble_chart.set_ylabel("Nutritional Value")
bubble_chart.set_title("Nutritional Value vs Calories and Fat Content by Manufacturer")

# Legend for sizes
h, lbls = bubble_chart.get_legend_handles_labels()
bubble_chart.legend(h[1:5], lbls[1:5], title="Fat Content (g)", borderpad=1, loc='lower right', labelspacing=1.5)

plt.show()