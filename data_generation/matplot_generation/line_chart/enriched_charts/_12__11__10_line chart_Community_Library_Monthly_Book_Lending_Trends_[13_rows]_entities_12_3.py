
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Organic Farming': 300, 'Plant-Based Alternatives': 180, 'Nutritional Supplements': 220, 'Food Safety': 400, 'R&D on Superfoods': 100},
    {'Month': 'February', 'Organic Farming': 320, 'Plant-Based Alternatives': 200, 'Nutritional Supplements': 230, 'Food Safety': 390, 'R&D on Superfoods': 120},
    {'Month': 'March', 'Organic Farming': 310, 'Plant-Based Alternatives': 190, 'Nutritional Supplements': 240, 'Food Safety': 380, 'R&D on Superfoods': 110},
    {'Month': 'April', 'Organic Farming': 330, 'Plant-Based Alternatives': 210, 'Nutritional Supplements': 250, 'Food Safety': 370, 'R&D on Superfoods': 130},
    {'Month': 'May', 'Organic Farming': 340, 'Plant-Based Alternatives': 220, 'Nutritional Supplements': 260, 'Food Safety': 360, 'R&D on Superfoods': 140},
    {'Month': 'June', 'Organic Farming': 350, 'Plant-Based Alternatives': 230, 'Nutritional Supplements': 270, 'Food Safety': 350, 'R&D on Superfoods': 150},
    {'Month': 'July', 'Organic Farming': 340, 'Plant-Based Alternatives': 220, 'Nutritional Supplements': 280, 'Food Safety': 340, 'R&D on Superfoods': 160},
    {'Month': 'August', 'Organic Farming': 360, 'Plant-Based Alternatives': 240, 'Nutritional Supplements': 290, 'Food Safety': 330, 'R&D on Superfoods': 170},
    {'Month': 'September', 'Organic Farming': 370, 'Plant-Based Alternatives': 250, 'Nutritional Supplements': 300, 'Food Safety': 320, 'R&D on Superfoods': 180},
    {'Month': 'October', 'Organic Farming': 380, 'Plant-Based Alternatives': 260, 'Nutritional Supplements': 310, 'Food Safety': 310, 'R&D on Superfoods': 190},
    {'Month': 'November', 'Organic Farming': 390, 'Plant-Based Alternatives': 270, 'Nutritional Supplements': 320, 'Food Safety': 300, 'R&D on Superfoods': 200},
    {'Month': 'December', 'Organic Farming': 400, 'Plant-Based Alternatives': 280, 'Nutritional Supplements': 330, 'Food Safety': 290, 'R&D on Superfoods': 210}
]

months = [entry['Month'] for entry in data]
organic_farming = [entry['Organic Farming'] for entry in data]
plant_based_alternatives = [entry['Plant-Based Alternatives'] for entry in data]
nutritional_supplements = [entry['Nutritional Supplements'] for entry in data]
food_safety = [entry['Food Safety'] for entry in data]
rd_superfoods = [entry['R&D on Superfoods'] for entry in data]

plt.figure(figsize=(16, 8))
plt.plot(months, organic_farming, marker='o', linestyle='-', color='#8c564b', label='Organic Farming')
plt.plot(months, plant_based_alternatives, marker='s', linestyle='--', color='#e377c2', label='Plant-Based Alternatives')
plt.plot(months, nutritional_supplements, marker='^', linestyle='-.', color='#7f7f7f', label='Nutritional Supplements')
plt.plot(months, food_safety, marker='x', linestyle=':', color='#bcbd22', label='Food Safety')
plt.plot(months, rd_superfoods, marker='d', linestyle='-', color='#17becf', label='R&D on Superfoods')

plt.title('Food & Nutrition: Monthly Investment Trends in Healthy Food Initiatives', pad=20)
plt.xlabel('Month')
plt.ylabel('Investment (in Million USD)')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.grid(True)

# Annotations
for i, txt in enumerate(rd_superfoods):
    plt.annotate(txt, (months[i], rd_superfoods[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()