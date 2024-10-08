
import matplotlib.pyplot as plt

scores = [
    78, 85, 88, 90, 92, 94, 95, 96, 98, 100, 102, 104, 105, 107, 108, 110, 
    112, 115, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 
    142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 
    170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 
    198, 200
]

bins = [75, 95, 115, 135, 155, 175, 195, 215]

plt.figure(figsize=(10, 6))
plt.hist(scores, bins=bins, color='#1E90FF', edgecolor='black', linewidth=2, orientation='horizontal')

plt.title('Test Scores Distribution')
plt.xlabel('Frequency')
plt.ylabel('Scores')

plt.yticks([85, 105, 125, 145, 165, 185, 205])

plt.show()