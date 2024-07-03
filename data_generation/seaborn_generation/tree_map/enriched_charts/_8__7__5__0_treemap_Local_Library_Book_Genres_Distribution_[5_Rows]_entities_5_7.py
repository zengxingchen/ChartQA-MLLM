
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Country': ['USA', 'China', 'UK', 'Germany', 'Japan', 'France', 'India', 'Canada', 
                'Australia', 'Italy', 'Spain', 'South Korea', 'Brazil', 'Netherlands', 
                'Sweden', 'Norway', 'Russia', 'Mexico', 'Argentina', 'South Africa'],
    'Book Sales (Millions)': [150.4, 124.7, 97.5, 86.3, 74.8, 65.2, 57.9, 45.6, 39.7, 
                              32.4, 29.5, 24.8, 21.3, 18.6, 15.9, 12.7, 11.4, 9.6, 8.3, 6.9]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFA8', 
          '#A833FF', '#FF5733', '#57FF33', '#5733FF', '#33A8FF', 
          '#A8FF33', '#FF3357', '#FF5733', '#33FFA8', '#A833FF',
          '#FFA833', '#33A8FF', '#33FF57', '#5733FF', '#FF33A8']

# Plot
plt.figure(figsize=(25, 12))
squarify.plot(sizes=df['Book Sales (Millions)'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Book Sales by Country', fontsize=24, fontweight='bold', pad=20)
plt.axis('off')  # Removes the axes to create a treemap
plt.show()