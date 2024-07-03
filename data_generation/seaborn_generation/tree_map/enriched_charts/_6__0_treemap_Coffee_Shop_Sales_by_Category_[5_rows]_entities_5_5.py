
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a DataFrame with the data
data = {
    'Category': ['Nutrition', 'Exercise', 'Sleep', 'Mental Wellness', 'Socializing', 'Hydration', 'Hobbies', 'Work-life Balance', 'Personal Growth', 'Relaxation', 'Diet', 'Education', 'Creativity', 'Productivity', 'Mindfulness'],
    'Value': [90, 75, 65, 85, 50, 45, 60, 70, 55, 80, 95, 85, 60, 75, 80],
    'Aspect': ['Health', 'Fitness', 'Health', 'Psychology', 'Social', 'Health', 'Leisure', 'Work', 'Psychology', 'Leisure', 'Health', 'Learning', 'Leisure', 'Work', 'Psychology']
}
df = pd.DataFrame(data)

# Plot parameters
plt.figure(figsize=(14, 10))
cmap = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#9edae5', '#f7b6d2', '#c7c7c7', '#c49c94', '#dbdb8d']

# Create a treemap
squarify.plot(sizes=df['Value'], label=df['Category'], color=cmap, alpha=0.8)

plt.title('Elements of a Balanced Lifestyle by Importance', fontsize=16)
plt.axis('off')

plt.show()