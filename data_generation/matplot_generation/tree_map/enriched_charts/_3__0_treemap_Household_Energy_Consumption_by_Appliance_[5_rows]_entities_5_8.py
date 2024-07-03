import matplotlib.pyplot as plt
import squarify

# Data
Category = ['Renaissance', 'Baroque', 'Classical', 'Romanticism', 'Impressionism', 'Expressionism', 'Surrealism', 
            'Abstract', 'Cubism', 'Dada', 'Pop Art', 'Futurism', 'Others']
Value = [23.1, 18.5, 16.2, 14.7, 12.9, 9.8, 7.3, 6.8, 5.7, 4.5, 3.9, 3.3, 2.4]
Color = ['#FF6347', '#4682B4', '#32CD32', '#FF4500', '#1E90FF', '#00FA9A', '#FFD700', '#20B2AA', 
         '#FF69B4', '#BA55D3', '#9370DB', '#8B0000', '#CD853F']

# Plot
plt.figure(figsize=(14, 10))
squarify.plot(sizes=Value, label=Category, color=Color, alpha=0.75)
plt.title('Popular Art Movements by Prominence', fontsize=18)
plt.axis('off')
plt.show()