
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Attraction': ['Grand Canyon', 'Niagara Falls', 'Eiffel Tower', 'Great Wall of China',
                   'Machu Picchu', 'Pyramids of Giza', 'Christ the Redeemer', 'Colosseum',
                   'Statue of Liberty', 'Sydney Opera House', 'Taj Mahal', 'Disneyland'],
    'Visitors': [4500, 6200, 8000, 7500, 5200, 5800, 3000, 7000, 6700, 4900, 8200, 15000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 8))
colors = ["#4e79a7", "#f28e2c", "#e15759", "#76b7b2", "#59a14f", "#edc949", "#af7aa1", "#ff9da7", "#9c755f", "#bab0ac", "#86bcff", "#e08b00"]
squarify.plot(sizes=df['Visitors'], label=df['Attraction'], alpha=0.8, color=colors)
plt.title('Number of Visitors to Various Tourist Attractions', fontsize=16)
plt.axis('off')
plt.show()