
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Topic': ['Mental Health', 'Nutrition & Diet', 'Physical Fitness', 'Sleep Science', 'Substance Abuse', 'Mindfulness & Meditation', 
              'Cognitive Therapy', 'Emotional Intelligence', 'Stress Management', 'Child Development', 'Psychological Disorders', 
              'Aging & Gerontology', 'Neuroscience', 'Behavioral Psychology', 'Positive Psychology', 'Health Psychology', 
              'Sports Psychology', 'Clinical Psychology', 'Social Psychology', 'Educational Psychology'],
    'Funding': [500, 450, 430, 410, 390, 370, 350, 330, 310, 290, 270, 250, 230, 210, 190, 170, 150, 130, 110, 90]
})

# Custom colors for the treemap
colors = ['#FF7F50', '#6495ED', '#FF6347', '#FFD700', '#6A5ACD', '#98FB98', '#FF69B4', '#8A2BE2', '#00FA9A', '#FF4500', 
          '#00CED1', '#FF1493', '#32CD32', '#8B0000', '#00BFFF', '#4B0082', '#B22222', '#2E8B57', '#A52A2A', '#DA70D6']

# Create a figure and a set of subplots
plt.figure(figsize=(22, 14))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Funding'], label=df['Topic'], color=colors, alpha=0.8)

plt.title("Distribution of Funding in Health & Psychology", fontsize=26, fontweight='bold', pad=20)
plt.axis('off')  # Disable the axis

plt.show()