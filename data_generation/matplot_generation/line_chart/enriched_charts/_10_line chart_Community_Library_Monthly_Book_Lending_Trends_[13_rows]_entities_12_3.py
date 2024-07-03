
import matplotlib.pyplot as plt

data = [
    {'Month': 'January', 'Beach Resorts': 300, 'Mountain Retreats': 150, 'Historical Sites': 450, 'City Tours': 500, 'Nature Parks': 200},
    {'Month': 'February', 'Beach Resorts': 320, 'Mountain Retreats': 140, 'Historical Sites': 470, 'City Tours': 520, 'Nature Parks': 210},
    {'Month': 'March', 'Beach Resorts': 340, 'Mountain Retreats': 130, 'Historical Sites': 490, 'City Tours': 540, 'Nature Parks': 220},
    {'Month': 'April', 'Beach Resorts': 360, 'Mountain Retreats': 120, 'Historical Sites': 510, 'City Tours': 560, 'Nature Parks': 230},
    {'Month': 'May', 'Beach Resorts': 380, 'Mountain Retreats': 110, 'Historical Sites': 530, 'City Tours': 580, 'Nature Parks': 240},
    {'Month': 'June', 'Beach Resorts': 400, 'Mountain Retreats': 100, 'Historical Sites': 550, 'City Tours': 600, 'Nature Parks': 250},
    {'Month': 'July', 'Beach Resorts': 420, 'Mountain Retreats': 90, 'Historical Sites': 570, 'City Tours': 620, 'Nature Parks': 260},
    {'Month': 'August', 'Beach Resorts': 440, 'Mountain Retreats': 80, 'Historical Sites': 590, 'City Tours': 640, 'Nature Parks': 270},
    {'Month': 'September', 'Beach Resorts': 460, 'Mountain Retreats': 70, 'Historical Sites': 610, 'City Tours': 660, 'Nature Parks': 280},
    {'Month': 'October', 'Beach Resorts': 480, 'Mountain Retreats': 60, 'Historical Sites': 630, 'City Tours': 680, 'Nature Parks': 290},
    {'Month': 'November', 'Beach Resorts': 500, 'Mountain Retreats': 50, 'Historical Sites': 650, 'City Tours': 700, 'Nature Parks': 300},
    {'Month': 'December', 'Beach Resorts': 520, 'Mountain Retreats': 40, 'Historical Sites': 670, 'City Tours': 720, 'Nature Parks': 310}
]

months = [entry['Month'] for entry in data]
beach_resorts = [entry['Beach Resorts'] for entry in data]
mountain_retreats = [entry['Mountain Retreats'] for entry in data]
historical_sites = [entry['Historical Sites'] for entry in data]
city_tours = [entry['City Tours'] for entry in data]
nature_parks = [entry['Nature Parks'] for entry in data]

plt.figure(figsize=(12, 6))
plt.plot(months, beach_resorts, marker='o', linestyle='-', color='#1f77b4', label='Beach Resorts')
plt.plot(months, mountain_retreats, marker='s', linestyle='--', color='#ff7f0e', label='Mountain Retreats')
plt.plot(months, historical_sites, marker='^', linestyle='-.', color='#2ca02c', label='Historical Sites')
plt.plot(months, city_tours, marker='x', linestyle=':', color='#d62728', label='City Tours')
plt.plot(months, nature_parks, marker='d', linestyle='-', color='#9467bd', label='Nature Parks')

plt.title('Travel & Adventure: Monthly Tourist Visits to Popular Destinations', pad=20)
plt.xlabel('Month')
plt.ylabel('Tourist Visits (Units)')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()