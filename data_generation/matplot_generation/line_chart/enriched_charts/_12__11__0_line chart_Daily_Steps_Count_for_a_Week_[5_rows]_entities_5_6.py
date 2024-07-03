
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
calories_burned = [300, 320, 290, 330, 340, 360, 380, 370, 350, 340, 310, 300]

plt.figure(figsize=(16, 9))

plt.plot(months, calories_burned, color='#2ca02c', linewidth=2)

plt.annotate('Peak Activity', xy=('July', 380), xytext=('August', 370),
             arrowprops=dict(facecolor='#d62728', shrink=0.05))

plt.title('Monthly Calories Burned During Exercise in 2023', fontsize=16, loc='left')  
plt.xlabel('Month', fontsize=12)  
plt.ylabel('Calories Burned', fontsize=12)  

plt.show()