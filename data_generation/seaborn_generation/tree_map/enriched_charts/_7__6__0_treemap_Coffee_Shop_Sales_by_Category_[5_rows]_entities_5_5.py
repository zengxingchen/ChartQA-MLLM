
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a DataFrame with the data
data = {
    'Category': ['Innovation', 'Investment', 'Painting', 'Traveling', 'Yoga', 'Concerts', 'Writing', 'Mental Health', 'Economics', 'Recycling', 'Fashion Trends', 'Historical Research', 'Government Policy', 'Space Missions', 'E-Learning', 'AI & Robotics', 'Ethical Debates', 'Movie Nights', 'Gourmet Cooking', 'Cultural Festivals'],
    'Value': [95, 85, 70, 65, 80, 50, 75, 90, 55, 60, 45, 85, 75, 90, 80, 85, 70, 65, 75, 60],
    'Aspect': ['Science & Nature', 'Business & Entrepreneurship', 'Art & Design', 'Travel & Adventure', 'Sports & Fitness', 'Music & Performing Arts', 'Literature & Writing', 'Health & Psychology', 'Economics & Finance', 'Environment & Climate Change', 'Fashion & Beauty', 'History & Archaeology', 'Politics & Governance', 'Astronomy & Space Exploration', 'Education & Learning', 'Future Technologies & Society', 'Philosophy & Ethics', 'Entertainment & Leisure', 'Food & Nutrition', 'Culture & Society']
}
df = pd.DataFrame(data)

# Plot parameters
plt.figure(figsize=(16, 12))
cmap = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#76d7c4','#f7b7a3','#ffccff','#c8e6c9','#bbdefb','#ffcdd2','#d1c4e9','#b39ddb','#e57373','#f06292','#ba68c8','#7986cb','#64b5f6']

# Create a treemap
squarify.plot(sizes=df['Value'], label=df['Category'], color=cmap, alpha=0.8)

plt.title('Key Aspects of Modern Life', fontsize=18, y=1.05)
plt.axis('off')

plt.show()