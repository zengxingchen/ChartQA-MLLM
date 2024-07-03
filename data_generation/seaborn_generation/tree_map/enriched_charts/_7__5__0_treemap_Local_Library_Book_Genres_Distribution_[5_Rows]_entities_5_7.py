
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'Country': ['USA', 'India', 'China', 'Germany', 'Brazil', 'UK', 'France', 'Japan', 
                'Russia', 'Italy', 'Canada', 'Australia', 'Spain', 'Mexico', 'South Africa',
                'South Korea', 'Argentina', 'Netherlands', 'Sweden', 'Norway'],
    'Music Festival Attendance (Millions)': [25.4, 22.3, 18.7, 15.6, 12.4, 10.8, 9.7, 8.2, 
                                             7.6, 6.3, 5.8, 4.9, 4.3, 3.5, 2.7, 2.4, 2.1, 
                                             1.9, 1.5, 1.2]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#FF4500', '#FF8C00', '#FFD700', '#ADFF2F', '#32CD32', 
          '#00FA9A', '#00CED1', '#1E90FF', '#4169E1', '#8A2BE2', 
          '#BA55D3', '#FF1493', '#FF69B4', '#FF6347', '#FFA07A',
          '#20B2AA', '#778899', '#4682B4', '#D2691E', '#B0C4DE']

# Plot
plt.figure(figsize=(30, 15))
squarify.plot(sizes=df['Music Festival Attendance (Millions)'], label=df['Country'], color=colors, alpha=0.8)
plt.title('Global Music Festival Attendance by Country', fontsize=28, fontweight='bold')
plt.axis('off')  # Removes the axes to create a treemap
plt.show()