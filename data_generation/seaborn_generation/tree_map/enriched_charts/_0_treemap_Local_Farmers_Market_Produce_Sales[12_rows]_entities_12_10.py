
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import squarify

# Define the data
data = {
    'Platform': [
        'Facebook', 'YouTube', 'WhatsApp', 'Instagram', 
        'WeChat', 'TikTok', 'QQ', 'Douyin', 'Telegram', 
        'Snapchat', 'Twitter', 'Pinterest', 'Reddit', 'LinkedIn'
    ],
    'Users (Millions)': [
        2790, 2291, 2000, 1500, 1252, 1000, 850, 
        600, 550, 498, 436, 431, 430, 310
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color palette
colors = [
    '#FF5733', '#FFC300', '#FF0000', '#C70039',
    '#900C3F', '#DAF7A6', '#FFC0CB', '#9B59B6',
    '#3498DB', '#85C1E9', '#16A085', '#138D75',
    '#7D3C98', '#F39C12'
]

# Define size of the figure
plt.figure(figsize=(16, 9))

# Plot the treemap with the specified colors and data
squarify.plot(sizes=df['Users (Millions)'], label=df['Platform'], color=colors, alpha=0.8)

plt.title('Global Social Media Users by Platform (in Millions)', fontsize=20)
plt.axis('off')
plt.show()