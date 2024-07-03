
import matplotlib.pyplot as plt
import squarify

# Data points
activities = ['Walking', 'Running', 'Cycling', 'Swimming', 'Yoga', 'Strength Training', 'Hiking', 'Dancing', 'Pilates', 'Aerobics', 'Other']
prevalence = [30.5, 20.0, 15.3, 12.7, 9.5, 4.6, 2.8, 1.9, 1.2, 1.1, 0.4]

# Color scheme
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF1', '#FF3333', '#33FF99', '#FF33EE', '#F3FF33', '#33FFBB', '#D3D3D3']

plt.figure(figsize=(16, 12))
squarify.plot(sizes=prevalence, label=activities, color=colors, alpha=0.7)

# Chart details
plt.title('Prevalence of Various Physical Activities in 2023')
plt.axis('off')

plt.show()