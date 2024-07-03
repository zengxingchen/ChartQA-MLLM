
import matplotlib.pyplot as plt

data = {
    'Topic': ['Natural History Museum', 'Art Gallery', 'Science Museum', 'Modern Art Museum', 
              'Children\'s Museum', 'Historical Museum', 'Cultural Heritage Museum', 
              'Space Exploration Museum', 'Aquarium', 'Zoo', 'Botanical Garden', 
              'Dinosaur Museum', 'War Museum', 'Automobile Museum', 'Fashion Museum', 
              'Ethnographic Museum'],
    'Number of Exhibits': [95, 150, 120, 200, 60, 80, 110, 70, 130, 170, 90, 55, 75, 85, 100, 50],
    'Visitors per Year (Millions)': [8.5, 7.2, 5.8, 9.1, 6.3, 7.0, 5.5, 6.8, 8.0, 10.2, 4.9, 6.1, 7.4, 5.7, 6.9, 4.5],
    'Curator Satisfaction (1-10)': [9.0, 8.3, 7.5, 8.9, 9.4, 8.7, 8.2, 9.1, 7.8, 8.4, 7.9, 9.2, 8.1, 8.6, 7.4, 7.7]
}

fig, ax = plt.subplots(figsize=(16, 10))

colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#5733FF', 
          '#FF33A1', '#33FFA1', '#A133FF', '#FFA133', '#A1FF33', 
          '#33A1FF', '#FF5733', '#5733A1', '#33FF57', '#3357FF', 
          '#FF33A1']

for i in range(len(data['Topic'])):
    ax.scatter(data['Number of Exhibits'][i], data['Visitors per Year (Millions)'][i], 
               s=(data['Curator Satisfaction (1-10)'][i] ** 3) * 10, 
               alpha=0.6,
               color=colors[i])

ax.set_title('Museum Exhibits: Number of Exhibits vs Visitors with Curator Satisfaction as Bubble Size', fontsize=18, pad=20)
ax.set_xlabel('Number of Exhibits', fontsize=14)
ax.set_ylabel('Visitors per Year (Millions)', fontsize=14)
ax.grid(True)

plt.show()