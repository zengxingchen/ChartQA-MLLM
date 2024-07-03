
import matplotlib.pyplot as plt
import squarify

# Data
species = [
    'African Elephant', 'Blue Whale', 'Giant Panda', 'Mountain Gorilla', 'Red Panda', 'Snow Leopard', 
    'Tiger', 'Bald Eagle', 'Gray Wolf', 'Green Sea Turtle', 'Orangutan', 'Jaguar', 'African Lion', 
    'Humpback Whale', 'Koala', 'Chimpanzee', 'Giraffe', 'Polar Bear', 'Siberian Tiger'
]
estimated_population = [
    415000, 10000, 1864, 1063, 10000, 4000, 3900, 316000, 300000, 85000, 104700, 17300, 
    20000, 84000, 80000, 172700, 68000, 26000, 540
]
color_code = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
    '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22'
]

# Plot
plt.figure(figsize=(16, 12))
squarify.plot(sizes=estimated_population, label=species, color=color_code, alpha=0.7)
plt.title('Estimated Populations of Various Animal Species', fontsize=22, pad=40)
plt.axis('off')
plt.show()