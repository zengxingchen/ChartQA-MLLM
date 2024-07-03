
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'ResearchArea': ['AI Ethics', 'Quantum Computing', 'Blockchain', 'Virtual Reality', 'Internet of Things', 'Cybersecurity', '5G Networks', 'Smart Cities', 'Autonomous Vehicles', 'Augmented Reality', 'Robotics', 'Digital Health', 'Biotechnology', 'Fintech', 'Renewable Energy', 'Smart Agriculture', 'Advanced Materials'],
    'Publications': [150, 120, 180, 100, 130, 170, 110, 140, 160, 90, 200, 115, 135, 125, 145, 155, 175],
    'H-Index': [85, 95, 70, 65, 80, 90, 75, 85, 78, 60, 92, 88, 83, 77, 89, 86, 91],
    'ImpactFactor': [5.6, 8.1, 6.4, 4.9, 5.2, 7.3, 6.0, 5.8, 7.1, 4.5, 7.8, 6.6, 6.2, 6.9, 8.0, 5.4, 7.5]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
bubble_chart = sns.scatterplot(
    data=df, 
    x='Publications', 
    y='H-Index', 
    size='ImpactFactor', 
    sizes=(100, 1000), 
    hue='ResearchArea', 
    palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', '#FFC300', '#DAF7A6', '#900C3F', '#C70039', '#581845', '#C0C0C0', '#808080', '#800000', '#808000', '#00FF00', '#00FFFF', '#000080', '#FF00FF']
)

plt.title('Research Impact in Future Technologies & Society', fontsize=18)
plt.xlabel('Number of Publications', fontsize=14)
plt.ylabel('H-Index', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

plt.tight_layout()
plt.show()