
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'FoodItem': ['Bananas', 'Apples', 'Oranges', 'Tomatoes', 'Potatoes', 'Carrots', 'Broccoli', 'Lettuce', 
                 'Strawberries', 'Blueberries', 'Raspberries', 'Kale', 'Spinach', 'Cabbage'],
    'MarketShare': [30.2, 20.1, 15.5, 10.2, 8.7, 5.9, 3.3, 2.7, 1.2, 1.0, 0.9, 0.7, 0.6, 0.4],
    'SalesVolume': [320.8, 228.3, 108.7, 84.5, 58.9, 50.6, 34.1, 29.9, 12.4, 10.3, 9.2, 7.2, 6.2, 4.1],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Vegetable', 'Vegetable', 'Vegetable', 'Vegetable', 'Vegetable', 
                 'Berry', 'Berry', 'Berry', 'Leafy Green', 'Leafy Green', 'Leafy Green']
}
df = pd.DataFrame(data)

# Create a scatter plot with varying bubble sizes
plt.figure(figsize=(16, 10))
bubble_chart = sns.scatterplot(data=df, x="FoodItem", y="MarketShare", size="SalesVolume", hue="Category", 
                               palette={"Fruit": "#FF9999", "Vegetable": "#66B2FF", "Berry": "#99FF99", "Leafy Green": "#FFCC99"}, 
                               sizes=(20, 2000), alpha=0.7, edgecolor="w", linewidth=1)

plt.title("Market Share of Various Food Items in 2022", fontsize=16, pad=20)
plt.xlabel("Food Item", fontsize=14)
plt.ylabel("Market Share (%)", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title="Category", loc="upper right", bbox_to_anchor=(1.25, 1))

# Show the plot
plt.tight_layout()
plt.show()