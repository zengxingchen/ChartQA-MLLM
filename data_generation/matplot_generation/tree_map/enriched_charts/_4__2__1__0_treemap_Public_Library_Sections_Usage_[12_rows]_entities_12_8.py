
import matplotlib.pyplot as plt
import squarify

# Data for entertainment and leisure activities
activities = ['Movies', 'Concerts', 'Amusement Parks', 'Theater', 'Museums', 'Festivals', 'Video Games', 'Sports Events', 'Books', 'Television Shows', 'Escape Rooms', 'Board Games', 'Puzzles', 'Virtual Reality']
market_share = [18.0, 14.0, 12.5, 10.0, 9.0, 8.5, 7.5, 6.0, 5.5, 4.5, 2.5, 1.5, 0.5, 0.5]

# Custom color scheme
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#DAF7A6', '#FFC300', '#FF5733', '#C70039']

# Treemap
plt.figure(figsize=(14, 10))  # Adjusting the size of the treemap
squarify.plot(sizes=market_share, label=activities, color=colors, alpha=0.8)
plt.title('Popularity of Entertainment & Leisure Activities', fontsize=18, pad=40)
plt.axis('off')  # No axes for a cleaner look

plt.show()