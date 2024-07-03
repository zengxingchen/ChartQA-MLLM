
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a data frame with diversified data
df = pd.DataFrame({
    'category': ['Business & Entrepreneurship', 'Business & Entrepreneurship', 'Business & Entrepreneurship', 'Business & Entrepreneurship',
                 'Technology', 'Technology', 'Technology', 'Technology',
                 'Health & Psychology', 'Health & Psychology', 'Health & Psychology', 'Health & Psychology',
                 'Education & Learning', 'Education & Learning', 'Education & Learning', 'Education & Learning',
                 'Environment & Climate Change', 'Environment & Climate Change', 'Environment & Climate Change', 'Environment & Climate Change',
                 'Culture & Society', 'Culture & Society', 'Culture & Society', 'Culture & Society'],
    'sub_category': ['Startups', 'Corporate Strategy', 'Marketing', 'Finance',
                     'AI Development', 'Cybersecurity', 'Blockchain', 'Quantum Computing',
                     'Mental Health', 'Public Health', 'Medical Research', 'Nutrition',
                     'Higher Education', 'Online Learning', 'STEM Education', 'Vocational Training',
                     'Renewable Energy', 'Conservation Efforts', 'Pollution Control', 'Wildlife Protection',
                     'Music', 'Art', 'History', 'Literature'],
    'value': [1200, 1100, 900, 800, 1400, 1200, 1100, 900, 1300, 1100, 1000, 900, 1000, 900, 800, 700, 1100, 1000, 800, 700, 1200, 1100, 900, 800]
})

# Create a new color list
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
          '#9edae5', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#dbdb8d', '#c7c7c7', '#aec7e8',
          '#ffbb78', '#2ca02c', '#ff7f0e', '#1f77b4']

# Plot
plt.figure(figsize=(20, 10))
squarify.plot(sizes=df['value'], label=df['sub_category'], color=colors, alpha=.8)
plt.title('Distribution of Key Areas in Business & Technology', fontsize=20)
plt.axis('off')
plt.show()