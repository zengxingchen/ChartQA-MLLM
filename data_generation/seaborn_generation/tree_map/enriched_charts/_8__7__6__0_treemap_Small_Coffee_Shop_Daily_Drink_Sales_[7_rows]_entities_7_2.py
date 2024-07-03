
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data for treemap
data = {
    'Topic': [
        'Modern Art', 'Contemporary Dance', 'Digital Art', 'Classical Music',
        'Sculpture', 'Photography', 'Theater', 'Film',
        'Opera', 'Ballet', 'Street Art', 'Jazz Music',
        'Abstract Art', 'Pop Art', 'Graffiti', 'Performance Art',
        'Ceramics', 'Illustration', 'Graphic Design', 'Calligraphy',
        'Video Art', 'Animation', 'Installation Art', 'Mixed Media',
        'Conceptual Art', 'New Media Art', 'Sound Art', 'Light Art',
        'Experimental Music'
    ],
    'Popularity': [
        600, 450, 400, 380, 350, 330, 320, 310, 300, 290,
        280, 270, 260, 250, 240, 230, 220, 210, 200, 190,
        180, 170, 160, 150, 140, 130, 120, 110, 100
    ]
}

# Convert the data into DataFrame
df = pd.DataFrame(data)

# Define color palette
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1', 
    '#FF5733', '#57FF33', '#33A1FF', '#A1FF33', '#5733FF', '#FF33A1', 
    '#33FFA1', '#FF5733', '#33A1FF', '#A133FF', '#A1FF33', '#33FFA1', 
    '#5733FF', '#FF33A1', '#33FF57', '#FF5733', '#33A1FF', '#A133FF', 
    '#33FFA1', '#A1FF33', '#5733FF', '#FF33A1', '#33FF57'
]

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(18, 12))

# Create a treemap
squarify.plot(sizes=df['Popularity'], label=df['Topic'], alpha=0.8, color=colors)

# Remove the axes
plt.axis('off')

# Add a title
plt.title('Popularity of Various Art Forms', fontsize=24, pad=30)

# Show the plot
plt.show()