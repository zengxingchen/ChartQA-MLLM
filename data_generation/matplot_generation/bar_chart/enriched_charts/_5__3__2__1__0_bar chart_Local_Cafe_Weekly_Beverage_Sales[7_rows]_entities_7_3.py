
import matplotlib.pyplot as plt

categories = ['Machine Learning', 'Data Science', 'Quantum Computing', 'Blockchain', 'Cybersecurity', 
              'Augmented Reality', 'Virtual Reality', 'Internet of Things', '5G Technology', 
              'Artificial Intelligence', 'Cloud Computing', 'Edge Computing', 'Big Data', 'Robotics', 'Digital Twins']
number_of_publications = [50, 45, 60, 55, 48, 30, 35, 40, 52, 65, 58, 36, 46, 54, 42]

colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357', '#5733FF', '#33FF99', '#FF9933', 
          '#9933FF', '#33FFCC', '#CC33FF', '#FF33CC', '#FF33A1', '#A133FF', '#33FFA1']

plt.figure(figsize=(16, 12))
plt.barh(categories, number_of_publications, color=colors, edgecolor='black', height=0.7)

plt.xlabel('Number of Publications', fontsize=14)
plt.ylabel('Technology', fontsize=14)
plt.title('Number of Publications per Technology in 2023', fontsize=18, pad=20)
plt.xlim(30, 70)

plt.tight_layout()
plt.show()