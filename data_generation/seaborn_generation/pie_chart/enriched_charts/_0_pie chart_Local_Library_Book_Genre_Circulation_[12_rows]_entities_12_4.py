
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'Platform': [
        'Facebook', 'YouTube', 'WhatsApp', 'Instagram', 'WeChat',
        'TikTok', 'QQ', 'Douyin', 'Telegram', 'Snapchat',
        'Pinterest', 'Reddit', 'Twitter', 'LinkedIn', 'Viber'
    ],
    'Active Users': [
        2796, 2291, 2000, 1386, 1203,
        1000, 617, 600, 550, 514,
        478, 430, 396, 310, 260
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Color scheme (e.g., #RRGGBB format)
colors = [
    '#3b5998', '#ff0000', '#25D366', '#C13584', '#09B83E',
    '#FF0000', '#12B7F5', '#EE1D52', '#0088cc', '#FFFC00',
    '#CB2027', '#FF4500', '#1DA1F2', '#0077B5', '#665CAC'
]

# Plot
plt.figure(figsize=(12, 8))
plt.pie(
    df['Active Users'],
    labels=df['Platform'],
    colors=colors,
    autopct='%1.1f%%',
    startangle=140
)
plt.title('Social Media Platforms by Active Users (in millions)')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the plot
plt.show()