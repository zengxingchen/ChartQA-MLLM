
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Region': ['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Australia/Oceania', 'Antarctica'],
    'Population': [4660000000, 1340000000, 747636026, 592072212, 430759766, 42677813, 1000],
    'Area': [44579000, 30370000, 10180000, 24709000, 17840000, 8611800, 14000000]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#FF5733', '#33FF57', '#3357FF', '#F0FF33', '#FF33A8', '#33FFF0', '#A833FF']

# Plot the Treemap
plt.figure(figsize=(14, 10))
squarify.plot(sizes=df['Area'], label=df['Region'], color=colors, alpha=0.8)
plt.title('Continent Sizes by Area', fontsize=20)
plt.axis('off')
plt.show()