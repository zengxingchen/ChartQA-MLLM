
import matplotlib.pyplot as plt

countries = [
    'Kenya', 'Ethiopia', 'Jamaica', 'USA', 'United Kingdom', 'China',
    'Brazil', 'Russia', 'Australia', 'Germany', 'France', 'Japan',
    'South Korea', 'India', 'Canada'
]

average_running_speeds = [
    20.5, 19.8, 22.4, 18.7, 17.3, 16.5, 17.8, 16.1, 18.2, 17.0, 17.6, 15.9,
    15.7, 16.0, 17.2
]

colors = [
    '#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00',
    '#ffff33', '#a65628', '#f781bf', '#999999', '#66c2a5',
    '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f'
]

plt.figure(figsize=(12, 10))
plt.bar(countries, average_running_speeds, color=colors, width=0.6)
plt.ylabel('Average Running Speed (km/h)')
plt.title('Average Running Speed by Country')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()