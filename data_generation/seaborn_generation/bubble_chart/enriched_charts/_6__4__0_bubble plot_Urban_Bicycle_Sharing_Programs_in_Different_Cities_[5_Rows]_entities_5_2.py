
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data into a Pandas DataFrame
data = pd.DataFrame({
    "Manufacturer": ["Samsung", "Apple", "Huawei", "Xiaomi", "Oppo", 
                     "Vivo", "Motorola", "Lenovo", "LG", "Nokia", 
                     "Sony", "HTC", "Google", "OnePlus", "Realme", 
                     "Asus", "HP", "Dell", "Acer"],
    "NutritionalValue": [8.5, 9.2, 7.5, 8.0, 6.5, 7.0, 6.0, 6.8, 5.5, 7.2, 
                         8.8, 5.2, 9.0, 8.3, 7.8, 6.6, 7.4, 8.1, 7.3],
    "Calories": [200, 180, 210, 190, 220, 195, 250, 240, 260, 230, 170, 270, 
                 160, 185, 200, 215, 225, 175, 190],
    "FatContent": [10, 5, 12, 8, 15, 10, 20, 18, 22, 17, 6, 24, 4, 9, 11, 14, 
                   13, 7, 9],
    "Popularity": [95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 
                   25, 28, 33, 38, 43],
})

# Plot
plt.figure(figsize=(18, 14))
bubble_chart = sns.scatterplot(data=data, x="Calories", y="NutritionalValue", 
                               size="FatContent", sizes=(100, 1000), 
                               alpha=0.7, palette=["#1F77B4", "#FF7F0E", 
                               "#2CA02C", "#D62728", "#9467BD", "#8C564B", 
                               "#E377C2", "#7F7F7F", "#BCBD22", "#17BECF",
                               "#AEC7E8", "#FFBB78", "#98DF8A", "#FF9896",
                               "#C5B0D5", "#C49C94", "#F7B6D2", "#C7C7C7", 
                               "#DBDB8D"])

# Customize the axes and title
bubble_chart.set_xlabel("Calories")
bubble_chart.set_ylabel("Nutritional Value")
bubble_chart.set_title("Nutritional Value vs Calories and Fat Content by Manufacturer")

# Legend for sizes
h, lbls = bubble_chart.get_legend_handles_labels()
bubble_chart.legend(h[1:5], lbls[1:5], title="Fat Content (g)", borderpad=1, 
                    loc='upper left', labelspacing=1.5)

plt.show()