
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Field': ['Novel Writing', 'Poetry', 'Screenwriting', 'Essay Writing', 'Playwriting', 'Literary Criticism',
              'Short Stories', 'Travel Writing', 'Creative Nonfiction', 'Technical Writing', 'Biographies', 'Journalism', 'Autobiographies'],
    'Funding': [300, 180, 250, 140, 160, 110, 130, 90, 210, 170, 150, 200, 190]
})

# Custom colors for the treemap
colors = ['#FFA07A', '#20B2AA', '#778899', '#FF6347', '#4682B4', '#DAA520', '#32CD32', '#8A2BE2', '#FF4500', '#00CED1', '#D2691E', '#7FFF00', '#FF69B4']

# Create a figure and a set of subplots
plt.figure(figsize=(18, 10))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Funding'], label=df['Field'], color=colors, alpha=0.8)

plt.title("Distribution of Funding in Literary Fields", fontsize=24, fontweight='bold')
plt.axis('off')  # Disable the axis

plt.show()