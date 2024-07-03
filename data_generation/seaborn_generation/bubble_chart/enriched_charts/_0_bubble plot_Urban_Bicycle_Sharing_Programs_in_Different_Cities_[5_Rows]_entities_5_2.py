
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data into a Pandas DataFrame
data = pd.DataFrame({
    "Manufacturer": ["Samsung", "Apple", "Huawei", "Xiaomi", "Oppo", 
                     "Vivo", "Motorola", "Lenovo", "LG", "Nokia", 
                     "Sony", "HTC", "Google", "OnePlus", "Realme"],
    "MarketShare": [21.2, 15.6, 14.8, 8.3, 5.6, 5.3, 2.2, 1.9, 1.5, 1.4, 1.1, 0.6, 0.5, 0.5, 0.4],
    "Price": [250, 750, 300, 150, 200, 180, 150, 120, 240, 100, 350, 220, 650, 470, 130],
    "UnitsShipped": [320, 220, 200, 100, 95, 90, 60, 50, 40, 35, 30, 10, 9, 8, 8],
})

# Plot
plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=data, x="Price", y="MarketShare", size="UnitsShipped",
                               sizes=(100, 1000), alpha=0.7, palette=["#FF5733", "#33FF57", "#3357FF", 
                               "#8357FF", "#FF57B9", "#57FFC8", "#FFDA57", "#7CFF57",
                               "#578AFF", "#EF57FF", "#FF5757", "#57FFBE", "#57D2FF",
                               "#FF9D57", "#A7FF57"])

# Customize the axes and title
bubble_chart.set_xlabel("Average Smartphone Price ($)")
bubble_chart.set_ylabel("Global Market Share (%)")
bubble_chart.set_title("Smartphone Market Share, Price, and Units Shipped (Millions) by Manufacturer in 2023")

# Legend for sizes
h, lbls = bubble_chart.get_legend_handles_labels()
bubble_chart.legend(h[1:5], lbls[1:5], title="Units Shipped (Millions)", borderpad=1, loc = 'upper left', labelspacing=1.5)

plt.show()