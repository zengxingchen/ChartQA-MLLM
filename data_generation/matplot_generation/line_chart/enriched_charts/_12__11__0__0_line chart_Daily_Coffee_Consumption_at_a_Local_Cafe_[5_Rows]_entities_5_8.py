
import matplotlib.pyplot as plt

days = [i for i in range(1, 32)]
calories_individual_a = [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600]
calories_individual_b = [450, 445, 440, 435, 430, 425, 420, 415, 410, 405, 400, 395, 390, 385, 380, 375, 370, 365, 360, 355, 350, 345, 340, 335, 330, 325, 320, 315, 310, 305, 300]

plt.figure(figsize=(12, 7))
plt.plot(days, calories_individual_a, color='#FF6347', label='Individual A')  # Tomato
plt.plot(days, calories_individual_b, color='#4682B4', label='Individual B')  # SteelBlue

plt.title('Daily Calories Burned in January', pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Calories Burned')

plt.annotate('Individual A Peak', xy=(31, calories_individual_a[-1]), xytext=(25, calories_individual_a[-5]),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05))

plt.annotate('Individual B Low', xy=(31, calories_individual_b[-1]), xytext=(25, calories_individual_b[-5]),
             arrowprops=dict(facecolor='#4682B4', shrink=0.05))

plt.grid(True)
plt.legend(loc='upper right')
plt.show()