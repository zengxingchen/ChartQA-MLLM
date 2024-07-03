
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Destination': ['Beach', 'Mountains', 'City Tours', 'Wildlife Safari', 'Historical Sites', 
                    'Adventure Sports', 'Cruise', 'Desert', 'Countryside', 'Islands', 
                    'Cultural Festivals', 'Rainforest'],
    'Visitors': [8500, 6400, 7200, 5300, 4800, 5900, 7500, 4200, 3000, 6800, 4700, 3500]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(20, 15))
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#aec7e8", "#ffbb78"]
squarify.plot(sizes=df['Visitors'], label=df['Destination'], alpha=0.8, color=colors)
plt.title('Popularity of Travel & Adventure Destinations', fontsize=24)
plt.axis('off')
plt.show()