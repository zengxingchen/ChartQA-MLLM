
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Category": ["Instagram", "YouTube", "TikTok", "Facebook", "Twitter", "Snapchat", "LinkedIn", "Pinterest", "Reddit", "WhatsApp", "Telegram", "WeChat"],
    "Followers (Million)": [1800, 2100, 1200, 2500, 600, 500, 800, 450, 600, 2200, 500, 1100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots(figsize=(16, 10))

# Area chart
ax.fill_between(df['Category'], df['Followers (Million)'], color='#ff7f0e', alpha=0.7)

# Titles and labels
ax.set_title('Social Media Platform Followers', fontsize=20, pad=25)
ax.set_xlabel('Platform', fontsize=15)
ax.set_ylabel('Followers (Million)', fontsize=15)

# Annotations
for i, txt in enumerate(df['Followers (Million)']):
    ax.annotate(txt, (df['Category'][i], df['Followers (Million)'][i]), textcoords="offset points", xytext=(0,5), ha='center')

# Display the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()