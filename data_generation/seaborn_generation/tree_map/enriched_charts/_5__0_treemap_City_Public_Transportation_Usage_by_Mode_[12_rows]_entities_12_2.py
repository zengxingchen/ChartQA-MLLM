
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Seaborn for improved visuals
import seaborn as sns
sns.set(style="whitegrid")

# Read the data
data = '''
category,sub_category,value
Health & Psychology,Mental Health,300
Health & Psychology,Physical Fitness,200
Health & Psychology,Nutrition,150
Health & Psychology,Sleep,90
Health & Psychology,Stress Management,95
Health & Psychology,Meditation,60
Health & Psychology,Wellness,180
Health & Psychology,Yoga,140
Health & Psychology,Therapy,110
Health & Psychology,Health Supplements,70
Health & Psychology,Healthy Eating,80
Health & Psychology,Exercise,60
Health & Psychology,Cardio,50
Health & Psychology,Strength Training,80
Health & Psychology,HIIT,200
Health & Psychology,Weight Loss,100
Health & Psychology,Recovery,120
Health & Psychology,Flexibility,130
Health & Psychology,Mindfulness,110
Health & Psychology,Preventive Care,140
'''

# Simulate reading a CSV file
from io import StringIO
df = pd.read_csv(StringIO(data))

# Prepare data
sizes = df['value'].values.tolist()
label_texts = df['sub_category'].map(str) + " (" + df['value'].astype(str) + ")"

# Color list
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357',
    '#57FFD5', '#D557FF', '#FFD557', '#FF57D5', '#D5FF57',
    '#5733FF', '#F733FF', '#FF3374', '#74FF33', '#3374FF',
    '#FF9933', '#33FF99', '#9933FF', '#3399FF', '#9933FF'
]

# Create a figure and a set of subplots
fig, ax = plt.subplots(1, figsize=(16, 10))

# Squarify: plot a treemap of the data
squarify.plot(sizes=sizes, label=label_texts, color=colors, alpha=.7, ax=ax)

# Remove the axes
plt.axis('off')

# Set the title of the plot
plt.title('Market Share by Health & Psychology Subcategories', fontsize=20)

# Show
plt.show()