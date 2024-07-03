
import matplotlib.pyplot as plt

# Data for stacked area chart
years = range(2012, 2024)
yoga = [9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]
meditation = [7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500]
jogging = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000]
pilates = [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500]

# Plot
plt.figure(figsize=(18, 12))  # Change width and height of the chart
plt.stackplot(years, yoga, meditation, jogging, pilates, 
              colors=['#FF6347', '#4682B4', '#32CD32', '#FFD700'])

# Customize the plot
plt.title('Participation in Wellness Activities from 2012 to 2023', fontsize=20, pad=40)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Number of Participants', fontsize=16)
plt.legend(['Yoga', 'Meditation', 'Jogging', 'Pilates'], loc='upper left', fontsize=12)

# Annotation
for i, y in enumerate(years):
    plt.annotate(f'{yoga[i]}', (y, yoga[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=10)
    plt.annotate(f'{meditation[i]}', (y, yoga[i] + meditation[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=10)
    plt.annotate(f'{jogging[i]}', (y, yoga[i] + meditation[i] + jogging[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=10)
    plt.annotate(f'{pilates[i]}', (y, yoga[i] + meditation[i] + jogging[i] + pilates[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=10)

plt.show()