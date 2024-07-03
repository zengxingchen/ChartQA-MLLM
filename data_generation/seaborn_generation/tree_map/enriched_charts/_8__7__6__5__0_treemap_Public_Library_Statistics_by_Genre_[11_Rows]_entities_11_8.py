
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a data frame with diversified data
df = pd.DataFrame({
    'category': ['AI & Machine Learning', 'AI & Machine Learning', 'AI & Machine Learning', 'AI & Machine Learning',
                 'Robotics', 'Robotics', 'Robotics', 'Robotics',
                 'Internet of Things', 'Internet of Things', 'Internet of Things', 'Internet of Things',
                 'Blockchain', 'Blockchain', 'Blockchain', 'Blockchain',
                 'Quantum Computing', 'Quantum Computing', 'Quantum Computing', 'Quantum Computing',
                 'Biotechnology', 'Biotechnology', 'Biotechnology', 'Biotechnology',
                 'Cybersecurity', 'Cybersecurity', 'Cybersecurity', 'Cybersecurity'],
    'sub_category': ['Deep Learning', 'Neural Networks', 'Computer Vision', 'Natural Language Processing',
                     'Industrial Robots', 'Service Robots', 'Medical Robots', 'Humanoid Robots',
                     'Smart Homes', 'Smart Cities', 'Wearable Devices', 'Connected Cars',
                     'Cryptocurrency', 'Smart Contracts', 'DeFi', 'NFTs',
                     'Qubit Development', 'Quantum Algorithms', 'Quantum Cryptography', 'Quantum Supremacy',
                     'CRISPR', 'Stem Cell Research', 'Bioinformatics', 'Genomics',
                     'Network Security', 'Data Privacy', 'Threat Intelligence', 'Penetration Testing'],
    'value': [1200, 1150, 1100, 1050, 1000, 950, 900, 850, 1300, 1250, 1200, 1150, 1100, 1050, 1000, 950,
              1400, 1350, 1300, 1250, 1200, 1150, 1100, 1050, 1400, 1350, 1300, 1250]
})

# Create a new color list
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF5733', '#33FF57', '#3357FF', '#FF33A6',
          '#FFBD33', '#33FFBD', '#BD33FF', '#FF3333', '#57FF33', '#33FF57', '#5733FF', '#FF3357',
          '#33FF33', '#FF33BD', '#33BDFF', '#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF5733',
          '#33FFBD', '#BD33FF', '#FF3333', '#57FF33']

# Plot
plt.figure(figsize=(26, 14))
squarify.plot(sizes=df['value'], label=df['sub_category'], color=colors, alpha=.8)
plt.title('Key Areas in Future Technologies & Society', fontsize=24, pad=30)
plt.axis('off')
plt.show()