
import matplotlib.pyplot as plt

cities = [
    "Bangkok", "Paris", "London", "Dubai", "Singapore", "Kuala Lumpur",
    "New York", "Istanbul", "Tokyo", "Antalya", "Seoul", "Phuket",
    "Mecca", "Hong Kong", "Barcelona", "Pattaya", "Palma de Mallorca",
    "Osaka", "Bali", "Las Vegas"
]
tourists = [
    22.8, 19.1, 19.0, 16.7, 14.7, 13.8, 13.5, 13.4, 12.5, 12.4, 12.1, 11.6,
    10.0, 9.4, 9.3, 9.1, 8.8, 8.4, 8.2, 7.5
]

plt.figure(figsize=(12, 8))
plt.barh(cities, tourists, color=[
    '#ff5733', '#33ff57', '#3357ff', '#ff33a1', '#a133ff', '#33fff5',
    '#f5ff33', '#a1ff33', '#33ffa1', '#ffa133', '#ff3357', '#5733ff',
    '#33a1ff', '#a1f533', '#ff5733', '#33a1ff', '#a1ff33', '#ff33a1',
    '#33ff57', '#ff5733'], height=0.6)

plt.xlabel('Annual Tourist Arrivals (Million)', fontsize=14)
plt.title('Top 20 Cities by Annual Tourist Arrivals', fontsize=16, pad=20)
plt.xlim(5, 25)
plt.tight_layout()
plt.show()