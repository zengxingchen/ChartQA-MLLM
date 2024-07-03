
import matplotlib.pyplot as plt
import squarify

# Data points
platforms = ['Facebook', 'YouTube', 'WhatsApp', 'Instagram', 'WeChat', 'TikTok', 'QQ', 
             'Douyin', 'Sina Weibo', 'Snapchat', 'Telegram', 'Kuaishou', 'Pinterest', 
             'Reddit', 'Twitter']
users_in_millions = [2798, 2291, 2000, 1221, 1213, 689, 617, 600, 521, 514, 500, 481, 454, 430, 396]
colors = ['#FFD700', '#FF8C00', '#FF6347', '#ADFF2F', '#7FFFD4', '#20B2AA', 
          '#6495ED', '#9370DB', '#DC143C', '#FF69B4', '#A52A2A', '#BDB76B', 
          '#9ACD32', '#556B2F', '#1E90FF']

# Plot Dimensions
plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=users_in_millions, label=platforms, color=colors, alpha=0.7)

# Title
plt.title('Global Social Media Users by Platforms in Millions', fontsize=18)

# Remove axes
plt.axis('off')

# Show plot
plt.show()