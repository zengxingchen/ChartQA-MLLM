
import matplotlib.pyplot as plt

data = {
    'Name': ['Running', 'Cycling', 'Swimming', 'Yoga', 'Hiking', 'Weightlifting', 
             'Pilates', 'Dancing', 'Boxing', 'Rowing', 'Tennis', 'Basketball', 
             'Soccer', 'Rock Climbing', 'Martial Arts', 'CrossFit', 'Jump Rope', 
             'Elliptical', 'Spinning', 'Zumba'],
    'Calories Burned (kcal)': [850, 750, 700, 300, 550, 500, 400, 600, 650, 600, 
                               700, 800, 850, 750, 650, 800, 700, 550, 600, 500],
    'Time Spent (minutes)': [60, 45, 50, 90, 120, 45, 60, 75, 60, 45, 60, 90, 
                             90, 120, 60, 60, 30, 45, 50, 60],
    'Satisfaction Level (1-10)': [9, 8, 8.5, 7, 8, 7.5, 7.8, 9.2, 8.7, 8.1, 8.9, 
                                  9.1, 9.3, 8.6, 8.2, 8.4, 7.9, 7.3, 8.3, 7.7]
}

fig, ax = plt.subplots(figsize=(14, 10))

for i in range(len(data['Name'])):
    ax.scatter(data['Calories Burned (kcal)'][i], data['Time Spent (minutes)'][i], 
               s=(data['Satisfaction Level (1-10)'][i] ** 3) * 10,  
               alpha=0.6,
               color=f'#{hex(255 - i*5)[2:].zfill(2)}{hex(100 + i*8)[2:].zfill(2)}{hex(150 + i*5)[2:].zfill(2)}') 

ax.set_title('Sports & Fitness: Calories Burned vs Time Spent with Satisfaction Level as Bubble Size', fontsize=16)
ax.set_xlabel('Calories Burned (kcal)', fontsize=14)
ax.set_ylabel('Time Spent (minutes)', fontsize=14)
ax.grid(True)

plt.show()