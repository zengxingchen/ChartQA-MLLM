
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
new_subscribers = [5.2, 6.1, 7.3, 8.0, 9.5, 10.2, 11.7, 13.4, 12.6, 10.9, 8.8, 7.2]
colors = ['#4B0082', '#FF4500', '#228B22', '#DC143C', '#8A2BE2', '#A52A2A',
          '#FF69B4', '#2F4F4F', '#FFD700', '#00CED1', '#483D8B', '#FF6347']

plt.figure(figsize=(10, 8))
bars = plt.barh(months, new_subscribers, color=colors, edgecolor='black', height=0.6)

plt.xlabel('New Subscribers (Thousands)')
plt.title('Monthly New Subscribers of XYZ Streaming Service in 2023')
plt.xlim(0, max(new_subscribers) + 5)
plt.ylim(-0.5, len(months) - 0.5)  # To ensure no clipping of the bars
plt.tight_layout()

plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()