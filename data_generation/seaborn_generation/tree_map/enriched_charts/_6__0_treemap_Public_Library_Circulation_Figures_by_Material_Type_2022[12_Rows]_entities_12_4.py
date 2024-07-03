
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Aspect': ['Mental Health', 'Physical Health', 'Nutrition', 'Sleep', 'Stress Management', 'Exercise', 
               'Cognitive Function', 'Social Relationships', 'Emotional Well-being', 'Addiction Recovery', 
               'Mindfulness', 'Spiritual Health'],
    'Percentage': [0.15, 0.20, 0.13, 0.12, 0.10, 0.10, 0.08, 0.07, 0.05, 0.04, 0.03, 0.02]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#FF5733', '#33FFBD', '#3358FF', '#D433FF', '#FFC133', '#33FF57', '#8C33FF', '#33D4FF', 
          '#FF335E', '#33FF8E', '#FF8C33', '#335CFF']

# Plot the Treemap
plt.figure(figsize=(14, 10))
squarify.plot(sizes=df['Percentage'], label=df['Aspect'], color=colors, alpha=0.8)
plt.title('Aspects of Health & Psychology', fontsize=20)
plt.axis('off')
plt.show()