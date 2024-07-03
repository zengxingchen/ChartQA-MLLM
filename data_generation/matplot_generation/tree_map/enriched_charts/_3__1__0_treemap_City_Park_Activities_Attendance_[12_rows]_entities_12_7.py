
import matplotlib.pyplot as plt
import squarify

# Data points
apps = ['Facebook', 'YouTube', 'WhatsApp', 'Instagram', 'Messenger', 
        'WeChat', 'QQ', 'Douyin', 'Sina Weibo', 'Qzone', 
        'Kuaishou', 'Snapchat', 'Twitter', 'Reddit', 'Pinterest', 
        'LinkedIn', 'Telegram', 'Viber', 'TikTok', 'Line']
active_users_in_millions = [290, 220, 200, 150, 130, 110, 100, 90, 80, 70, 
                            60, 50, 40, 35, 30, 25, 20, 15, 10, 5]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
          '#1f78b4', '#ff7e0d', '#2ca03c', '#d62729', '#9468bd', 
          '#8c564c', '#e377c3', '#7f7f80', '#bcbd23', '#17bec0']

# Plot Dimensions
plt.figure(figsize=(16, 12))

# Create a treemap
squarify.plot(sizes=active_users_in_millions, label=apps, color=colors, alpha=0.8)

# Title
plt.title('Number of Active Users of Social Media Apps (in Millions)', fontsize=20, pad=20)

# Remove axes
plt.axis('off')

# Show plot
plt.show()