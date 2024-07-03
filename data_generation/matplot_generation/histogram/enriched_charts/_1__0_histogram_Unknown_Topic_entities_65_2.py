import matplotlib.pyplot as plt

distance_data = [
    3.2, 2.9, 5.0, 4.7, 4.1, 3.9, 2.3, 6.8, 3.6, 5.1, 5.3, 3.4, 4.5, 6.1, 3.8, 4.4, 
    2.7, 6.0, 4.9, 5.8, 5.5, 2.8, 4.3, 3.5, 6.3, 3.1, 4.8, 6.5, 3.0, 5.2, 6.2, 3.3, 
    5.4, 4.2, 5.9, 4.0, 6.7, 4.6, 5.6, 2.5, 5.7, 6.4, 2.6, 6.6, 3.7, 2.4, 2.2, 2.1, 
    6.9, 7.0, 7.2, 7.4, 7.5, 7.3, 2.0, 7.1
]

plt.figure(figsize=(12, 6))
plt.hist(distance_data, bins=20, color="#FF5733", orientation='vertical', rwidth=0.8)
plt.title('Distribution of Distances in a Running Competition', pad=20)
plt.xlabel('Distance (km)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--')
plt.show()