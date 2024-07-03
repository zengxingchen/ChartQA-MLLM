
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataframe with the new topic and data points
data = {
    'Service': ['Netflix', 'Amazon Prime Video', 'Disney+', 'Hulu', 'HBO Max', 'Apple TV+', 'Paramount+', 'Peacock', 'Discovery+', 'Others'],
    'Market Share': [40, 20, 15, 8, 5, 4, 3, 2, 1, 2]
}

df = pd.DataFrame(data)

# Define a new color list for better visual appeal
colors = ['#FF5733', '#33FF57', '#3357FF', '#F4FF33', '#FF33F6', '#33FFF2', '#F2FF33', '#FF8B33', '#8B33FF', '#33FF8B']

# Plot the treemap with modified dimensions
plt.figure(figsize=(20, 10))
squarify.plot(sizes=df['Market Share'], label=df['Service'], color=colors, alpha=0.8)

# Add title to the plot
plt.title('Streaming Services Market Share in 2023', fontsize=20)

# Remove axes for a cleaner look
plt.axis('off')

plt.show()