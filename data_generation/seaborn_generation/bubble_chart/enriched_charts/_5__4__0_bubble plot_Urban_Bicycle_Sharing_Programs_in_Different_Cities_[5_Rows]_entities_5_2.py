
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data into a Pandas DataFrame
data = pd.DataFrame({
    "Manufacturer": ["Samsung", "Apple", "Huawei", "Xiaomi", "Oppo", 
                     "Vivo", "Motorola", "Lenovo", "LG", "Nokia", 
                     "Sony", "HTC", "Google", "OnePlus", "Realme", "BlackBerry", "Asus"],
    "NutritionalValue": [8.5, 9.2, 7.5, 8.0, 6.5, 7.0, 6.0, 6.8, 5.5, 7.2, 8.8, 5.2, 9.0, 8.3, 7.8, 6.3, 8.1],
    "Calories": [200, 180, 210, 190, 220, 195, 250, 240, 260, 230, 170, 270, 160, 185, 200, 245, 205],
    "FatContent": [10, 5, 12, 8, 15, 10, 20, 18, 22, 17, 6, 24, 4, 9, 11, 19, 13],
    "Popularity": [95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 50, 65],
})

# Plot
plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=data, x="Calories", y="NutritionalValue", size="FatContent",
                               sizes=(100, 1000), alpha=0.7, palette=["#1f77b4", "#ff7f0e", "#2ca02c", 
                               "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f",
                               "#bcbd22", "#17becf", "#393b79", "#637939", "#e6550d",
                               "#756bb1", "#636363", "#d6616b", "#ff9896"])

# Customize the axes and title
bubble_chart.set_xlabel("Calories")
bubble_chart.set_ylabel("Nutritional Value")
bubble_chart.set_title("Calories vs Nutritional Value and Fat Content by Manufacturer")

# Legend for sizes
h, lbls = bubble_chart.get_legend_handles_labels()
bubble_chart.legend(h[1:5], lbls[1:5], title="Fat Content (g)", borderpad=1, loc='upper right', labelspacing=1.5)

plt.show()