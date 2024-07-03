
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import squarify

# Define the data
data = {
    'Company': [
        'Pfizer', 'Johnson & Johnson', 'Roche', 'Novartis', 
        'Merck', 'Sanofi', 'AbbVie', 'GSK', 
        'Bristol-Myers Squibb', 'AstraZeneca', 'Eli Lilly', 
        'Amgen', 'Takeda', 'Bayer', 'Novo Nordisk', 
        'Regeneron', 'Moderna', 'Biogen', 
        'Gilead Sciences', 'CSL'
    ],
    'Market Share (Billion USD)': [
        850, 820, 800, 790, 780, 760, 750, 740, 730, 
        720, 710, 700, 690, 680, 670, 660, 650, 640, 
        630, 620
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color palette
colors = [
    '#8B0000', '#FF8C00', '#FF4500', '#FFD700',
    '#ADFF2F', '#32CD32', '#00FF00', '#00FA9A',
    '#20B2AA', '#87CEEB', '#4169E1', '#6A5ACD',
    '#8A2BE2', '#FF00FF', '#FF1493', '#C71585',
    '#DB7093', '#FF6347', '#FFD700', '#FF4500'
]

# Define size of the figure
plt.figure(figsize=(20, 12))

# Plot the treemap with the specified colors and data
squarify.plot(sizes=df['Market Share (Billion USD)'], label=df['Company'], color=colors, alpha=0.8)

plt.title('Market Share of Top Pharmaceuticals (in Billion USD)', fontsize=22, pad=20)
plt.axis('off')
plt.show()