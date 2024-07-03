
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data for treemap
data = {
    'Topic': [
        'Politics', 'Governance', 'Public Policy', 'Elections', 'Legislation',
        'Diplomacy', 'Public Opinion', 'Campaigns', 'Government Spending', 
        'International Relations', 'Constitutional Law', 'Political Philosophy'
    ],
    'Values': [
        150, 80, 200, 170, 220,
        130, 250, 90, 180, 160,
        140, 210
    ]
}

# Convert the data into DataFrame
df = pd.DataFrame(data)

# Define color palette
colors = [
    '#4CAF50', '#2196F3', '#FF5722', '#FFC107', '#9C27B0',
    '#00BCD4', '#E91E63', '#FF9800', '#8BC34A', '#3F51B5',
    '#FFEB3B', '#607D8B'
]

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(14, 10))

# Create a treemap
squarify.plot(sizes=df['Values'], label=df['Topic'], alpha=0.8, color=colors)

# Remove the axes
plt.axis('off')

# Add a title
plt.title('Political Topics and Their Impact Values', fontsize=20)

# Show the plot
plt.show()