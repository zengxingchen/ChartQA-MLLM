
import matplotlib.pyplot as plt
import squarify

food_items = [
    'Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Figs', 'Grapes',
    'Honeydew', 'Indian_Figs', 'Jackfruit', 'Kiwis', 'Lemons', 'Mangoes', 
    'Nectarines', 'Oranges', 'Papayas', 'Quinces', 'Raspberries', 'Strawberries', 
    'Tangerines', 'Ugli_Fruit', 'Vanilla', 'Watermelons', 'Xigua', 
    'Yellow_Passion_Fruit', 'Zucchini'
]

count = [
    1200, 950, 850, 720, 600, 500, 450, 380, 320, 290, 250, 200, 180, 160, 140, 
    120, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10
]

color_palette = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA6', '#FF8C33', 
    '#3385FF', '#85FF33', '#FF3333', '#33FFC4', '#A6FF33', '#FF3385', '#338AFF', 
    '#D433FF', '#33FF8C', '#FF6F33', '#3333FF', '#33FFDB', '#B533FF', '#33FF57', 
    '#5733FF', '#FFB833', '#33A1FF', '#FF33D4'
]

plt.figure(figsize=(20, 12))

squarify.plot(sizes=count, label=food_items, color=color_palette, alpha=0.8)

plt.title('Popular Fruits Distribution in the Market', fontsize=24, fontweight='bold', pad=20)
plt.axis('off')

plt.show()