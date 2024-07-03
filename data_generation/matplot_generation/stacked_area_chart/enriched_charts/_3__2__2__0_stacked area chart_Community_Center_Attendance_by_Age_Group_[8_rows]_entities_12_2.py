
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
flights = [8, 10, 12, 15, 18, 20, 22, 21, 19, 17, 15, 13]
hotel_stays = [14, 16, 18, 20, 22, 24, 26, 25, 23, 21, 19, 17]
car_rentals = [10, 12, 14, 16, 18, 20, 22, 21, 19, 17, 15, 13]
tours = [12, 14, 16, 18, 20, 22, 24, 23, 21, 19, 17, 15]
restaurants = [18, 20, 22, 24, 26, 28, 30, 29, 27, 25, 23, 21]

fig, ax = plt.subplots(figsize=(18, 10))

# Stacking the data
y = np.vstack([flights, hotel_stays, car_rentals, tours, restaurants])

# Colors
colors = ['#1E90FF', '#32CD32', '#FF4500', '#8A2BE2', '#FFD700']

# Plotting the stacked area chart
ax.stackplot(months, y, labels=['Flights', 'Hotel Stays', 'Car Rentals', 'Tours', 'Restaurants'], colors=colors)

# Annotating specific points
ax.annotate('Peak travel season', xy=('July', 30), xytext=('June', 35),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('High restaurant visits', xy=('July', 130), xytext=('August', 140),
            arrowprops=dict(facecolor='blue', shrink=0.05))

# Adding title and labels
ax.set_title('Monthly Travel and Adventure Expenditures', pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Number of Activities')

# Adding legend
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()