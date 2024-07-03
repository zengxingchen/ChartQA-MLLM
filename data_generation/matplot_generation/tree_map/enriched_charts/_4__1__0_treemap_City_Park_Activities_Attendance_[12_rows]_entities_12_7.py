
import matplotlib.pyplot as plt
import squarify

# Data points
apps = [
    'Facebook', 'YouTube', 'WhatsApp', 'Facebook Messenger', 'Instagram', 
    'WeChat', 'TikTok', 'QQ', 'Douyin', 'Sina Weibo', 
    'Telegram', 'Snapchat', 'Kuaishou', 'Pinterest', 'Reddit', 
    'Twitter', 'Quora', 'LinkedIn', 'Viber', 'Discord'
]
users_in_millions = [
    2800, 2291, 2000, 1300, 1200, 
    1200, 689, 617, 600, 523, 
    500, 498, 481, 442, 430, 
    353, 300, 310, 260, 250
]
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', 
    '#33FFF4', '#FF3333', '#FF8C33', '#8CFF33', '#338CFF', 
    '#FF33A6', '#A6FF33', '#33A6FF', '#FF5733', '#33FFA6', 
    '#57FF33', '#A633FF', '#FFA633', '#33A6FF', '#FF338C'
]

# Plot Dimensions
plt.figure(figsize=(16, 12))

# Create a treemap
squarify.plot(sizes=users_in_millions, label=apps, color=colors, alpha=0.8)

# Title
plt.title('Number of Active Users of Social Media Apps (in Millions)', fontsize=18, pad=20)

# Remove axes
plt.axis('off')

# Show plot
plt.show()