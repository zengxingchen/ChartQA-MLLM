
import matplotlib.pyplot as plt

categories = ['Renewable Energy', 'Wildlife Conservation', 'Sustainable Agriculture', 'Clean Water Access', 
              'Climate Change Mitigation', 'Pollution Control', 'Deforestation Prevention', 'Ocean Protection', 
              'Air Quality Improvement', 'Green Technology', 'Urban Green Spaces', 'Eco-Friendly Products',
              'Carbon Footprint Reduction', 'Biodiversity Preservation', 'Water Conservation', 'Energy Efficiency',
              'Sustainable Transportation', 'Waste Management', 'Environmental Education', 'Eco-Tourism',
              'Green Building', 'Sustainable Fashion', 'Environmental Policy', 'Sustainable Development',
              'Climate Resilience', 'Recycling Programs']

impact = [95, 87, 80, 89, 73, 67, 88, 60, 75, 70, 58, 65, 92, 85, 79, 82, 74, 68, 66, 77, 81, 63, 84, 90, 76, 70]
support = [92, 84, 78, 85, 70, 72, 86, 65, 74, 68, 62, 64, 88, 83, 77, 80, 73, 71, 69, 76, 79, 61, 82, 87, 75, 72]
respondents = [600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50, 450, 420, 390, 360, 330, 300, 270, 240, 210, 180, 150, 120, 90, 60]

size = [respondent / 2 for respondent in respondents]

fig, ax = plt.subplots(figsize=(14, 10))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8333', '#33FFA1', '#A133FF', '#33FFF2', '#FF5733', '#337FFF', 
          '#8D33FF', '#FFC433', '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8333', '#33FFA1', '#A133FF', '#33FFF2',
          '#FF5733', '#337FFF', '#8D33FF', '#FFC433', '#FF5733', '#33FF57']

for i in range(len(categories)):
    ax.scatter(impact[i], support[i], s=size[i], alpha=0.6, color=colors[i])

for i, txt in enumerate(categories):
    ax.annotate(txt, (impact[i], support[i]), ha='center', va='center')

ax.set_title('Impact and Support in Environmental Initiatives', fontsize=18)
ax.set_xlabel('Impact on Environment', fontsize=14)
ax.set_ylabel('Public Support', fontsize=14)

ax.set_xlim(45, 100)
ax.set_ylim(50, 100)

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.show()