
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Day': list(range(1, 31)),
    'StepsWalked': [
        5200, 5300, 5500, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 
        7200, 7400, 7600, 7800, 8000, 8200, 8400, 8600, 8800, 9000, 
        9200, 9400, 9600, 9800, 10000, 10200, 10400, 10600, 10800, 11000
    ]
})

plt.figure(figsize=(16, 8))
plt.style.use('seaborn-whitegrid')

ax = plt.gca()
ax.plot(data['Day'], data['StepsWalked'], color="#FF6347")
ax.fill_between(data['Day'], data['StepsWalked'], color="#4682B4", alpha=0.5)

highest_steps = data['StepsWalked'].max()
highest_day = data['Day'][data['StepsWalked'].idxmax()]
plt.annotate(f'Highest\n{highest_steps} steps', xy=(highest_day, highest_steps), xytext=(highest_day+2, highest_steps+500),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

plt.title('Daily Steps Walked in January', fontsize=16, pad=20)
plt.xlabel('Day')
plt.ylabel('Steps Walked')

plt.show()