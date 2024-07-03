
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Topic': ['Ancient History', 'Modern History', 'Archaeology', 'Medieval History', 'Prehistory', 
              'Military History', 'History of Science', 'Cultural History', 'Economic History', 
              'Social History', 'Historiography', 'Maritime History', 'Environmental History', 
              'Art History', 'History of Medicine', 'Religious History'],
    'Participants': [800, 700, 600, 500, 400, 300, 200, 150, 100, 80, 60, 50, 40, 30, 20, 10],
    'Percentage': [0.20, 0.175, 0.15, 0.125, 0.10, 0.075, 0.05, 0.0375, 0.025, 0.02, 0.015, 0.0125, 0.01, 0.0075, 0.005, 0.0025]
}

df = pd.DataFrame(data)

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', '#FF8333', 
          '#33FF83', '#8333FF', '#FF33E0', '#33FFE0', '#E033FF', '#FFEB33', '#FF33EB', 
          '#33EBFF', '#FF3333']

plt.figure(figsize=(18, 14))
squarify.plot(sizes=df['Percentage'], label=df['Topic'], color=colors, alpha=0.8)
plt.title('Interest in History & Archaeology among Participants', fontsize=22, pad=30)
plt.axis('off')
plt.show()