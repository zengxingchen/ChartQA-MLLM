
import matplotlib.pyplot as plt
import numpy as np

countries = ['United States', 'China', 'India', 'Germany', 'Japan', 'South Korea', 
             'United Kingdom', 'France', 'Italy', 'Canada', 'Australia', 'Spain', 
             'Brazil', 'Russia', 'Netherlands', 'Sweden', 'Switzerland', 'Israel', 
             'South Africa', 'Saudi Arabia']
research_expenditure = np.array([600, 500, 250, 400, 350, 200, 300, 250, 150, 200, 180, 130, 100, 220, 160, 140, 150, 100, 80, 90])
research_papers = np.array([1100000, 900000, 300000, 500000, 400000, 250000, 350000, 300000, 200000, 230000, 210000, 180000, 150000, 270000, 200000, 170000, 180000, 140000, 90000, 110000])
population = np.array([331, 1402, 1380, 83, 126, 51, 68, 65, 60, 38, 26, 47, 213, 146, 17, 10, 8, 9, 59, 34])

sizes = population * 5

colors = ['#8A2BE2', '#FF4500', '#7CFC00', '#6495ED', '#FF1493', '#00CED1', 
          '#FF8C00', '#B22222', '#ADFF2F', '#FF6347', '#4682B4', '#6A5ACD', 
          '#20B2AA', '#FFD700', '#FF69B4', '#8B0000', '#2E8B57', '#DAA520', 
          '#D2691E', '#8B4513']

plt.figure(figsize=(18, 10))

scatter = plt.scatter(research_papers, research_expenditure, s=sizes, c=colors, alpha=0.7, edgecolors="w", linewidth=2)

plt.title('Scientific Research Expenditure vs Number of Research Papers by Country', pad=20)
plt.xlabel('Number of Research Papers')
plt.ylabel('Scientific Research Expenditure (in billions USD)')

for i, country in enumerate(countries):
    plt.annotate(country, (research_papers[i], research_expenditure[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()