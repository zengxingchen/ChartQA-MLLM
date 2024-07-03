
import matplotlib.pyplot as plt
import squarify

technology_categories = ['Artificial Intelligence', 'Blockchain', 'Cloud Computing', 'Quantum Computing',
                         'Virtual Reality', 'Cybersecurity', 'Augmented Reality', 'Internet of Things',
                         '5G Technology', 'Biotechnology', 'Nanotechnology', 'Fintech']

market_share = [25.7, 15.3, 12.8, 10.2, 8.1, 7.5, 5.2, 4.9, 3.6, 3.2, 2.1, 1.4]

colors = ['#4CAF50', '#2196F3', '#FFEB3B', '#FF9800', '#9C27B0', '#00BCD4', '#E91E63', '#CDDC39', 
          '#FF5722', '#795548', '#607D8B', '#9E9E9E']

plt.figure(figsize=(12, 8))
squarify.plot(sizes=market_share, label=technology_categories, color=colors, alpha=0.7, text_kwargs={'fontsize':9})

plt.title('Market Share of Emerging Technologies in 2023', fontsize=16, pad=20)
plt.axis('off')

plt.show()