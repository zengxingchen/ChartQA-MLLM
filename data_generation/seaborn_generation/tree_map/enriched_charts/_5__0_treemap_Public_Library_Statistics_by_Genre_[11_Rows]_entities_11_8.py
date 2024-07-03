
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a data frame with diversified data
df = pd.DataFrame({
    'category': ['Environment', 'Environment', 'Environment', 'Environment', 'Health', 'Health', 'Health', 'Health', 
                 'Technology', 'Technology', 'Technology', 'Technology', 'Education', 'Education', 'Education', 'Education', 
                 'Finance', 'Finance', 'Finance', 'Finance', 'Culture', 'Culture', 'Culture', 'Culture'],
    'sub_category': ['Renewable Energy', 'Conservation Efforts', 'Pollution Control', 'Wildlife Protection', 
                     'Medical Research', 'Nutrition', 'Mental Health', 'Public Health', 'AI Development', 'Cybersecurity', 
                     'Blockchain', 'Quantum Computing', 'Higher Education', 'Online Learning', 'STEM Education', 
                     'Vocational Training', 'Investment Banking', 'Personal Finance', 'Insurance', 'Real Estate', 
                     'Music', 'Art', 'History', 'Literature'],
    'value': [1400, 900, 500, 600, 1000, 800, 700, 600, 1200, 1100, 800, 700, 1300, 1000, 900, 700, 1500, 1200, 1000, 800, 
              900, 800, 700, 600]
})

# Create a new color list
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4', '#e6e6fa', '#ffb6c1', 
          '#ffa07a', '#ff7f50', '#dda0dd', '#b0c4de', '#f5deb3', '#deb887', '#98fb98', '#afeeee', '#db7093', '#d3d3d3', 
          '#b0e0e6', '#add8e6', '#f08080', '#f0e68c']

# Plot
plt.figure(figsize=(24, 12))
squarify.plot(sizes=df['value'], label=df['sub_category'], color=colors, alpha=.8)
plt.title('Sectoral Distribution of Key Areas', fontsize=25)
plt.axis('off')
plt.show()