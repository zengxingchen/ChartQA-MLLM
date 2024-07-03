
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import squarify

# Define the data
data = {
    'Field': [
        'AI Research', 'Quantum Computing', 'Blockchain Technology', 
        'Cybersecurity', 'IoT (Internet of Things)', '5G Technology', 
        'Augmented Reality', 'Virtual Reality', 'Autonomous Vehicles', 
        'Biotechnology', 'Clean Energy', 'Nanotechnology', 
        'Robotics', 'Genomics', '3D Printing'
    ],
    'Funding (Millions)': [
        5000, 4200, 3800, 3500, 3000, 2900, 2500, 2400, 
        2200, 2100, 2000, 1900, 1800, 1700, 1600
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color palette
colors = [
    '#FF5733', '#FFC300', '#FF0000', '#C70039', '#900C3F', 
    '#DAF7A6', '#FFC0CB', '#9B59B6', '#3498DB', '#85C1E9', 
    '#16A085', '#138D75', '#7D3C98', '#F39C12', '#2E4053'
]

# Define size of the figure
plt.figure(figsize=(18, 10))

# Plot the treemap with the specified colors and data
squarify.plot(sizes=df['Funding (Millions)'], label=df['Field'], color=colors, alpha=0.8)

plt.title('Funding Allocation in Future Technologies (in Millions)', fontsize=22, pad=20)
plt.axis('off')
plt.show()