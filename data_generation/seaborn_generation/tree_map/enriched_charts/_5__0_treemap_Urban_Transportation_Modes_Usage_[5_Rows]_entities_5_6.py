
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Topic': ['Cardio Fitness', 'Yoga & Meditation', 'Strength Training', 'Marathons', 'Cycling', 'Swimming', 'Martial Arts', 
              'Dance', 'Gymnastics', 'Pilates', 'Hiking', 'CrossFit', 'Rock Climbing'],
    'Funding': [320, 280, 220, 180, 210, 160, 140, 200, 110, 150, 190, 170, 130]
})

# Custom colors for the treemap
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF69B4', '#20B2AA', '#DAA520', '#FF4500', '#2E8B57', '#4169E1', '#BA55D3', '#CD5C5C']

# Create a figure and a set of subplots
plt.figure(figsize=(18, 10))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Funding'], label=df['Topic'], color=colors, alpha=0.8)

plt.title("Distribution of Sports & Fitness Funding by Activity", fontsize=24, fontweight='bold')
plt.axis('off')  # Disable the axis

plt.show()