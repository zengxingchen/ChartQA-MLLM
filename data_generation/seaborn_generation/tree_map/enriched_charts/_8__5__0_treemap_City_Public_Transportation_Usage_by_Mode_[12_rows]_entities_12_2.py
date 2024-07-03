
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Seaborn for improved visuals
import seaborn as sns
sns.set(style="whitegrid")

# Data
data = '''
category,sub_category,value
Entertainment & Leisure,Movies,450
Entertainment & Leisure,Music,320
Entertainment & Leisure,Video Games,280
Entertainment & Leisure,Books,190
Entertainment & Leisure,Board Games,120
Entertainment & Leisure,Live Shows,150
Entertainment & Leisure,Concerts,210
Entertainment & Leisure,Theater,170
Entertainment & Leisure,Amusement Parks,140
Entertainment & Leisure,Museums,110
Entertainment & Leisure,Festivals,130
Entertainment & Leisure,TV Shows,220
Entertainment & Leisure,Streaming Services,300
Entertainment & Leisure,Podcasts,90
Entertainment & Leisure,Escape Rooms,80
Entertainment & Leisure,Art Exhibitions,60
Entertainment & Leisure,Stand-Up Comedy,100
Entertainment & Leisure,Circus,70
Entertainment & Leisure,Zoos,50
Entertainment & Leisure,Parades,200
'''

# Simulate reading a CSV file
from io import StringIO
df = pd.read_csv(StringIO(data))

# Prepare data
sizes = df['value'].values.tolist()
label_texts = df['sub_category'].map(str) + " (" + df['value'].astype(str) + ")"

# Color list
colors = [
    '#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700',
    '#FF69B4', '#8A2BE2', '#7FFF00', '#DC143C', '#00FFFF',
    '#FF7F50', '#00FA9A', '#8B4513', '#FF4500', '#DA70D6',
    '#EEE8AA', '#98FB98', '#AFEEEE', '#DB7093', '#FFD700'
]

# Create a figure and a set of subplots
fig, ax = plt.subplots(1, figsize=(18, 12))

# Squarify: plot a treemap of the data
squarify.plot(sizes=sizes, label=label_texts, color=colors, alpha=.7, ax=ax)

# Remove the axes
plt.axis('off')

# Set the title of the plot
plt.title('Market Share by Entertainment & Leisure Subcategories', fontsize=24)

# Show
plt.show()