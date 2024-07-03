
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # You may need to install this package if you haven't already

# Insert the table data here
data = {
    'Type': ['Petrol Small', 'Petrol Medium', 'Petrol Large', 'Diesel Small',
             'Diesel Medium', 'Diesel Large', 'Hybrid Small', 'Hybrid Medium',
             'Hybrid Large', 'Electric Small', 'Electric Medium', 'Electric SUV'],
    'Emissions': [120, 150, 200, 130, 160, 210, 100, 110, 140, 70, 80, 90]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 6))
colors = ["#63b179", "#ffbb42", "#d35f5f", "#8ecae6", "#219ebc", "#ffb703", "#fb8500", "#023047", "#ffd60a", "#8ecae6", "#219ebc", "#023047"]
squarify.plot(sizes=df['Emissions'], label=df['Type'], alpha=0.8, color=colors)
plt.title('Distribution of Vehicle Types by CO2 Emissions')
plt.axis('off')
plt.show()