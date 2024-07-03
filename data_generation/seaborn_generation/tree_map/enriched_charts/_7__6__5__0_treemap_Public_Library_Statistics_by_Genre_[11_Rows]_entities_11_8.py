
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a data frame with diversified data
df = pd.DataFrame({
    'category': ['Literature & Writing', 'Literature & Writing', 'Literature & Writing', 'Literature & Writing',
                 'Philosophy & Ethics', 'Philosophy & Ethics', 'Philosophy & Ethics', 'Philosophy & Ethics',
                 'Sports & Fitness', 'Sports & Fitness', 'Sports & Fitness', 'Sports & Fitness',
                 'Food & Nutrition', 'Food & Nutrition', 'Food & Nutrition', 'Food & Nutrition',
                 'Art & Design', 'Art & Design', 'Art & Design', 'Art & Design',
                 'Business & Entrepreneurship', 'Business & Entrepreneurship', 'Business & Entrepreneurship', 'Business & Entrepreneurship',
                 'Culture & Society', 'Culture & Society', 'Culture & Society', 'Culture & Society'],
    'sub_category': ['Poetry', 'Novels', 'Short Stories', 'Plays',
                     'Existentialism', 'Ethics', 'Metaphysics', 'Logic',
                     'Running', 'Cycling', 'Swimming', 'Weightlifting',
                     'Fruits', 'Vegetables', 'Proteins', 'Dairy',
                     'Painting', 'Sculpture', 'Graphic Design', 'Photography',
                     'Marketing', 'Finance', 'Management', 'Entrepreneurship',
                     'Music', 'Theatre', 'Dance', 'Film'],
    'value': [1000, 950, 850, 800, 1100, 1050, 950, 900, 1200, 1150, 1000, 900, 1300, 1200, 1100, 1000, 1100, 1050, 950, 900, 1300, 1250, 1200, 1150, 1100, 1050, 1000, 950]
})

# Create a new color list
colors = ['#4B0082', '#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD', '#D2691E', '#FF4500', '#DAA520', '#2E8B57',
          '#8A2BE2', '#FF69B4', '#87CEEB', '#FFA07A', '#7FFF00', '#FF00FF', '#FF1493', '#00BFFF', '#CD5C5C', '#BDB76B',
          '#00FF7F', '#FF6347', '#20B2AA', '#6B8E23', '#FA8072', '#FF00FF', '#FF1493', '#00BFFF']

# Plot
plt.figure(figsize=(24, 12))
squarify.plot(sizes=df['value'], label=df['sub_category'], color=colors, alpha=.8)
plt.title('Distribution of Key Areas in Literature, Philosophy, and Arts', fontsize=20, pad=20)
plt.axis('off')
plt.show()