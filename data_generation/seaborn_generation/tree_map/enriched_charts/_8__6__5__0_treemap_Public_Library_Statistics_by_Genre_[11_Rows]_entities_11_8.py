
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a data frame with diversified data
df = pd.DataFrame({
    'category': ['Fashion & Beauty', 'Fashion & Beauty', 'Fashion & Beauty', 'Fashion & Beauty',
                 'Food & Nutrition', 'Food & Nutrition', 'Food & Nutrition', 'Food & Nutrition',
                 'Music & Performing Arts', 'Music & Performing Arts', 'Music & Performing Arts', 'Music & Performing Arts',
                 'Health & Psychology', 'Health & Psychology', 'Health & Psychology', 'Health & Psychology',
                 'Art & Design', 'Art & Design', 'Art & Design', 'Art & Design',
                 'Science & Nature', 'Science & Nature', 'Science & Nature', 'Science & Nature'],
    'sub_category': ['Hairstyling', 'Cosmetics', 'Skincare', 'Fashion Design',
                     'Fine Dining', 'Healthy Eating', 'Street Food', 'Baking',
                     'Opera', 'Theater', 'Rock Music', 'Classical Music',
                     'Mental Wellness', 'Physical Fitness', 'Public Health', 'Psychotherapy',
                     'Graphic Design', 'Interior Design', 'Photography', 'Painting',
                     'Astronomy', 'Botany', 'Zoology', 'Geology'],
    'value': [1100, 1200, 1300, 900, 1400, 1200, 1000, 1100, 800, 900, 1000, 1100, 
              1300, 1200, 1100, 1000, 1400, 1200, 1100, 1000, 1100, 1200, 1300, 1400]
})

# Create a new color list
colors = ['#4B0082', '#8A2BE2', '#A52A2A', '#DEB887', '#5F9EA0', '#7FFF00', '#D2691E', '#FF7F50', '#6495ED', '#DC143C', 
          '#00FFFF', '#00008B', '#008B8B', '#B8860B', '#A9A9A9', '#006400', '#8B008B', '#FF8C00', '#9932CC', '#8B0000', 
          '#E9967A', '#8FBC8F', '#483D8B', '#2F4F4F']

# Plot
plt.figure(figsize=(24, 12))
squarify.plot(sizes=df['value'], label=df['sub_category'], color=colors, alpha=.8)
plt.title('Distribution of Interests in Various Fields', fontsize=24, pad=20)
plt.axis('off')
plt.show()