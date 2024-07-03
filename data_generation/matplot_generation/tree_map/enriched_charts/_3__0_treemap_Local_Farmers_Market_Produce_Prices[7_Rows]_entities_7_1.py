
import matplotlib.pyplot as plt
import squarify

# Data points
conditions = ['Hypertension', 'Diabetes', 'Asthma', 'COPD', 'Arthritis', 'Depression', 'Anxiety', 
              'Obesity', 'Osteoporosis', 'Heart Disease', 'Stroke', 'Cancer', 'Chronic Kidney Disease', 
              "Alzheimer's", 'Migraine', 'Sleep Disorders', 'Autism', 'Epilepsy', 'Parkinson\'s', 'Others']
prevalence = [25.0, 10.0, 7.5, 5.5, 20.0, 15.0, 18.0, 12.5, 6.0, 8.0, 3.5, 9.0, 4.5, 2.5, 11.0, 13.5, 1.5, 1.2, 1.0, 24.8]

# Color scheme
colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#FF5733', '#C70039', '#900C3F',
          '#581845', '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#FF5733',
          '#C70039', '#900C3F', '#581845', '#D3D3D3']

plt.figure(figsize=(14, 10))
squarify.plot(sizes=prevalence, label=conditions, color=colors, alpha=0.8)

# Chart details
plt.title('Prevalence of Various Health Conditions in 2023', fontsize=18, pad=20)
plt.axis('off')

plt.show()