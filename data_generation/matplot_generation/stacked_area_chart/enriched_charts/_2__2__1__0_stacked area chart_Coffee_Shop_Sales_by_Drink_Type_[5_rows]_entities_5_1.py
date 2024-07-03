
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
soccer = [14000, 16000, 18000, 22000, 24000, 26000, 28000, 30000, 27000, 25000, 23000, 21000]
basketball = [8000, 8500, 9000, 10000, 10500, 11000, 12000, 12500, 13000, 13500, 14000, 14500]
baseball = [12000, 13500, 14500, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000]
swimming = [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500]

plt.figure(figsize=(14, 8))
plt.stackplot(months, soccer, basketball, baseball, swimming, 
              colors=['#1E90FF', '#32CD32', '#FFD700', '#FF6347'])

plt.title('Monthly Participation in Sports Activities', fontsize=20, pad=30)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Participants', fontsize=14)

peak_soccer_month = months[soccer.index(max(soccer))]
peak_soccer_value = max(soccer)
plt.text(peak_soccer_month, peak_soccer_value, 'Peak for Soccer', ha='center', va='bottom', fontsize=12, color='black')

plt.legend(['Soccer', 'Basketball', 'Baseball', 'Swimming'], loc='upper right', fontsize=12)
plt.show()