
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Category': ['Mental Health', 'Nutrition', 'Exercise', 'Sleep', 'Stress Management', 'Cognitive Therapy', 
                 'Meditation', 'Work-Life Balance', 'Public Health', 'Psychiatry', 'Clinical Psychology', 
                 'Neuroscience', 'Child Development', 'Substance Abuse', 'Health Policy', 'Positive Psychology', 
                 'Psychological Research', 'Counseling', 'Health Education', 'Behavioral Psychology'],
    'Value': [450, 420, 400, 380, 360, 340, 320, 300, 280, 260, 240, 220, 200, 180, 160, 140, 120, 100, 80, 60]
})

# Custom colors for the treemap
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3', '#1b9e77', 
          '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d', '#666666', '#1f78b4', '#33a02c', 
          '#fb9a99', '#e31a1c']

# Create a figure and a set of subplots
plt.figure(figsize=(24, 16))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Value'], label=df['Category'], color=colors, alpha=0.8)

plt.title("Health & Psychology Value Distribution", fontsize=28, fontweight='bold', pad=30)
plt.axis('off')  # Disable the axis

plt.show()