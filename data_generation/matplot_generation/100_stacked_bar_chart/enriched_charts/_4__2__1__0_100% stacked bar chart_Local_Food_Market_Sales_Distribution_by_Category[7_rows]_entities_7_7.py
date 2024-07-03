
import matplotlib.pyplot as plt
import numpy as np

categories = ['Solar System Exploration', 'Deep Space Missions', 'Astronomical Phenomena', 'Space Technology', 'Planetary Science', 'Astrobiology', 'Galactic Studies', 'Stellar Research', 'Cosmology', 'Exoplanet Exploration']
segment_A = [22, 25, 28, 26, 30, 24, 22, 23, 24, 26]
segment_B = [18, 20, 22, 24, 20, 26, 28, 27, 25, 24]
segment_C = [30, 25, 20, 25, 25, 25, 25, 25, 26, 25]
segment_D = [30, 30, 30, 25, 25, 25, 25, 25, 25, 25]

totals = np.array(segment_A) + np.array(segment_B) + np.array(segment_C) + np.array(segment_D)
segment_A = np.array(segment_A) / totals * 100
segment_B = np.array(segment_B) / totals * 100
segment_C = np.array(segment_C) / totals * 100
segment_D = np.array(segment_D) / totals * 100

barWidth = 0.75
r = range(len(categories))

plt.figure(figsize=(10, 15))

plt.bar(r, segment_A, color='#1f77b4', edgecolor='white', width=barWidth, label='Segment A')
plt.bar(r, segment_B, bottom=segment_A, color='#ff7f0e', edgecolor='white', width=barWidth, label='Segment B')
plt.bar(r, segment_C, bottom=segment_A + segment_B, color='#2ca02c', edgecolor='white', width=barWidth, label='Segment C')
plt.bar(r, segment_D, bottom=segment_A + segment_B + segment_C, color='#d62728', edgecolor='white', width=barWidth, label='Segment D')

plt.ylabel('Percentage')
plt.title('Distribution of Segments in Astronomy & Space Exploration', pad=20)
plt.xticks(r, categories, rotation=45, ha='right')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()