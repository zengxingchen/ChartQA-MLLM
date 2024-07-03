
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Seaborn for improved visuals
import seaborn as sns
sns.set(style="whitegrid")

# Create the dataframe
data = '''
category,sub_category,value
Sports & Fitness,Running,300
Sports & Fitness,Cycling,250
Sports & Fitness,Swimming,220
Sports & Fitness,Weightlifting,200
Sports & Fitness,Yoga,190
Sports & Fitness,Pilates,180
Sports & Fitness,Martial Arts,170
Sports & Fitness,Boxing,160
Sports & Fitness,Hiking,150
Sports & Fitness,Rock Climbing,140
Sports & Fitness,Skiing,130
Sports & Fitness,Snowboarding,120
Sports & Fitness,Gymnastics,110
Sports & Fitness,Dance,100
Sports & Fitness,Rowing,90
Sports & Fitness,Tennis,80
Sports & Fitness,Basketball,70
Sports & Fitness,Football,60
Sports & Fitness,Baseball,50
Sports & Fitness,Volleyball,40
'''

# Simulate reading a CSV file
from io import StringIO
df = pd.read_csv(StringIO(data))

# Prepare data
sizes = df['value'].values.tolist()
label_texts = df['sub_category'].map(str) + " (" + df['value'].astype(str) + ")"

# Color list
colors = [
    '#e6194b', '#3cb44b', '#ffe119', '#0082c8', '#f58231',
    '#911eb4', '#46f0f0', '#f032e6', '#d2f53c', '#fabebe',
    '#008080', '#e6beff', '#aa6e28', '#fffac8', '#800000',
    '#aaffc3', '#808000', '#ffd8b1', '#000080', '#808080'
]

# Create a figure and a set of subplots
fig, ax = plt.subplots(1, figsize=(16, 10))

# Squarify: plot a treemap of the data
squarify.plot(sizes=sizes, label=label_texts, color=colors, alpha=.7, ax=ax)

# Remove the axes
plt.axis('off')

# Set the title of the plot
plt.title('Market Share by Sports & Fitness Subcategories', fontsize=22, y=1.05)

# Show
plt.show()