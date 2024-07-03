
import matplotlib.pyplot as plt
import squarify

labels = ['Modernism', 'Surrealism', 'Impressionism', 'Romanticism', 'Realism', 'Post-Impressionism', 'Baroque', 'Renaissance', 'Expressionism', 'Symbolism', 'Neoclassicism', 'Gothic', 'Naturalism', 'Art Nouveau', 'Cubism']
sizes = [20, 15, 12, 11, 10, 8, 7, 6, 5, 4, 4, 3, 3, 2, 2]
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc948', '#b07aa1', '#ff9da7', '#9c755f', '#bab0ac', '#fabfd2', '#fdc086', '#78c679', '#88cdbc', '#d9a6d2']

plt.figure(figsize=(14, 12))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)
plt.title('Artistic Movements Across History', fontsize=20, y=1.05)
plt.axis('off')
plt.show()