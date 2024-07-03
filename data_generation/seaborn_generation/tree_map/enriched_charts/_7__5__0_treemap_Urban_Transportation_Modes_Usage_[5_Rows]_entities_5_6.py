
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Topic': ['Artificial Intelligence', 'Quantum Computing', 'Blockchain Technology', 'Cybersecurity', 'Augmented Reality', 
              '5G Networks', 'Internet of Things', 'Biotechnology', 'Autonomous Vehicles', 'Smart Cities', 'Wearable Technology', 
              'Renewable Energy', 'Digital Twins', 'Space Exploration', 'Robotics'],
    'Funding': [450, 400, 350, 300, 280, 260, 240, 220, 200, 180, 160, 140, 120, 100, 80]
})

# Custom colors for the treemap
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#FF8F33', '#33FFA5', '#FF3333', '#33D1FF', '#FF33D1', 
          '#B6FF33', '#FF5733', '#8F33FF', '#33FF6F', '#D133FF']

# Create a figure and a set of subplots
plt.figure(figsize=(20, 12))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Funding'], label=df['Topic'], color=colors, alpha=0.8)

plt.title("Distribution of Future Technologies Funding by Area", fontsize=24, fontweight='bold')
plt.axis('off')  # Disable the axis

plt.show()