
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    "Field": ["History", "Archaeology", "Health", "Psychology", "Philosophy", "Ethics", 
              "Entertainment", "Leisure", "Art", "Design", "Culture", "Society", "Astronomy", 
              "Space Exploration", "Science", "Nature", "Politics", "Governance", "Food", 
              "Nutrition", "Environment", "Climate Change", "Education", "Learning", "Fashion", 
              "Beauty", "Travel", "Adventure", "Literature", "Writing", "Economics", "Finance", 
              "Business", "Entrepreneurship", "Future Technologies", "Society", "Music", 
              "Performing Arts", "Sports", "Fitness"],
    "Amount": [120, 110, 130, 140, 105, 95, 80, 75, 100, 125, 115, 90, 85, 135, 145, 150, 
               140, 105, 110, 95, 85, 80, 125, 115, 130, 135, 75, 70, 90, 85, 145, 150, 
               140, 135, 140, 125, 110, 105, 130, 120]
}

df = pd.DataFrame(data)

color_mapper = {
    'History': '#FF5733', 'Archaeology': '#33FF57', 'Health': '#3357FF', 'Psychology': '#FF33A1', 
    'Philosophy': '#F3FF33', 'Ethics': '#33FFF6', 'Entertainment': '#FF8A33', 'Leisure': '#8A33FF', 
    'Art': '#57FF33', 'Design': '#3357FF', 'Culture': '#33FFF6', 'Society': '#FF333A', 
    'Astronomy': '#8A33FF', 'Space Exploration': '#FF33A1', 'Science': '#57FF33', 'Nature': '#FF5733', 
    'Politics': '#33FF57', 'Governance': '#3357FF', 'Food': '#FF33A1', 'Nutrition': '#F3FF33', 
    'Environment': '#33FFF6', 'Climate Change': '#FF8A33', 'Education': '#8A33FF', 'Learning': '#57FF33', 
    'Fashion': '#3357FF', 'Beauty': '#33FFF6', 'Travel': '#FF333A', 'Adventure': '#8A33FF', 
    'Literature': '#FF33A1', 'Writing': '#57FF33', 'Economics': '#FF5733', 'Finance': '#33FF57', 
    'Business': '#3357FF', 'Entrepreneurship': '#FF33A1', 'Future Technologies': '#F3FF33', 
    'Society': '#33FFF6', 'Music': '#FF8A33', 'Performing Arts': '#8A33FF', 'Sports': '#57FF33', 
    'Fitness': '#3357FF'
}

colors = [color_mapper[field] for field in df['Field']]

fig, ax = plt.subplots(1, figsize=(18, 12))

squarify.plot(sizes=df['Amount'], label=df['Field'], color=colors, alpha=0.8, text_kwargs={'fontsize':9})

plt.title('Field of Study Distribution (Number of Publications)', fontsize=18, pad=20)
plt.axis('off')
plt.show()