
import matplotlib.pyplot as plt

# Data
topics = ['Video Games', 'Movies', 'Music', 'Reading', 'Traveling', 'Photography', 'Cooking', 
          'Gardening', 'Painting', 'Writing', 'Yoga', 'Dancing', 'Hiking', 'Crafts', 'Fishing']
hours_spent = [20, 45, 30, 50, 42, 38, 28, 40, 37, 33, 22, 39, 27, 20, 26]

# Color scheme using color codes
colors = ['#FF4500', '#32CD32', '#FFD700', '#1E90FF', '#8A2BE2', '#00CED1',
          '#FF1493', '#7FFF00', '#FF69B4', '#87CEEB', '#FF6347', '#8B0000', '#40E0D0', '#BA55D3', '#4682B4']

# Create vertical bar chart
plt.figure(figsize=(14, 8))
bars = plt.bar(topics, hours_spent, color=colors, width=0.6)

# Adjusting the width of bars
for bar in bars:
    bar.set_width(0.5)

# Changing the layout and labels
plt.ylabel('Hours Spent', fontsize=12)
plt.title('Weekly Entertainment & Leisure Activities Distribution', fontsize=16)
plt.ylim(15, max(hours_spent) * 1.1)  # Set y-axis limit starting from 15

# Adding value labels on top of each bar
for i, v in enumerate(hours_spent):
    plt.text(i, v + 1, str(v), color='black', ha='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()