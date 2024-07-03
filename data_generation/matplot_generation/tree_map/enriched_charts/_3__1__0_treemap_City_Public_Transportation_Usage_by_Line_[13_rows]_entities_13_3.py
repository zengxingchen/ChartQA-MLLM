
import matplotlib.pyplot as plt
import squarify

labels = [
    'Hiking', 'Camping', 'Mountaineering', 'Kayaking', 'Skiing', 
    'Rock Climbing', 'Bird Watching', 'Fishing', 'Surfing', 
    'Scuba Diving', 'Snorkeling', 'Caving', 'Bungee Jumping', 
    'Paragliding', 'Skydiving', 'White Water Rafting'
]
sizes = [10, 12, 8, 5, 15, 7, 3, 11, 13, 9, 4, 6, 2, 14, 1, 12]
colors = [
    '#32a852', '#a83232', '#324da8', '#a83a74', '#eb4034', 
    '#40e0d0', '#ff6347', '#4682b4', '#ff4500', '#2e8b57', 
    '#b22222', '#daa520', '#778899', '#800080', '#40e0d0', 
    '#ff6347'
]

plt.figure(figsize=(14, 12))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

plt.title('Adventurous Outdoor Activities Distribution', fontsize=20)
plt.axis('off')

plt.show()