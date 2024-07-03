
import matplotlib.pyplot as plt

# Data for stacked area chart
years = range(2012, 2023)
mental_health_resources = [1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300, 3500]
physical_fitness_programs = [2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000]
wellness_workshops = [1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800]
nutrition_counseling = [2200, 2500, 2800, 3100, 3400, 3700, 4000, 4300, 4600, 4900, 5200]

# Plot
plt.figure(figsize=(16, 12))
plt.stackplot(years, mental_health_resources, physical_fitness_programs, wellness_workshops, nutrition_counseling, 
              colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A6'])

# Customize the plot
plt.title('Health and Wellness Program Participation from 2012 to 2022', fontsize=18, pad=30)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Number of Participants', fontsize=16)
plt.legend(['Mental Health Resources', 'Physical Fitness Programs', 'Wellness Workshops', 'Nutrition Counseling'], loc='upper right')

# Annotation
for i, y in enumerate(years):
    plt.annotate(f'{mental_health_resources[i]}', (y, mental_health_resources[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{physical_fitness_programs[i]}', (y, mental_health_resources[i] + physical_fitness_programs[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{wellness_workshops[i]}', (y, mental_health_resources[i] + physical_fitness_programs[i] + wellness_workshops[i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{nutrition_counseling[i]}', (y, mental_health_resources[i] + physical_fitness_programs[i] + wellness_workshops[i] + nutrition_counseling[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()