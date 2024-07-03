
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Activity': ['Running', 'Yoga', 'Cycling', 'Swimming', 'Hiking', 'Weightlifting', 'Tennis', 'Basketball', 
                 'Soccer', 'Baseball', 'Golf', 'Boxing'],
    'Participants': [12000, 8500, 9000, 7500, 6700, 5400, 5800, 8200, 15000, 6900, 5000, 4100]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(16, 10))
colors = ["#ff6f69", "#ffcc5c", "#88d8b0", "#c7f464", "#4e4e4e", "#6b5b95", "#feb236", "#d64161", "#ff7b25", "#3fb0ac", "#bc5a45", "#405d27"]
squarify.plot(sizes=df['Participants'], label=df['Activity'], alpha=0.8, color=colors)
plt.title('Participation in Various Fitness Activities', fontsize=20)
plt.axis('off')
plt.show()