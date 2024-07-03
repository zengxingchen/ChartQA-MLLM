
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
hotel_bookings = [10000, 12000, 15000, 17000, 20000, 22000, 25000, 24000, 23000, 22000, 21000, 20000]
flight_bookings = [8000, 8500, 9500, 10000, 11000, 11500, 12000, 12500, 12000, 11500, 11000, 10500]
car_rentals = [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 8000, 7500, 7000, 6500]
travel_insurance = [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 5000, 4500, 4000, 3500]

plt.figure(figsize=(16, 9))
plt.stackplot(months, hotel_bookings, flight_bookings, car_rentals, travel_insurance, 
              colors=['#8B0000', '#FF4500', '#32CD32', '#4682B4'])

plt.title('Monthly Travel Bookings Breakdown', fontdict={'fontsize': 20}, pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Bookings')

peak_hotel_month = months[hotel_bookings.index(max(hotel_bookings))]
peak_hotel_value = max(hotel_bookings)
plt.text(peak_hotel_month, peak_hotel_value, 'Peak for Hotel Bookings', ha='center', va='bottom', fontsize=12, color='#8B0000')

plt.legend(['Hotel Bookings', 'Flight Bookings', 'Car Rentals', 'Travel Insurance'], loc='upper left')

plt.show()