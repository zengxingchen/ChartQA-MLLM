
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
tourist_arrivals = [1500, 1600, 1550, 1650, 1700, 1800, 1750, 1900, 1850, 1950, 2000, 2100]

plt.figure(figsize=(14, 7))

plt.plot(months, tourist_arrivals, marker='o', linestyle='-', color='#FF6347')  # Tomato color

for i, arrivals in enumerate(tourist_arrivals):
    plt.annotate(str(arrivals), xy=(months[i], arrivals), xytext=(5, 5), textcoords='offset points')

plt.title('Monthly Tourist Arrivals', pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Tourists')

plt.show()