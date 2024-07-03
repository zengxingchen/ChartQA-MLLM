
import matplotlib.pyplot as plt

months = ['Jan 2021', 'Feb 2021', 'Mar 2021', 'Apr 2021', 'May 2021', 'Jun 2021', 'Jul 2021', 'Aug 2021', 'Sep 2021', 
          'Oct 2021', 'Nov 2021', 'Dec 2021', 'Jan 2022', 'Feb 2022', 'Mar 2022', 'Apr 2022', 'May 2022', 'Jun 2022', 
          'Jul 2022', 'Aug 2022', 'Sep 2022', 'Oct 2022', 'Nov 2022', 'Dec 2022']
destination_a = [15000, 16000, 15500, 16500, 17500, 18500, 19500, 20500, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 
                 28000, 29000, 30000, 31000, 32000, 33000, 34000, 35000, 36000]
destination_b = [13000, 14000, 14500, 15000, 16000, 17000, 18000, 18500, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 
                 26000, 27000, 28000, 29000, 30000, 31000, 32000, 33000, 34000]
destination_c = [12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000, 
                 19500, 20000, 20500, 21000, 21500, 22000, 22500, 23000, 23500]

plt.figure(figsize=(14, 10))
plt.stackplot(months, destination_a, destination_b, destination_c, 
              labels=['Destination A', 'Destination B', 'Destination C'],
              colors=['#FF4500', '#1E90FF', '#3CB371'])

plt.title('Monthly Visitor Counts to Popular Travel Destinations', pad=20)
plt.xlabel('Month')
plt.ylabel('Visitor Count')

plt.annotate('Peak for Destination A', xy=(23, 36000), xytext=(15, 50000),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.legend(loc='upper right')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()