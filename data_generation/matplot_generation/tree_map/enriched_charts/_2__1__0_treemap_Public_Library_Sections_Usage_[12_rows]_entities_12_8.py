
import matplotlib.pyplot as plt
import squarify

# Data for travel and adventure activities
activities = ['Mountain Climbing', 'Scuba Diving', 'Hiking', 'Safari', 'Paragliding', 'Skiing', 'Bungee Jumping', 'Rafting', 'Skydiving', 'Kayaking', 'Camping', 'Cycling', 'Surfing', 'Rock Climbing']
market_share = [15.0, 12.5, 11.0, 10.5, 9.0, 8.5, 7.0, 6.5, 5.5, 5.0, 4.5, 3.0, 1.5, 0.5]

# Custom color scheme
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#FF6F61', '#92A8D1', '#F7CAC9', '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC', '#EFC050', '#5B5EA6', '#9B2335']

# Treemap
plt.figure(figsize=(12, 12))  # Adjusting the size of the treemap
squarify.plot(sizes=market_share, label=activities, color=colors, alpha=0.8)
plt.title('Popularity of Travel & Adventure Activities', pad=30)
plt.axis('off')  # No axes for a cleaner look

plt.show()