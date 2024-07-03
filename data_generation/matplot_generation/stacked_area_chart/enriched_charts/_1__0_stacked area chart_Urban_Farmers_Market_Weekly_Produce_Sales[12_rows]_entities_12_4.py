
import matplotlib.pyplot as plt

# Data for stacked area chart
years = range(2012, 2023)
basketball = [10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 26000, 28000, 30000]
football = [15000, 17000, 19000, 21000, 23000, 25000, 27000, 29000, 31000, 33000, 35000]
swimming = [8000, 9000, 10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 26000]
tennis = [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]

# Plot
plt.figure(figsize=(14, 9))  # Change width and height of the chart
plt.stackplot(years, basketball, football, swimming, tennis, 
              colors=['#FF6347', '#4682B4', '#32CD32', '#FFD700'])

# Customize the plot
plt.title('Participation in Various Sports Activities from 2012 to 2022', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Participants', fontsize=14)
plt.legend(['Basketball', 'Football', 'Swimming', 'Tennis'], loc='upper right')

# Annotation
for i, y in enumerate(years):
    plt.annotate(f'{basketball[i]}', (y, basketball[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
    plt.annotate(f'{football[i]}', (y, basketball[i] + football[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
    plt.annotate(f'{swimming[i]}', (y, basketball[i] + football[i] + swimming[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
    plt.annotate(f'{tennis[i]}', (y, basketball[i] + football[i] + swimming[i] + tennis[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

plt.show()