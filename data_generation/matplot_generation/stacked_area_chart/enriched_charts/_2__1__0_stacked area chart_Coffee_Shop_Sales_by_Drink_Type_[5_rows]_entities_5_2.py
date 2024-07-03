
import matplotlib.pyplot as plt

# Data for each year
years = list(range(2010, 2024))
cardio = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
strength_training = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
flexibility = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
endurance = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Creating a stacked area chart
plt.figure(figsize=(16, 10))
plt.stackplot(years, cardio, strength_training, flexibility, endurance, 
              colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A6'])

# Adding labels and title
plt.title('Fitness Activity Trends (2010-2023)', fontsize=18, pad=30)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Hours per Week', fontsize=14)

# Adding a legend
plt.legend(['Cardio', 'Strength Training', 'Flexibility', 'Endurance'], loc='upper left')

# Annotating the last data point for Endurance
plt.annotate(f'{endurance[-1]} Hours/Week',
             (years[-1], sum([cardio[-1], strength_training[-1], flexibility[-1], endurance[-1]])),
             textcoords="offset points",
             xytext=(0,10),
             ha='center',
             fontsize=12,
             color='#FF33A6')

plt.show()