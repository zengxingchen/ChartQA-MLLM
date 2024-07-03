
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data
data = {
    'Location': ['Paris', 'New York', 'Tokyo', 'Dubai', 'Rome', 'Bangkok', 'London', 'Istanbul', 'Hong Kong', 
                 'Sydney', 'Singapore', 'Barcelona', 'Amsterdam', 'Los Angeles', 'Madrid', 'Rio de Janeiro', 
                 'Cape Town', 'San Francisco', 'Venice', 'Toronto'],
    'Visitors': [16000, 14000, 12000, 11000, 10000, 9000, 8500, 8000, 7500, 7000, 6800, 6600, 6400, 6200, 6000, 5800, 
                 5600, 5400, 5200, 5000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(18, 12))
colors = ["#f94144", "#f3722c", "#f8961e", "#f9844a", "#f9c74f", "#90be6d", "#43aa8b", "#4d908e", "#577590", 
          "#277da1", "#f94144", "#f3722c", "#f8961e", "#f9844a", "#f9c74f", "#90be6d", "#43aa8b", "#4d908e", 
          "#577590", "#277da1"]
squarify.plot(sizes=df['Visitors'], label=df['Location'], alpha=0.8, color=colors)
plt.title('Top Travel Destinations by Visitor Count', fontsize=24)
plt.axis('off')
plt.show()