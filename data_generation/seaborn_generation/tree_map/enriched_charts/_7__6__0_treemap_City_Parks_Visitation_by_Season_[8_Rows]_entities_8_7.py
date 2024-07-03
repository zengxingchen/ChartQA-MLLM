
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataframe with the new topic and data points
data = {
    'Innovation': ['Artificial Intelligence', 'Quantum Computing', 'Blockchain', '5G Technology', 'Internet of Things', 'Augmented Reality', 'Virtual Reality', 'Edge Computing', 'Biometric Security', 'Others'],
    'Market Share': [25, 20, 15, 10, 8, 7, 5, 4, 3, 3]
}

df = pd.DataFrame(data)

# Define a new color list for better visual appeal
colors = ['#FF5733', '#33FF57', '#3357FF', '#F4FF33', '#FF33F6', '#33FFF2', '#F2FF33', '#FF8B33', '#8B33FF', '#33FF8B']

# Plot the treemap with modified dimensions
plt.figure(figsize=(24, 12))
squarify.plot(sizes=df['Market Share'], label=df['Innovation'], color=colors, alpha=0.8)

# Add title to the plot
plt.title('Market Share of Future Technologies in 2023', fontsize=24)

# Remove axes for a cleaner look
plt.axis('off')

plt.show()