
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Seaborn for improved visuals
import seaborn as sns
sns.set(style="whitegrid")

# Create the dataframe
data = '''
category,sub_category,value
Entertainment & Leisure,Movies,350
Entertainment & Leisure,Music,270
Entertainment & Leisure,Video Games,320
Entertainment & Leisure,Books,230
Entertainment & Leisure,TV Shows,210
Entertainment & Leisure,Podcasts,190
Entertainment & Leisure,Live Events,170
Entertainment & Leisure,Streaming Services,240
Entertainment & Leisure,Board Games,130
Entertainment & Leisure,Comics,140
Entertainment & Leisure,Theme Parks,160
Entertainment & Leisure,Concerts,180
Entertainment & Leisure,Art Exhibitions,150
Entertainment & Leisure,Theater,200
Entertainment & Leisure,Opera,120
Entertainment & Leisure,Museums,110
Entertainment & Leisure,Amusement Parks,100
Entertainment & Leisure,Virtual Reality,90
Entertainment & Leisure,Augmented Reality,80
Entertainment & Leisure,Escape Rooms,70
'''

# Simulate reading a CSV file
from io import StringIO
df = pd.read_csv(StringIO(data))

# Prepare data
sizes = df['value'].values.tolist()
label_texts = df['sub_category'].map(str) + " (" + df['value'].astype(str) + ")"

# Color list
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
    '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5'
]

# Create a figure and a set of subplots
fig, ax = plt.subplots(1, figsize=(18, 12))

# Squarify: plot a treemap of the data
squarify.plot(sizes=sizes, label=label_texts, color=colors, alpha=.7, ax=ax)

# Remove the axes
plt.axis('off')

# Set the title of the plot
plt.title('Market Share by Entertainment & Leisure Subcategories', fontsize=22)

# Show
plt.show()