
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Activity': ['Running', 'Cycling', 'Swimming', 'Yoga', 'Strength Training', 'Dancing', 
                 'Hiking', 'Rowing', 'Pilates', 'Jump Rope', 'Others'],
    'Calorie Burn per Hour': [600, 500, 700, 200, 400, 300, 550, 650, 250, 750, 100]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#FF5733', '#33FF57', '#3357FF', '#F7DC6F', '#BB8FCE', 
          '#5DADE2', '#48C9B0', '#F4D03F', '#DC7633', '#AAB7B8', '#E74C3C']

# Plot
plt.figure(figsize=(18, 12))
squarify.plot(sizes=df['Calorie Burn per Hour'], label=df['Activity'], color=colors, alpha=0.8)
plt.title('Average Calorie Burn per Hour by Physical Activity', fontsize=22, fontweight='bold')
plt.axis('off')  # Removes the axes to create a treemap
plt.show()